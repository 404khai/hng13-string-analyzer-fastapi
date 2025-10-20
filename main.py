from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models, database
from app.routes import stringRoutes

models.Base.metadata.create_all(bind=database.engine)

# Initialize FastAPI app
app = FastAPI(title="String Analyzer Service", docs_url="/docs", redoc_url="/redoc", openapi_url="/openapi.json")

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "*",
    # add others if needed, e.g. deployed URLs
]

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routes
app.include_router(stringRoutes.router)



# Root endpoint
@app.get("/")
def home():
    return {"message": "HNG13 String Analyzer Service Task | Stage 1"}