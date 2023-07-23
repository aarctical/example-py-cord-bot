import time
BotStartupTime = time.time()

import discord
from discord.ext import commands
import os
import asyncio
import json
import math
from configfunctions import GetActivity, GetStatus

with open('configuration.json') as cfg:
    config = json.load(cfg)

bot = commands.Bot(command_prefix=config['prefix'], description=config['description'], intents=discord.Intents.all(), activity=GetActivity(), status=GetStatus())

for filename in os.listdir('./cogs'): # //
    if filename.endswith('.py'): #      || Do not touch this unless you are putting your cogs into sys folder-files, seek support if so.
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f"Loaded: {filename[:-3]}")

@bot.event
async def on_ready():
    print(f"{bot.user.name} is now online! ({config['status'].upper()}: {config['activity-type']} {config['activity-data']})")

@bot.slash_command(name="status", help="Check the status of the bot", description="Check how long the bot has been online, and its connection!")
async def status(ctx):
    await ctx.respond(f"{bot.user.name}'s uptime is {math.floor((time.time()-BotStartupTime) / 60)} minutes with a ping of {math.floor(bot.latency)}ms", delete_after=5, ephemeral=True)

bot.run(config['token'])