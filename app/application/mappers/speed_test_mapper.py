from typing import List , Sequence
from abcem.app.infrastructure.schemas.speed_test_servers_table import SpeedTestServerTable  # Infrastructure model
from abcem.app.domain.entities.speed_test_server_domain  import SpeedTestServerDomain  # Domain model

def to_domain(model: SpeedTestServerTable) -> SpeedTestServerDomain:
    return SpeedTestServerDomain(
        server_id=model.server_id,
        url=model.url,
        distance=model.distance,
        sponsor=model.sponsor,
        name=model.name,
        country=model.country,
        lat=model.lat,
        lon=model.lon,
        host=model.host,
        cc=model.cc,
    )

def to_domain_list(models: Sequence[SpeedTestServerTable]) -> List[SpeedTestServerDomain]:
    return [to_domain(model) for model in models]

def from_domain(domain: SpeedTestServerDomain) -> SpeedTestServerTable:
    return SpeedTestServerTable(
        server_id=domain.server_id,
        url=domain.url,
        distance=domain.distance,
        sponsor=domain.sponsor,
        name=domain.name,
        country=domain.country,
        lat=domain.lat,
        lon=domain.lon,
        host=domain.host,
        last_updated=domain.last_updated,
    )
def from_domain_list(domains: List[SpeedTestServerDomain]) -> List[SpeedTestServerTable]:
    return [from_domain(domain) for domain in domains]