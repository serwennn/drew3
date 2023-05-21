from disnake import ApplicationCommandInteraction
from disnake.ext import commands


class Purge(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_load(self) -> None:
        print(f"[COG] {self.__cog_name__} was loaded.")

    @commands.slash_command(
        name = "purge",
        description = "Удаляет сообщения.",
        dm_permission = False
    )
    async def purge(self, ctx: ApplicationCommandInteraction, count: int) -> None:
        messages = await ctx.channel.purge(limit=count)
        await ctx.send(f"Было очищено {len(messages)} сообщений.", ephemeral=True)


def setup(bot: commands.Bot) -> None:
    bot.add_cog(Purge(bot))
