import datetime
import os

import disnake
from disnake.ext import commands

from configs import tokens

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    intents=disnake.Intents.all(),
    activity=disnake.Game("github.com/nassendg/drew3"),
    status=disnake.Status.idle
)

bot.remove_command('help')

# RUN


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (USER ID: {bot.user.id})\n"
          f"Start time: {start_time}")


# Loading cogs
for category in os.listdir("cogs"):
    bot.load_extensions(f"cogs/{category}")

start_time = datetime.datetime.now().ctime()
bot.run(tokens['debug'])
