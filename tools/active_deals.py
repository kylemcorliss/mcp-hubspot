
from datetime import datetime
from mcp_server_hubspot.hubspot_client import get_all_deals

def calculate_time_in_pipeline():
    deals = get_all_deals(properties=["createdate"])
    now = datetime.utcnow()
    durations = []
    for d in deals:
        created = d["properties"].get("createdate")
        if not created:
            continue
        try:
            start = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            start = datetime.strptime(created, "%Y-%m-%dT%H:%M:%SZ")
        days_open = (now - start).days
        durations.append({"id": d["id"], "days_in_pipeline": days_open})
    return {"pipeline_duration_by_deal": durations}

def analyze_total_activity():
    # Placeholder: requires join with engagements
    return {"status": "stub - needs engagement integration"}
