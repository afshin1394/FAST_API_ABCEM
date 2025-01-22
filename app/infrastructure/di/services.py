import httpx
from fastapi import Depends

from abcem.app.domain.services.get_gis_service import GetGISService
from abcem.app.domain.services.get_ip_info_service import GetIpInfoService
from abcem.app.infrastructure.di.async_client import get_client
from abcem.app.infrastructure.repository_impl.get_gis_repository_impl import GetGISServiceImpl
from abcem.app.infrastructure.repository_impl.get_ip_info_repository_impl import GetIpInfoServiceImpl



#services
async def get_ip_info_service(client: httpx.AsyncClient = Depends(get_client)) -> GetIpInfoService:
    return GetIpInfoServiceImpl(client=client)


async def get_gis_service() -> GetGISService:
    return GetGISServiceImpl()