import datetime
import os

import disnake
from disnake.ext import commands

from tokens import tokens

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    intents=disnake.Intents.all(),
    activity=disnake.Game("drewsupport.github.io"),
    status=disnake.Status.idle
)

bot.remove_command('help')


# TEST
@bot.command()
async def host(ctx):
    await ctx.send(
        f"Current host time: {datetime.datetime.now().ctime()}\n"
        f"Start host time: {startTime}"
    )


# RUN
@bot.event
async def on_ready():
    print(f"Logged as {bot.user} (USER ID: {bot.user.id})\n"
          f"Start time: {startTime}")


for category in os.listdir("cogs"):
    for file in os.listdir(f"cogs/{category}"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{category}.{file[:-3]}")

startTime = datetime.datetime.now().ctime()
bot.run(tokens['debug'])
