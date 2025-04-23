
from mcp_server_hubspot.hubspot_client import get_all_deals

def analyze_contact_cadence():
    deals = get_all_deals(properties=["num_contacted_notes", "dealstage"])
    cadence_by_stage = {}
    for d in deals:
        stage = d["properties"].get("dealstage", "unknown")
        contacts = int(d["properties"].get("num_contacted_notes", "0"))
        if stage not in cadence_by_stage:
            cadence_by_stage[stage] = {"count": 0, "contacts": 0}
        cadence_by_stage[stage]["count"] += 1
        cadence_by_stage[stage]["contacts"] += contacts

    return {
        "cadence_by_stage": {
            stage: {
                "avg_contacts": round(data["contacts"] / data["count"], 2) if data["count"] > 0 else 0
            }
            for stage, data in cadence_by_stage.items()
        }
    }
