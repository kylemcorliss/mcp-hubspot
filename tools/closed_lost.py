
from mcp_server_hubspot.hubspot_client import get_all_deals

def summarize_closed_lost_reasons():
    deals = get_all_deals(properties=["dealstage", "closed_lost_reason"])
    reasons = {}
    for d in deals:
        if d["properties"].get("dealstage") != "closedlost":
            continue
        reason = d["properties"].get("closed_lost_reason", "None")
        reasons.setdefault(reason, 0)
        reasons[reason] += 1
    return {"closed_lost_reasons": reasons}

def summarize_closed_lost_themes():
    # Placeholder for text clustering or theme extraction from reasons
    return {"themes": "stub - clustering needed"}

def get_next_activity_info():
    deals = get_all_deals(properties=["dealstage", "hs_task_next_task_id"])
    return [{"id": d["id"], "next_task": d["properties"].get("hs_task_next_task_id")} for d in deals]

def get_next_activity_notes():
    # Placeholder - requires pulling associated notes from engagements
    return {"next_activity_notes": "stub - needs engagement enrichment"}

def identify_inactive_closed_lost():
    deals = get_all_deals(properties=["dealstage", "hs_lastmodifieddate"])
    return [d["id"] for d in deals if d["properties"].get("dealstage") == "closedlost"]
