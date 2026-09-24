from fastapi import FastAPI
from routes.student_routes import router


app = FastAPI(
    title="Student CRUD API",
    description="FastAPI Student CRUD Application",
    version="1.0.0"
)


app.include_router(router)