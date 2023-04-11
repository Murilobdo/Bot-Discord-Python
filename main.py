
import discord
import requests

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    def getRandomAnimal(self):
        response = requests.get('https://goweather.herokuapp.com/weather/sorocaba')
        return f'Hoje está {response.json()["temperature"]} em Sorocaba!'
        
    async def on_message(self, message):
        if(message.content.startswith('!temperatura')):
            text = self.getRandomAnimal()
            await message.channel.send(text)

intents = discord.Intents.all()
client = MyClient(intents=intents)

client.run('SEU TOKEN DO DISCORD DEVELOPER')