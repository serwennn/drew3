from disnake import ApplicationCommandInteraction, Embed
from disnake.ext import commands

from configs import configs


class Server(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_load(self) -> None:
        print(f"[COG] {self.__cog_name__} was loaded.")

    @commands.slash_command(
        name = "server",
        description = "Информация о этом сервере",
        dm_permission = False
    )
    async def server(
        self, ctx: ApplicationCommandInteraction,
    ) -> None:
        
        embed = Embed(
            title = f"🌸・О **{ctx.guild.name}**",
            color = configs['color']
        )
        if ctx.guild.icon != None: embed.set_thumbnail(ctx.guild.icon)

        member_bot_count = 0
        for member in ctx.guild.members:
            if member.bot == True: member_bot_count += 1

        embed.add_field(
            name = "👤・Участники:",
            value = f"Всего: { ctx.guild.member_count }\nЛюдей: { ctx.guild.member_count - member_bot_count }\nБотов: { member_bot_count }",
            inline = True
        )
        embed.add_field(
            name = "☕・Каналы:",
            value = f"sdansdauinfue"
        )
        embed.add_field(
            name = "・Прочее:",
            value = f"smfoiesfoimesois"
        )

        await ctx.send(embed = embed)


def setup(bot: commands.Bot) -> None:
    bot.add_cog(Server(bot))
