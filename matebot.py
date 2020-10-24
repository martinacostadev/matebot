# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} se ha conectado a tu Discord!')


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logueado como', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

        if message.content == 'Hola!':
            await message.channel.send('¡Hola! ¿Cómo estás? Bienvenido a mi Servidor, soy un proyecto de miembros de FrontEndCafé. ¿Querés un matesito? :)')

client = MyClient()

client.run(TOKEN)