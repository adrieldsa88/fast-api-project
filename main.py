from fastapi import FastAPI

app = FastAPI()

from routes.auth_routes import auth_router
from routes.order_routes import order_router