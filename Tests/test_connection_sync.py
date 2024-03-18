from neo4j import GraphDatabase
from utils.neo4j_connection_sync import Neo4jConnectionSync

class TestMain:

    # Connects to Neo4j with Sync Driver
    def test_connect_when_driver_not_set(self, mocker):

        uri = "bolt://localhost:7687"
        user = "neo4j"
        password = "password"
        connection = Neo4jConnectionSync(uri, user, password)

        mocker.patch('neo4j.GraphDatabase.driver')

        connection.connect()

        assert connection._Neo4jConnectionSync__driver is not None
        assert GraphDatabase.driver.called