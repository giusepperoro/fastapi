from .api_v1 import basic
from fastapi.routing import APIRouter

router = APIRouter(prefix="/api/v1")
router.include_router(basic.router)
