from pydantic import BaseModel
from typing import List, Dict


class SpeedTestServerResponse(BaseModel):
    server_id: str
    sponsor: str
    name: str
    country: str
    lat: str
    lon: str
    url: str
    host: str
    distance: int
    cc: str

    # Include other relevant fields as needed


# Since the keys are floats (distances), but JSON keys must be strings,
# it's better to represent the data as a list rather than a dict.
class ServersResponse(BaseModel):
    servers: List[SpeedTestServerResponse]

    class Config:
        json_schema_extra = {

            "example": {

                "url": "http://it3.speedtest.aruba.it:8080/speedtest/upload.php",
                "lat": "45.6983",
                "lon": "9.6773",
                "distance": 5343,
                "name": "Ponte San Pietro",
                "country": "Italy",
                "cc": "IT",
                "sponsor": "Aruba S.p.A.",
                "id": "40519",
                "preferred": 0,
                "https_functional": 1,
                "host": "it3.speedtest.aruba.it.prod.hosts.ooklaserver.net:8080",
            }
        }
