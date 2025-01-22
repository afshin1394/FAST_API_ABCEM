from fastapi import Depends

from abcem.app.application.commands.authenticate_command import AuthenticateCommand
from abcem.app.application.commands.create_user_command import CreateUserCommand
from abcem.app.application.handlers.authenticate_command_handler import AuthenticateCommandHandler
from abcem.app.application.handlers.create_user_command_handler import CreateUserCommandHandler
from abcem.app.application.mediator import Mediator
from abcem.app.domain.repositories.users_repository import UsersRepository
from abcem.app.domain.services.get_ip_info_service import GetIpInfoService
from abcem.app.infrastructure.di.repositories import  get_users_repository
from abcem.app.infrastructure.di.services import get_ip_info_service


def get_mediator(get_ip_info_service : GetIpInfoService = Depends(get_ip_info_service),users_repository : UsersRepository = Depends(get_users_repository)) -> Mediator:
    mediator = Mediator()
    # Register command handlers
    mediator.register_handler(AuthenticateCommand, AuthenticateCommandHandler(get_ip_info_service).handle)
    # Register query handlers
    mediator.register_handler(CreateUserCommand, CreateUserCommandHandler(users_repository).handle)

    return mediator