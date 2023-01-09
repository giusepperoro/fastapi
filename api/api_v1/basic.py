from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from schemas import Model, ModelOut
from fastapi import status

router = APIRouter(prefix="/basic")


@router.get("/hello")
async def say_hello():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "Hello",
            "version": 1
        }
    )


@router.post("/lol", response_model=ModelOut)
async def lol(model: Model):
    return ModelOut(full=f"{model.mol} {model.lom}")
