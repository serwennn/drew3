from disnake import ApplicationCommandInteraction
from disnake.ext import commands


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
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("У вас недостаточно полномочий для выполнения команды.")
        



def setup(bot: commands.Bot) -> None:
    bot.add_cog(ErrorHandler(bot))