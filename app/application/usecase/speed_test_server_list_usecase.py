from typing import Any, List

from abcem.app.application.usecase.base_use_case import BaseUseCase
from abcem.app.domain.entities.speed_test_server_domain import SpeedTestServerDomain
from abcem.app.domain.repositories.speed_test_repository import SpeedTestRepository
from abcem.app.infrastructure.services_impl.speed_test_crawler import SpeedTestServerCrawler


class SpeedTestServerListUseCase(BaseUseCase):

    def __init__(self,repository: SpeedTestRepository):
        self.repository = repository

    async def execute(self, **kwargs) -> List[SpeedTestServerDomain]:
        # Initialize the crawler with concurrency = 10 and max retries = 3
        concurrency = int(kwargs.get("concurrency", "Key not found"))
        retries = int(kwargs.get("retries", "Key not found"))
        # Start the crawler and get the results
        crawler = SpeedTestServerCrawler(t=concurrency, r=retries)
        servers = await crawler.run()

        print(servers)
        await self.repository.upsert_servers(servers=servers)

        return servers
        # Update the database
