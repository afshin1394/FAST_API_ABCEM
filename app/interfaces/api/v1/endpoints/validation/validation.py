from fastapi import APIRouter,Depends,HTTPException

from abcem.app.infrastructure.di.controllers import authentication_controller
from abcem.app.infrastructure.di.speed_test import get_speed_test
from abcem.app.infrastructure.services_impl.speed_test_servers import Speedtest, SpeedtestException
from abcem.app.interfaces.controllers.authentication_controller import AuthenticationController
from abcem.app.interfaces.dto.response.server_response import ServersResponse

router_v1 = APIRouter(
    prefix="/validation",
)


@router_v1.get("/servers", response_model=ServersResponse)
async def get_servers(speed_test: Speedtest = Depends(get_speed_test)) -> ServersResponse:
    try:
        servers_dict = speed_test.get_servers()
    except SpeedtestException as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Flatten the dictionary into a list of servers
    servers_list = []
    for server_group in servers_dict.values():
        servers_list.extend(server_group)

    # Validate and create Server instances
    try:
        validated_servers = [Server(**server) for server in servers_list]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Data validation error: {e}")

    return ServersResponse(servers=validated_servers)
@router_v1.get("/validateIp")
async def get_ip_info_v1(controller: AuthenticationController = Depends(authentication_controller)):
    pass
    # try:
    #     ip_info = await controller.authenticate(authenticate_request= AuthenticationRequest())
    #     return ip_info
    # except httpx.HTTPStatusError as e:
    #     # Handle specific HTTP errors
    #     raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
    # except httpx.RequestError as e:
    #     # Handle network-related errors
    #     raise HTTPException(status_code=500, detail=str(e))
    # except Exception as e:
    #     # Handle any other unexpected errors
    #     raise HTTPException(status_code=500, detail=str(e))
#implement in other service

@router_v1.post("/validateLocation")
async def validate_location():
  pass

