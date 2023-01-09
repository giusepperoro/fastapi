from fastapi import FastAPI
from api import router
import uvicorn

app = FastAPI()

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        app="main:app",
        host='localhost',
        port=3000,
        reload=True
    )
