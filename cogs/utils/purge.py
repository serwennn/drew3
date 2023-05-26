from disnake import ApplicationCommandInteraction, Embed
from disnake.ext import commands

from configs import configs

class Purge(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_load(self) -> None:
        print(f"[COG] {self.__cog_name__} was loaded.")

    @commands.slash_command(
        name = "purge",
        description = "Удаляет сообщения",
        dm_permission = False
    )
    @commands.has_permissions(manage_messages = True)
    @commands.bot_has_permissions(manage_messages = True)
    async def purge(
        self, ctx: ApplicationCommandInteraction,
        count: int
    ) -> None:
        messages = await ctx.channel.purge(limit=count)

        embed = Embed(
            description = f"Было очищено { len(messages) } из { count } сообщений.",
            color = configs['color']
        )

        if len(messages) < count: embed.set_footer(text = "Некоторые сообщения могли быть проигнорированы.")

        await ctx.send(embed = embed, ephemeral=True)


def setup(bot: commands.Bot) -> None:
    bot.add_cog(Purge(bot))
