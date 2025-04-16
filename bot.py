
           f"👧 Ребёнок: {data['child_name']}, {data['child_age']} лет\n"            f"📞 Контакт: {data['contact']}\n"            f"🏅 Опыт: {data.get('has_experience', 'Нет')}\n"            f"📝 Вид спорта: {data.get('sport_experience', '—')}"

    await bot.send_message(trainer_username, info)
    await message.answer("Спасибо! Ваша заявка отправлена ✅", reply_markup=main_kb)
    await state.finish()

@dp.message_handler(lambda m: m.text == "📩 Связаться с руководством")
async def contact_admin(message: types.Message):
    await message.answer("Вы можете написать руководству сюда: @bobryshevv")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
