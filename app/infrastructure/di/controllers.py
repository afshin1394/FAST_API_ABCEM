from fastapi import Depends

from app.application.mediator import Mediator
from app.infrastructure.di.mediator import get_mediator
from app.interfaces.controllers.authentication_controller import AuthenticationController


async def authentication_controller(mediator: Mediator = Depends(get_mediator)) -> AuthenticationController:
    return AuthenticationController(mediator = mediator)



