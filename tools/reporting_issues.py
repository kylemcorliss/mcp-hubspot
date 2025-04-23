
from mcp_server_hubspot.hubspot_client import get_all_deals

def find_deals_missing_stage_history():
    deals = get_all_deals(properties=["hs_latest_stage_move_date", "dealstage"])
    missing = [d["id"] for d in deals if not d["properties"].get("hs_latest_stage_move_date")]
    return {"deals_missing_stage_history": missing}
