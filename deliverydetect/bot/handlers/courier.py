from aiogram import Bot, Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from deliverydetect.models.callback import RoleCallback
from deliverydetect.core.enums import Role
from deliverydetect.bot.states import GetCourierInfo


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
    await msg.reply('У тебя есть термосумка?')
    await msg.answer(str(await state.get_data()))
