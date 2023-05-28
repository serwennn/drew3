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
        description = "Статистика этого сервера",
        dm_permission = False
    )
    async def server(
        self, ctx: ApplicationCommandInteraction,
    ) -> None:
        
        embed = Embed(
            title = f"🌸・Статистика **{ ctx.guild.name }**",
            description = f"Владелец: { ctx.guild.owner.mention } ({ ctx.guild.owner })\nСоздан: <t:{ int(ctx.guild.created_at.timestamp()) }>",
            color = configs['color']
        )
        if ctx.guild.icon != None: embed.set_thumbnail(ctx.guild.icon)

        member_bot_count = 0
        for member in ctx.guild.members:
            if member.bot == True: member_bot_count += 1

        ver_level_raw = ctx.guild.verification_level.name
        if ver_level_raw == "none": ver_level = "Отсутствует (Кто-угодно может зайти на сервер)"
        elif ver_level_raw == "low": ver_level = "Низкий (Участнику необходимо иметь подтвержденный Email)"
        elif ver_level_raw == "medium": ver_level = "Средний (Подтвержденный Email и 5 минут с регистрации аккаунта)"
        elif ver_level_raw == "high": ver_level = "Высокий (Должен быть участником этого сервера больше 10 минут)"
        elif ver_level_raw == "highest": ver_level = "Самый высокий (Участник должен иметь подтвержденный номер телефона)"

        embed.add_field(
            name = "👤・Участники:",
            value = f"Всего: { ctx.guild.member_count }\nЛюдей: { ctx.guild.member_count - member_bot_count }\nБотов: { member_bot_count }",
            inline = True
        )
        embed.add_field(
            name = "☕・Каналы:",
            value = f"Всего: { len(ctx.guild.channels) }\nТекстовые: { len(ctx.guild.text_channels) }\nГолосовые: { len(ctx.guild.voice_channels) }",
            inline = True
        )
        embed.add_field(
            name = "✨・Прочее:",
            value = f"Всего категорий: { len(ctx.guild.categories) }\nРолей: { len(ctx.guild.roles) }\nЭмодзи: { len(ctx.guild.emojis) }",
            inline = True
        )
        embed.add_field(
            name = "🛡️・Уровень проверки (верификации):",
            value = ver_level,
            inline = False
        )

        await ctx.send(embed = embed)


def setup(bot: commands.Bot) -> None:
    bot.add_cog(Server(bot))
