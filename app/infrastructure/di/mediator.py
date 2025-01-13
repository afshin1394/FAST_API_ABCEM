from fastapi import Depends

from app.application.commands.authenticate_command import AuthenticateCommand
from app.application.handlers.authenticate_command_handler import AuthenticateCommandHandler
from app.application.mediator import Mediator
from app.domain.services.get_ip_info_service import GetIpInfoService
from app.infrastructure.di.repositories import get_ip_info_service


def get_mediator(service: GetIpInfoService = Depends(get_ip_info_service)) -> Mediator:
    mediator = Mediator()
    # Register command handlers
    mediator.register_handler(AuthenticateCommand, AuthenticateCommandHandler(service).handle)
    # Register query handlers

    return mediator