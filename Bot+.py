from aiogram import Bot, Dispatcher, executor, types
from decouple import config
from random import choice


bot = Bot(config('API_TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Здравствуй, я Элоер👋")
    print(message)

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer('Я Элоер, у меня есть команды "start" и "help"👀')
    await message.answer('Можешь написать мне: Привет, Какая погода?, Как дела?, Пока, Сколько тебе лет?, Сколько время?, Как тебя зовут? или кинь кости🤝')
    print(message)

@dp.message_handler(content_types=['dice'])
async def dice(message: types.Message):
    await message.answer("Ты кинул куб")
    print(message)

answers = {
    'привет': 'hello.txt',
    'как дела?': 'how.txt',
    'как тебя зовут?': 'name.txt',
    'сколько тебе лет?': 'age.txt',
    'сколько времени?': 'time.txt',
    'какая погода?': 'weather.txt',
    'пока':'bye.txt'
}

@dp.message_handler()
async def echo(message: types.Message):
    if message.text in answers:
        with open(f'answers/{answers[message.text]}', 'r', encoding='utf-8') as file:
            variants = file.read().split('\n')
        await message.answer(choice(variants))
    else:
        await message.answer('Не понимаю что ты пристал, но вот команды: /help')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
