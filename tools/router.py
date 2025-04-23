
from fastapi import APIRouter
from mcp_server_hubspot.hubspot_client import get_all_deals
import os
import httpx

router = APIRouter()

@router.get("/health/hubspot")
async def hubspot_health():
    access_token = os.getenv("HUBSPOT_ACCESS_TOKEN")
    if not access_token:
        return {"status": "error", "detail": "No HUBSPOT_ACCESS_TOKEN found in .env"}
    
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    async with httpx.AsyncClient() as client:
        resp = await client.get("https://api.hubapi.com/integrations/v1/me", headers=headers)
    
    if resp.status_code == 200:
        data = resp.json()
        return {
            "status": "ok",
            "hubspot_user_id": data.get("user_id"),
            "hubspot_scopes": data.get("scopes"),
        }
    else:
        return {"status": "error", "code": resp.status_code, "message": resp.text}
