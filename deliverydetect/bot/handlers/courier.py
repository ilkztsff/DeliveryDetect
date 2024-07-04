from aiogram import Bot, Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from deliverydetect.models.callback import RoleCallback
from deliverydetect.core.enums import Role, transport, confirmation
from deliverydetect.bot.states import GetCourierInfo
from deliverydetect.bot.keyboards import yes_no_kb, choose_transport_kb


router = Router()


@router.callback_query(RoleCallback.filter(F.role == Role.COURIER))
async def edit_info(call: types.CallbackQuery, bot: Bot, callback_data: RoleCallback, state: FSMContext):
    await bot.send_message(text='Как тебя зовут?\n(Укажи имя и фамилию)', chat_id=call.from_user.id)
    await state.set_state(GetCourierInfo.GET_NAME)
    await call.answer()


@router.message(StateFilter(GetCourierInfo.GET_NAME))
async def get_name(msg: types.Message, state: FSMContext):
    await state.set_data(data={'name': msg.text})
    await msg.reply('Окей, теперь укажи свой номер телефона')
    await state.set_state(GetCourierInfo.GET_CONTACT)


@router.message(StateFilter(GetCourierInfo.GET_CONTACT))
async def get_contact(msg: types.Message, state: FSMContext):
    await state.update_data(data={'contact': msg.text})
    await msg.reply('У тебя есть термосумка?', reply_markup=yes_no_kb)
    await state.set_state(GetCourierInfo.GET_HAS_THERMAL_BAG)


@router.message(StateFilter(GetCourierInfo.GET_HAS_THERMAL_BAG))
async def get_has_thermal_bag(msg: types.Message, state: FSMContext):
    if msg.text not in list(confirmation.keys()) or msg.text is None:
        await state.set_state(GetCourierInfo.GET_HAS_THERMAL_BAG)
        return await msg.reply('Некорректный ввод. Используйте кнопки')

    await state.update_data(data={'has_thermal_bag': confirmation[msg.text]})
    await msg.reply('Какой транспорт вы используете?', reply_markup=choose_transport_kb)
    await state.set_state(GetCourierInfo.GET_TRANSPORT)


@router.message(StateFilter(GetCourierInfo.GET_TRANSPORT))
async def get_transport(msg: types.Message, state: FSMContext):
    if msg.text not in transport.keys() or msg.text is None:
        await state.set_state(GetCourierInfo.GET_TRANSPORT)
        return await msg.reply('Некорректный ввод. Используйте кнопки')

    await state.update_data(data={'transport': transport[msg.text]})
    data = await state.get_data()
    await msg.reply(
        text=f'''<b>Ваша информация:</b>
Имя - {data['name']}
Номер телефона - {data['contact']}
Наличие термосумки - {'да' if data['has_thermal_bag'] else 'нет'}
Транспорт - {msg.text[2:].lower()}

Подтвердить?''',
        reply_markup=yes_no_kb,
        parse_mode='html'
    )
    await state.set_state(GetCourierInfo.CONFIRM)


@router.message(StateFilter(GetCourierInfo.CONFIRM))
async def confirm(msg: types.Message, state: FSMContext):
    if msg.text not in list(confirmation.keys()) or msg.text is None:
        await state.set_state(GetCourierInfo.CONFIRM)
        return await msg.reply('Некорректный ввод. Используйте кнопки')

    if confirmation[msg.text] is True:
        await msg.reply('Сохраняем данные. Помощь по боту - /help')
        return await state.clear()

    await msg.reply('Хорошо, давай заново заполним форму. Введи своё имя')
    await state.set_state(GetCourierInfo.GET_NAME)
