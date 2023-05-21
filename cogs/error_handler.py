from disnake import ApplicationCommandInteraction, Embed
from disnake.ext import commands

from configs import configs

class ErrorHandler(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_load(self) -> None:
        print(f"[COG] {self.__cog_name__} was loaded.")

    @commands.Cog.listener()
    async def on_slash_command_error(
        self, ctx: ApplicationCommandInteraction,
        error
    ) -> None:
        
        embed = Embed(color = configs['color'])
        if isinstance(error, commands.MissingPermissions):
            embed.description = "У вас недостаточно полномочий для выполнения команды."
        elif isinstance(error, commands.BotMissingPermissions):
            embed.description = "У меня недостаточно полномочий для выполнения команды."
        else:
            embed.description = f"Похоже произошла какая-то непредвиденная ошибка. Свяжитесь с seru#2356 ([Ссылка на аккаунт](https://discordapp.com/users/735371414533701672)) и отправьте ему это:\n```{error}```"
        await ctx.send(embed = embed)
        



def setup(bot: commands.Bot) -> None:
    bot.add_cog(ErrorHandler(bot))