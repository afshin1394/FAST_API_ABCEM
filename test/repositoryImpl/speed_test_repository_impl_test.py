import pytest
from unittest.mock import AsyncMock
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert
from abcem.app.infrastructure.schemas.speed_test_servers_table import SpeedTestServerTable
from abcem.app.domain.entities.speed_test_server_domain import SpeedTestServerDomain
from abcem.app.infrastructure.repository_impl.speed_test_repository_impl import SpeedTestRepositoryImpl
from datetime import datetime

@pytest.mark.asyncio
async def test_upsert_servers():
    # Mock database session
    mock_db = AsyncMock(spec=AsyncSession)
    # Create mock data for servers
    servers = [
        SpeedTestServerDomain(

            id=1,
            sponsor="Sponsor A",
            name="Server A",
            country="Country A",
            lat=12.34,
            lon=56.78,
            host="hostA.com",
            last_updated=     datetime.fromisoformat("2025-01-01T00:00:00")
        ),
        SpeedTestServerDomain(
            id=2,
            sponsor="Sponsor B",
            name="Server B",
            country="Country B",
            lat=23.45,
            lon=67.89,
            host="hostB.com",
            last_updated=     datetime.fromisoformat("2025-01-02T00:00:00")
        ),
    ]

    # Initialize repository
    repository = SpeedTestRepositoryImpl(mock_db)

    # Call the method under test
    await repository.upsert_servers(servers)

    # Prepare expected SQL statement
    expected_values = [server.model_dump() for server in servers]
    stmt = insert(SpeedTestServerTable).values(expected_values)
    stmt = stmt.on_conflict_do_update(
        index_elements=["server_id"],
        set_={
            "sponsor": stmt.excluded.sponsor,
            "name": stmt.excluded.name,
            "country": stmt.excluded.country,
            "lat": stmt.excluded.lat,
            "lon": stmt.excluded.lon,
            "host": stmt.excluded.host,
            "last_updated": stmt.excluded.last_updated,
        },
    )

    # Assert that the expected SQL statement was executed
    # mock_db.execute.assert_called_once_with(stmt)

    # # Assert that the transaction was committed
    # mock_db.commit.assert_called_once()
