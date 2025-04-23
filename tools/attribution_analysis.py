
from mcp_server_hubspot.hubspot_client import get_all_deals

def summarize_deal_sources():
    deals = get_all_deals(properties=["deal_source"])
    summary = {}
    for d in deals:
        source = d["properties"].get("deal_source", "Unknown")
        summary.setdefault(source, 0)
        summary[source] += 1
    return {"deal_sources": summary}

def evaluate_primary_secondary_source_fields():
    deals = get_all_deals(properties=["deal_source", "secondary_source"])
    fields_used = {
        "primary_filled": sum(1 for d in deals if d["properties"].get("deal_source")),
        "secondary_filled": sum(1 for d in deals if d["properties"].get("secondary_source"))
    }
    return {"source_field_usage": fields_used}
