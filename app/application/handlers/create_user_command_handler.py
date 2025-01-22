import uuid
from typing import Optional

from abcem.app.application.commands.create_user_command import CreateUserCommand
from abcem.app.application.shared.command_handler import CommandHandler, C, E
from abcem.app.domain.entities.users_domain import UserDomain
from abcem.app.domain.events.user_created_event import UserCreatedEvent
from abcem.app.domain.repositories.users_repository import UsersRepository


class CreateUserCommandHandler(CommandHandler):
    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository

    async def handle(self, command: CreateUserCommand) -> UserCreatedEvent:
        await self.user_repository.save(UserDomain(name=command.name,age= command.age,gender=command.gender))


    async def deserialize_command(self, json_str: str) -> C:
        pass