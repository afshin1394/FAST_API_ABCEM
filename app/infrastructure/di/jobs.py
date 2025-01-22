from abcem.app.domain.repositories.speed_test_repository import SpeedTestRepository
from fastapi import Depends

from abcem.app.infrastructure.di.repositories import get_speed_test_repository


async def run_speed_test_job(speed_test_repository : SpeedTestRepository = Depends(get_speed_test_repository)):
    speed_test_crawler_and_update_db()
