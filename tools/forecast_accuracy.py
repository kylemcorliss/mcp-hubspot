
from mcp_server_hubspot.hubspot_client import get_all_deals

def evaluate_pipeline_forecast_accuracy():
    deals = get_all_deals(properties=["dealstage"])
    stage_counts = {}
    closed_count = 0
    for d in deals:
        stage = d["properties"].get("dealstage")
        stage_counts.setdefault(stage, 0)
        stage_counts[stage] += 1
        if stage == "closedwon":
            closed_count += 1
    return {
        "total_closed_won": closed_count,
        "stage_counts": stage_counts
    }

def compare_deal_weighting_to_outcomes():
    # Placeholder for weighting logic — would require config of expected %
    return {"weighting_check": "stub"}
