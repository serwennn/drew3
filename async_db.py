import aiosqlite


def async_with_connection(func):

    async def wrapper(*args, **kwargs):

        connection = await aiosqlite.connect("database.db")
        try:
            result = await func(connection, *args, **kwargs)
            await connection.commit()
            return result
        
        finally:
            await connection.close()

    return wrapper

'''
There's how to use it

@async_with_connection
async def async_insert_value(connection):
    cursor = await connection.cursor()
    await cursor.execute(
        """ INSERT INTO user (id) VALUES (?) """, (34,)
    )

asyncio.run(async_insert_value())
'''