# Neo4j Connection Class using the Async Driver
# Remove this file if you will use the Sync Driver

from neo4j import AsyncGraphDatabase, basic_auth

class Neo4jConnectionAsync: 
    """
    Neo4j Connection Class for handling database operations asynchronously.
    """

    def __init__(self, uri, user, password):
        self.__uri = uri
        self.__user = user
        self.__password = password
        self.__driver = None

    async def connect(self):
        if not self.__driver:
            self.__driver = AsyncGraphDatabase.driver(
                self.__uri,
                auth=basic_auth(self.__user, self.__password)
            )
            print("Connected to the database (Async).")

    async def close(self):
        if self.__driver:
            await self.__driver.close()
            print("Connection closed (Async).")

    async def execute_query(self, query, parameters=None):
        async with self.__driver.session() as session:
            result = await session.run(query, parameters)
            return [record["n"] async for record in result]
