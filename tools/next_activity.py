
from mcp_server_hubspot.hubspot_client import get_all_deals

def check_active_deals_have_next_activity():
    deals = get_all_deals(properties=["dealstage", "hs_task_next_task_id"])
    no_next = [d["id"] for d in deals if d["properties"].get("dealstage") not in ["closedwon", "closedlost"]
               and not d["properties"].get("hs_task_next_task_id")]
    return {"active_deals_missing_next_activity": no_next}

def verify_next_activity_task_completed():
    # Placeholder: this would require task engagement checking
    return {"task_completion_check": "stub - needs engagement layer"}
