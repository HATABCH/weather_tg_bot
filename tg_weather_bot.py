import datetime
import requests
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет, скинь городок")

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={message.text}&limit=5&appid={open_weather_token}")
        data = r.json()
        # pprint(data)

        lat = data[0]['lat']
        lon = data[0]['lon']

        t = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={open_weather_token}&units=metric")
        dataa = t.json()
        # pprint(dataa)

        city = dataa['name']
        temp = dataa['main']['temp']
        wind = dataa['wind']['speed']
        weather = dataa['weather'][0]['main']
        await message.reply(
            f'Погода в городе {city} на {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}: \nСостояние: {weather} \nТемпература: {temp}, \nСкорость ветра: {wind}')



    except:
        await message.reply("не чую")


#def main():
    #city =
    # state = input('state хочеца')
    # country = input('Ну и страну')

    #get_weather(city, open_weather_token)

if __name__ == '__main__':
    executor.start_polling(dp)