import sys
import os
import logging
from fastapi import FastAPI
from dotenv import load_dotenv

# Ensure root path is in sys.path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

# Now safe to import local modules
from tools.router import router as analytics_router

# Load environment variables
load_dotenv()

# Initialize logger
logger = logging.getLogger("mcp_hubspot_server")
logging.basicConfig(level=logging.INFO)

# Create FastAPI app
app = FastAPI(
    title="HubSpot MCP Server",
    description="A modular FastAPI server to analyze HubSpot CRM data",
    version="1.0.0"
)

# Include analytics router
app.include_router(analytics_router)

# Health check endpoint
@app.get("/")
def root():
    return {"message": "HubSpot MCP Server is up and running!"}
