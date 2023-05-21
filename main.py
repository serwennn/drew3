import datetime
import os

import disnake
from disnake.ext import commands

from configs import tokens

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
        f"Start host time: {start_time}"
    )


# RUN
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (USER ID: {bot.user.id})\n"
          f"Start time: {start_time}")


for category in os.listdir("cogs"):
    if category.endswith(".py"):
        bot.load_extension(f"cogs.{category[:-3]}")
    else:
        for file in os.listdir(f"cogs/{category}"):
            if file.endswith(".py"):
                bot.load_extension(f"cogs.{category}.{file[:-3]}")

start_time = datetime.datetime.now().ctime()
bot.run(tokens['debug'])
