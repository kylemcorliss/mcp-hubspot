
from mcp_server_hubspot.hubspot_client import get_all_deals

def filter_deals_by_pipeline(pipeline_id):
    deals = get_all_deals(properties=["pipeline", "dealname"])
    filtered = [d for d in deals if d["properties"].get("pipeline") == pipeline_id]
    return {"filtered_deals": [{"id": d["id"], "name": d["properties"].get("dealname")} for d in filtered]}
