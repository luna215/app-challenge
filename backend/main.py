from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from routes import router


app = FastAPI(
    title="Infersoft Slim Version", 
    version="0.1.0",
    dependencies=[]
)


origins = [
    "http://localhost:3000",
    "http://0.0.0.0:8000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router, prefix='/documents', tags=["Documents"])


@app.get("/")
def read_root():
    return {"Hello": "World"}