from fastapi import APIRouter, Depends, HTTPException

from app.infrastructure.di.controllers import authentication_controller
from app.interfaces.controllers.authentication_controller import AuthenticationController
from app.interfaces.dto.request.authenticate_request import AuthenticateRequest
from app.interfaces.dto.response.authenticate_response import AuthenticateResponse

# Router for API version 1
router_v1 = APIRouter(
    prefix="/authentication",
)


@router_v1.post("/authenticate", response_model=AuthenticateResponse)
async def login_v1(authenticate_request: AuthenticateRequest,
             authenticate_controller: AuthenticationController = Depends(authentication_controller)):
    try:
        return await authenticate_controller.authenticate(authenticate_request)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router_v1.get("/verify")
def verify_v1():
    return [{"verify": "true"}]
