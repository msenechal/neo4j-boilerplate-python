import pytest
from utils.neo4j_connection_async import Neo4jConnectionAsync
from neo4j import AsyncGraphDatabase

class TestMain:

    # Connects to Neo4j with Async Driver
    @pytest.mark.asyncio
    async def test_connect_when_driver_not_set(self, mocker):

        uri = "bolt://localhost:7687"
        user = "neo4j"
        password = "password"
        connection = Neo4jConnectionAsync(uri, user, password)

        mocker.patch('neo4j.AsyncGraphDatabase.driver')

        await connection.connect()

        assert connection._Neo4jConnectionAsync__driver is not None
        assert AsyncGraphDatabase.driver.called