from disnake import ApplicationCommandInteraction, Member
from disnake.ext import commands


class Mute(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_load(self) -> None:
        print(f"[COG] {self.__cog_name__} was loaded.")

    @commands.slash_command(
        name="mute",
        description="Мьютит участника.",
        dm_permission=False
    )
    async def mute(
        self, ctx: ApplicationCommandInteraction,
        member: Member,
        time: int,
        reason: str = "не указано."
    ) -> None:
        await member.timeout(duration=time, reason=reason)
        await ctx.send(
            f"Участник {member.mention} получил мьют на {time} секунд, по причине: {reason}")


def setup(bot: commands.Bot) -> None:
    bot.add_cog(Mute(bot))
