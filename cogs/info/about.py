from disnake import ApplicationCommandInteraction, Embed
from disnake.ext import commands

from configs import configs, macros


class About(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_load(self) -> None:
        print(f"[COG] {self.__cog_name__} was loaded.")

    @commands.slash_command(
        name = "about",
        description = "О DrewBot и его авторах <3",
        dm_permission = False
    )
    async def about(
        self, ctx: ApplicationCommandInteraction,
    ) -> None:
        
        embed = Embed(
            title = "🦊・О DrewBot:",
            description = "DrewBot — бот, для модерации вашего сервера. Его главная цель — автоматическое модерирование серверов, но он также имеет пару других функций. Он постоянно развивается, и в нем добавляются или изменяются различные функции.",
            color = configs['color']
        )
        embed.add_field(
            name = "📀・О проекте:",
            value = f"У DrewBot только один разработчик, и это { macros['seruen_link'] }. Но в его развитии участвуют множество других авторов и обычных людей, которые привносят свой вклад в проект! Вы тоже можете помочь нам в его развитии, подробнее на [странице репозитория проекта](https://github.com/nassendg/drew3).",
            inline = False
        )
        embed.add_field(
            name = "🚧・Справочная информация:",
            value = f"Обратиться с вопросом или предложением можно к: { macros['seruen_link'] }."
        )
        embed.add_field(
            name = "⚙️・Техническая информация:",
            value = f"Версия: { configs['version'] }\nДата релиза: { configs['date'] }\nКол-во серверов: { len(self.bot.guilds) }\nПинг: { round(self.bot.latency * 1000) }мс."
        )
        embed.set_footer(text = "(c) 2022-2023 DrewSupport.kz (seruen) — Сүйіспеншілікпен істеген <3")

        await ctx.send(embed = embed)


def setup(bot: commands.Bot) -> None:
    bot.add_cog(About(bot))
