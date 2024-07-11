from aiogram import Bot, Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from deliverydetect.core.enums import Role, transport, confirmation
from deliverydetect.core.database import sessionmaker
from deliverydetect.core.settings import _
from deliverydetect.models.callback import RoleCallback
from deliverydetect.models.database import Courier
from deliverydetect.bot.states import GetCourierInfo
from deliverydetect.bot.keyboards import yes_no_kb, choose_transport_kb


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
    await msg.reply(_('Do you have a thermal bag?'), reply_markup=yes_no_kb)
    await state.set_state(GetCourierInfo.GET_HAS_THERMAL_BAG)


@router.message(StateFilter(GetCourierInfo.GET_HAS_THERMAL_BAG))
async def get_has_thermal_bag(msg: types.Message, state: FSMContext):
    if msg.text not in list(confirmation.keys()) or msg.text is None:
        await state.set_state(GetCourierInfo.GET_HAS_THERMAL_BAG)
        return await msg.reply(_('Invalid input. Use buttons'), reply_markup=yes_no_kb)

    await state.update_data(data={'has_thermal_bag': confirmation[msg.text]})
    await msg.reply(_('What kind of transport do you use?'), reply_markup=choose_transport_kb)
    await state.set_state(GetCourierInfo.GET_TRANSPORT)


@router.message(StateFilter(GetCourierInfo.GET_TRANSPORT))
async def get_transport(msg: types.Message, state: FSMContext):
    if msg.text not in transport.keys() or msg.text is None:
        await state.set_state(GetCourierInfo.GET_TRANSPORT)
        return await msg.reply(_('Invalid input. Use buttons'), reply_markup=choose_transport_kb)

    await state.update_data(data={'transport': transport[msg.text]})
    data = await state.get_data()
    await msg.reply(
        text=_(f'''<b>Your data:</b>
Name - {data['name']}
Contact - {data['contact']}
Has thermal bag - {'да' if data['has_thermal_bag'] else 'нет'}
Transport - {msg.text[2:].lower()}

Do you confirm it?'''),
        reply_markup=yes_no_kb,
        parse_mode='html'
    )
    await state.set_state(GetCourierInfo.CONFIRM)


@router.message(StateFilter(GetCourierInfo.CONFIRM))
async def confirm(msg: types.Message, state: FSMContext):
    if msg.text not in list(confirmation.keys()) or msg.text is None or msg.from_user is None:
        await state.set_state(GetCourierInfo.CONFIRM)
        return await msg.reply(_('Invalid input. Use buttons'))

    if confirmation[msg.text] is True:
        await msg.reply(_('Saving data... Bot usage - /help'))
        data = await state.get_data()
        courier = Courier(
            telegram_id=int(msg.from_user.id),
            name=data['name'],
            contact=data['contact'],
            has_thermal_bag=data['has_thermal_bag'],
            transport=data['transport']
        )
        async with sessionmaker() as session:
            session.add(courier)
            await session.commit()

        return await state.clear()

    await msg.reply(_('Okay, let\'s enter your data again. What is your name?'))
    await state.clear()
    await state.set_state(GetCourierInfo.GET_NAME)
