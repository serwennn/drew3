from disnake import ApplicationCommandInteraction, Embed, Member
from disnake.ext import commands

from configs import configs


class User(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_load(self) -> None:
        print(f"[COG] {self.__cog_name__} was loaded.")

    @commands.slash_command(
        name="user",
        description="Информация о участнике",
        dm_permission=False
    )
    async def user(
        self, ctx: ApplicationCommandInteraction,
        member: Member = None
    ) -> None:
        
        if member == None: member = ctx.author

        status = "Не в сети"
        if member.raw_status == "online": status = "В сети"
        elif member.raw_status == "idle": status = "Неактивен"
        elif member.raw_status == "dnd": status = "Не беспокоить"

        premium_since = "Нет бустов"
        if member.premium_since != None: premium_since = f"<t:{ int(member.premium_since.timestamp()) }>"
        
        embed = Embed(
            title=f"🌸・Информация о **{ member.name }**",
            color=configs['color']
        )

        if member.avatar != None: embed.set_thumbnail(member.avatar)
        print(member.premium_since)

        embed.add_field(
            name="☀️・Статус:",
            value=status,
            inline=True
        )
        embed.add_field(
            name="🧬・ID:",
            value=f"`{ member.id }`",
            inline=True
        )
        embed.add_field(
            name="👋・Присоединился к серверу:",
            value=f"<t:{ int(member.joined_at.timestamp()) }>",
            inline=False
        )
        embed.add_field(
            name="🚀・Буст сервера с:",
            value=premium_since,
            inline=False
        )
        embed.add_field(
            name="🎭・Высшая роль:",
            value=f"{ member.top_role.mention } ({ member.top_role.name })",
            inline=False
        )

        await ctx.send(embed=embed)


def setup(bot: commands.Bot) -> None:
    bot.add_cog(User(bot))
