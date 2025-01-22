from typing import Sequence, List

from pydantic import BaseModel
from datetime import datetime

class SpeedTestServerDomain(BaseModel):
    server_id: str
    sponsor: str
    name: str
    country: str
    lat: str
    lon: str
    url: str
    host:str
    distance:int
    cc:str

   # Ensure the data type is consistent
    @staticmethod
    def validate_list(data: Sequence) -> List:
        return list(data)