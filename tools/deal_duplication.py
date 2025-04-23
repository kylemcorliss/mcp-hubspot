
from mcp_server_hubspot.hubspot_client import get_all_deals

def identify_deal_duplicates_across_pipelines():
    deals = get_all_deals(properties=["dealname", "pipeline"])
    seen = {}
    duplicates = []
    for d in deals:
        name = d["properties"].get("dealname", "").strip().lower()
        pipeline = d["properties"].get("pipeline")
        if name in seen:
            if seen[name] != pipeline:
                duplicates.append({"id": d["id"], "name": name, "pipeline": pipeline})
        else:
            seen[name] = pipeline
    return {"duplicates_across_pipelines": duplicates}
