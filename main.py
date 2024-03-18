# Vanilla Python boilerplate script to connect to Neo4j
# This can be used as a quick starting point for developping apps using the Neo4j Driver
# It shows both synchronous and asynchronous usage of the driver
# Based on your needs, remove the one you don't need

import asyncio # Remove this if you don't need async
from config.config_loader import URI, USERNAME, PASSWORD
from utils.neo4j_connection_sync import Neo4jConnectionSync
from utils.neo4j_connection_async import Neo4jConnectionAsync

async def main():
    query = "MATCH (n) RETURN n LIMIT 5"

    # Synchronous driver
    conn_sync = Neo4jConnectionSync(URI, USERNAME, PASSWORD)
    conn_sync.connect() # instanciate the driver
    results_sync = conn_sync.execute_query(query)
    for record in results_sync:
        print("Sync result:", record)
    conn_sync.close()

    # Asynchronous driver
    conn_async = Neo4jConnectionAsync(URI, USERNAME, PASSWORD)
    await conn_async.connect() # instanciate the driver
    results_async = await conn_async.execute_query(query)
    for record in results_async:
        print("Async result:", record)
    await conn_async.close()

if __name__ == "__main__":
    asyncio.run(main())
