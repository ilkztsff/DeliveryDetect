from aiogram import Bot, Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from deliverydetect.core.enums import Role, Transport
from deliverydetect.core.database import sessionmaker
from deliverydetect.core.settings import _
from deliverydetect.models.callback import RoleCallback, TransportCallback, ConfirmationCallback
from deliverydetect.models.database import Courier
from deliverydetect.bot.states import GetCourierInfo
from deliverydetect.bot.keyboards import yes_no_ikb, choose_transport_ikb


router = Router()


@router.callback_query(RoleCallback.filter(F.role == Role.COURIER))
async def add_info(call: types.CallbackQuery, bot: Bot, callback_data: RoleCallback, state: FSMContext):
    await bot.send_message(
        text=_('What is your name?'),
        chat_id=call.from_user.id,
        reply_markup=types.ReplyKeyboardRemove()
    )
    await state.set_state(GetCourierInfo.GET_NAME)
    await call.answer()


@router.message(StateFilter(GetCourierInfo.GET_NAME))
async def get_name(msg: types.Message, state: FSMContext):
    await state.set_data(data={'name': msg.text})
    await msg.reply(_('Okay, now send your phone number'), reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(GetCourierInfo.GET_CONTACT)


@router.message(StateFilter(GetCourierInfo.GET_CONTACT))
async def get_contact(msg: types.Message, state: FSMContext):
    await state.update_data(data={'contact': msg.text})
    await msg.reply(_('Do you have a thermal bag?'), reply_markup=yes_no_ikb)
    await state.set_state(GetCourierInfo.GET_HAS_THERMAL_BAG)


@router.callback_query(StateFilter(GetCourierInfo.GET_HAS_THERMAL_BAG))
async def get_has_thermal_bag(call: types.CallbackQuery, bot: Bot, callback_data: ConfirmationCallback, state: FSMContext):
    if not isinstance(call.data, bool):
        await state.set_state(GetCourierInfo.GET_HAS_THERMAL_BAG)
        return await bot.send_message(
            text=_('Invalid input - use buttons. Do you have a thermal bag?'),
            chat_id=call.from_user.id,
            reply_markup=yes_no_ikb
        )

    await state.update_data(data={'has_thermal_bag': call.data})
    await bot.send_message(
        text=_('What kind of transport do you use?'),
        chat_id=call.from_user.id,
        reply_markup=choose_transport_ikb
    )
    await state.set_state(GetCourierInfo.GET_TRANSPORT)


@router.callback_query(StateFilter(GetCourierInfo.GET_TRANSPORT))
async def get_transport(call: types.CallbackQuery, bot: Bot, callback_data: TransportCallback, state: FSMContext):
    if not isinstance(call.data, Transport):
        await state.set_state(GetCourierInfo.GET_TRANSPORT)
        return await bot.send_message(
            text=_('Invalid input - use buttons. What kind of transport do you use?'),
            chat_id=call.from_user.id,
            reply_markup=choose_transport_ikb
        )

    await state.update_data(data={'transport': call.data})
    data = await state.get_data()
    await bot.send_message(
        text=_(f'''<b>Your data:</b>
Name - {data['name']}
Contact - {data['contact']}
Has thermal bag - {_('yes') if data['has_thermal_bag'] else _('no')}
Transport - {call.data}

Do you confirm it?'''),
        chat_id=call.from_user.id,
        reply_markup=yes_no_ikb,
        parse_mode='html'
    )
    await state.set_state(GetCourierInfo.CONFIRM)


@router.callback_query(StateFilter(GetCourierInfo.CONFIRM))
async def confirm(call: types.CallbackQuery, bot: Bot, callback_data: ConfirmationCallback, state: FSMContext):
    if not isinstance(call.data, bool):
        await state.set_state(GetCourierInfo.CONFIRM)
        return await bot.send_message(
            text=_('Invalid input - use buttons. Is your data correct?'),
            chat_id=call.from_user.id
        )

    if call.data:
        await call.message.answer(_('Saving data... Bot usage - /help'))
        data = await state.get_data()
        courier = Courier(
            telegram_id=int(call.from_user.id),
            name=data['name'],
            contact=data['contact'],
            has_thermal_bag=data['has_thermal_bag'],
            transport=data['transport']
        )
        async with sessionmaker() as session:
            session.add(courier)
            await session.commit()

        return await state.clear()

    await call.message.answer(_('Okay, let\'s enter your data again. What is your name?'))
    await state.clear()
    await state.set_state(GetCourierInfo.GET_NAME)
