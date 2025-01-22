from abcem.app.application.mediator import Mediator
from abcem.app.application.usecase.create_user_usecase import CreateUserUseCase
from abcem.app.application.usecase.speed_test_server_list_usecase import SpeedTestServerListUseCase
from abcem.app.domain.repositories.speed_test_repository import SpeedTestRepository
from fastapi import Depends

from abcem.app.infrastructure.di.mediator import get_mediator
from abcem.app.infrastructure.di.repositories import get_speed_test_repository


async def get_speed_test_use_case(
    speed_test_repository: SpeedTestRepository = Depends(get_speed_test_repository),
) -> SpeedTestServerListUseCase:
    return SpeedTestServerListUseCase(repository=speed_test_repository)

async def get_create_user_use_case(
     mediator : Mediator = Depends(get_mediator),
) -> CreateUserUseCase:
    return CreateUserUseCase(mediator=mediator)