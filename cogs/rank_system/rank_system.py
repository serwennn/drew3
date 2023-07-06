from disnake import ApplicationCommandInteraction, Embed, Member
from disnake.ext import commands

import async_db
from random import randint

from configs import configs


class RankSystem(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_load(self) -> None:
        print(f"[COG] {self.__cog_name__} was loaded.")

        await create_exp_table()

    @commands.slash_command(
        name = "rank",
        description = "Показать текущий ранг участника",
        dm_permission = False
    )
    async def rank(
        self, inter: ApplicationCommandInteraction,
        member: Member = None
    ) -> None:
        
        if member == None: member = inter.author

        exp_data = await select_data(member_id=member.id, guild_id=inter.guild.id)

        if exp_data == None: exp = 0
        else: exp = exp_data[0]

        level_data = await get_level(exp=exp)
        if level_data == None: level_data = (0, 182)

        embed = Embed(
            title = f"🚀・Ранг {member.name}:",
            description = f"Текущий уровень: {level_data[0]}\n"
                          f"До следующего ранга: {exp}/{level_data[1]}",
            color = configs['color']
        )

        await inter.send(embed=embed)
    
    
    @commands.Cog.listener()
    async def on_message(
        self, inter: ApplicationCommandInteraction
    ) -> None:
        
        if inter.author.bot == True: return

        data = await select_data(guild_id=inter.guild.id, member_id=inter.author.id)

        min_per = 20
        max_per = 25

        # exp = int( len(inter.content) * ( randint(min_per, max_per)/100 ) )
        exp = randint(min_per, max_per)

        if data != None:

            last_msg_timestamp = data[1]

            if inter.created_at.timestamp() - last_msg_timestamp < 12: return

            total_exp = data[0] + exp
            level_data = await get_level(exp=data[0])

            if total_exp > level_data[1]:
                embed = Embed(
                    description = f"{inter.author.name} получил {level_data[0] + 1} уровень.",
                    color = configs['color']
                )

                await inter.reply(embed=embed)

        await add_exp(member_id=inter.author.id, guild_id=inter.guild.id, exp=exp, last_msg_timestamp=inter.created_at.timestamp())


@async_db.async_with_connection
async def create_exp_table(
    connection
):
    cursor = await connection.cursor()
    await cursor.execute(
        """ CREATE TABLE IF NOT EXISTS experience (member_id INTEGER, guild_id INTEGER, exp INTEGER, last_msg_timestamp INTEGER) """
    )


@async_db.async_with_connection
async def select_data(
    connection, guild_id, member_id
):
    cursor = await connection.cursor()
    await cursor.execute(
        """ SELECT exp, last_msg_timestamp FROM experience WHERE guild_id = ? AND member_id = ? """,
        (guild_id, member_id,)
    )
    data = await cursor.fetchone()

    return data


@async_db.async_with_connection
async def add_exp(
    connection,
    member_id, guild_id, exp, last_msg_timestamp
):
    cursor = await connection.cursor()

    data = await select_data(guild_id=guild_id, member_id=member_id)

    if data == None:
        await cursor.execute(
            """ INSERT INTO experience VALUES (?, ?, ?, ?) """,
            (member_id, guild_id, exp, last_msg_timestamp,)
        )
    else:
        await cursor.execute(
            """ UPDATE experience SET exp = ?, last_msg_timestamp = ? WHERE guild_id = ? AND member_id = ? """,
            (data[0] + exp, last_msg_timestamp, guild_id, member_id,)
        )


async def get_level(
    exp
):
    initial_num = 175
    percent = 1.04
    past_total_exp = 0

    for level in range(176): # until 175 lvl
        total_exp = level * initial_num

        if past_total_exp < exp < total_exp: return (level, total_exp)
        
        initial_num = int(initial_num * percent)
        past_total_exp = total_exp


def setup(bot: commands.Bot) -> None:
    bot.add_cog(RankSystem(bot))
