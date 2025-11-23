from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.conversational_module.chat_controller import cnv_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="My API",
        description="A production-ready Hitayu Backend System",
        version="1.0.0",
    )

    # Setup CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

app = create_app()


#adding different routers
app.include_router(cnv_router)



@app.get("/")
def read_root():
    return {"message": "Hitayu API is working"}