from fastapi import FastAPI
from app.api.v1.routes import router

app = FastAPI()

# Register routes under /api/v1
app.include_router(router, prefix="/api/v1/pokemon", tags=["Pokemon"])
