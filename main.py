
import discord
import requests

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    def getRandomAnimal(self, city):
        response = requests.get(f'https://goweather.herokuapp.com/weather/{city}')
        return f'Hoje está {response.json()["temperature"]} em {city}!'
        
    async def on_message(self, message):
        city = message.content.split('!temp-')[1]
        if(city is not '' or None):
            text = self.getRandomAnimal(city)
            await message.channel.send(text)
        else:
            await message.channel.send('comando inválido, o correto é !temp-[cidade-alvo]')

intents = discord.Intents.all()
client = MyClient(intents=intents)

client.run('TOKEN DISCORD')