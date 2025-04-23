
from mcp_server_hubspot.hubspot_client import get_all_deals

def analyze_field_completeness():
    fields = ["department", "industry", "metrics", "economic_buyer", "decision_criteria", "decision_process", "identify_pain", "champion"]
    deals = get_all_deals(properties=fields)
    field_counts = {field: 0 for field in fields}
    total = len(deals)

    for d in deals:
        for field in fields:
            if d["properties"].get(field):
                field_counts[field] += 1

    return {
        "field_completeness": {
            field: f"{count}/{total} ({round((count/total)*100, 1)}%)"
            for field, count in field_counts.items()
        }
    }

def detect_unused_fields():
    # Placeholder – would require full schema access from HubSpot API
    return {"unused_fields": "stub - would compare schema to population"}
