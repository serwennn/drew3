from disnake import ApplicationCommandInteraction, Embed
from disnake.ext import commands

from configs import configs, macros


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
        
        embed = Embed(color=configs['color'])

        if isinstance(error, commands.MissingPermissions):
            embed.description = "Хм, видимо у вас недостаточно прав для выполнения этой команды."
        elif isinstance(error, commands.BotMissingPermissions):
            embed.description = "Хм, видимо у меня недостаточно прав для выполнения этой команды."
        else:
            embed.description = f"Хм, видимо произошла какая-то непредвиденная ошибка. " \
                                f"Свяжитесь с {macros['seruen_link']} и отправьте ему это: \n```{error}```"
        await ctx.send(embed=embed)


def setup(bot: commands.Bot) -> None:
    bot.add_cog(ErrorHandler(bot))
