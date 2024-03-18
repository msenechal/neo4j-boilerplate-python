# Neo4j Connection Class using the Sync Driver
# Remove this file if you will use the Async Driver

from neo4j import GraphDatabase, basic_auth

class Neo4jConnectionSync:
    """
    Neo4j Connection Class for handling database operations synchronously.
    """

    def __init__(self, uri, user, password):
        self.__uri = uri
        self.__user = user
        self.__password = password
        self.__driver = None

    def connect(self):
        if not self.__driver:
            self.__driver = GraphDatabase.driver(
                self.__uri,
                auth=basic_auth(self.__user, self.__password)
            )
            print("Connected to the database (Sync).")

    def close(self):
        if self.__driver:
            self.__driver.close()
            print("Connection closed (Sync).")

    def execute_query(self, query, parameters=None):
        with self.__driver.session() as session:
            result = session.run(query, parameters)
            return [record["n"] for record in result]
