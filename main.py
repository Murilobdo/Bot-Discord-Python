import discord
from discord.ext import commands


bot = discord.Client()

#Inicialização do bot
@bot.event
async def on_ready():
    print(f'Logado: {bot.user}')

#Log
@bot.event
async def on_message(message):
    print(f'Message de {message.author}: {message.content}')
    await bot.process_commands(message)

#Comandos
@bot.command(name="ola")
async def ola(message):
    await message.channel.send("Olá, você faz parte da turma? Caso não, venha fazer parte! :D")

@bot.command(name="tabnews")
async def tabnews(message):
    await message.channel.send("O Tabnews é uma plataforma que podemos compartilhar experiência, informações e notícias sobre tecnologia, idealizado pelo Filipe Deschamps.")

#Token
bot.run(token='TOKEN')