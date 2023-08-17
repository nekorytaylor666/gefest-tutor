# import discord
# from discord.ext import commands

from discord.ext import commands
from config import DISCORD_BOT_KEY
# from tutor import ask
# from discord import app_commands

import discord
from discord import app_commands

from tutor import ask

TOKEN = DISCORD_BOT_KEY

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


bot = commands.Bot(command_prefix='?',
                   description=description, intents=intents)


synonims = ['гефест', 'Гефест', "Gefest", "gefest"]


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    print(message)
    if message.author == client.user:
        return
    # if message content contains any from synonims
    if any(synonim in message.content for synonim in synonims):
        # await message.channel.send('Hello!')
        question = message.content[7:]
        print(question)
        answer = await ask(question)
        await message.reply(answer, mention_author=True)


client.run(TOKEN)
