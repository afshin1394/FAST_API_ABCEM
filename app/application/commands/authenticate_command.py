# application/commands.py
from pydantic import BaseModel

from app.application.shared.command import Command


class AuthenticateCommand(Command):
    msisdn: str


