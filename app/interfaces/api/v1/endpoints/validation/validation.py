import httpx
from fastapi import APIRouter, Depends



from app.infrastructure.di.controllers import authentication_controller
from app.interfaces.controllers.authentication_controller import AuthenticationController

router_v1 = APIRouter(
    prefix="/validation",
)

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

