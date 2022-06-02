# Copyright 2022 Thomas Gingele (https://github.com/b1tc0r3)

'''
This module contains the bots framework
'''

from discord.ext.commands import Bot
from discord              import Intents

description = "Read this from file later"
intents = Intents.default()

bot = Bot(command_prefix="b/", description=description, intents=intents)

@bot.event
async def on_ready():
    '''
    Print basic information when the bot is ready
    '''
    print("# BOT READY #\n"+\
         f"Name: {bot.user.name}\n"+\
         f"ID  : {bot.user.id}\n")

@bot.command
async def status():
    '''
    Command to check whether the bot is resposive on discord
    '''
    print("# SIGNAL RECEIVED #")

bot.run(input("Token: "))
