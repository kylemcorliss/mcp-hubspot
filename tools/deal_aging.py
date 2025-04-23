
from datetime import datetime
from mcp_server_hubspot.hubspot_client import get_all_deals

def get_deal_aging_by_profile_and_owner():
    today = datetime.utcnow()
    buckets = {
        "<7d": {}, "7–30d": {}, "30–90d": {}, "90d+": {}, "Unknown": {}
    }
    deals = get_all_deals(properties=["hs_lastcontacteddate", "hubspot_owner_id"])

    for deal in deals:
        owner = deal["properties"].get("hubspot_owner_id", "unknown")
        last_contact = deal["properties"].get("hs_lastcontacteddate")
        if not last_contact:
            buckets["Unknown"].setdefault(owner, 0)
            buckets["Unknown"][owner] += 1
            continue
        try:
            contact_date = datetime.strptime(last_contact, "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            contact_date = datetime.strptime(last_contact, "%Y-%m-%dT%H:%M:%SZ")
        days = (today - contact_date).days
        if days < 7:
            bucket = "<7d"
        elif days < 30:
            bucket = "7–30d"
        elif days < 90:
            bucket = "30–90d"
        else:
            bucket = "90d+"
        buckets[bucket].setdefault(owner, 0)
        buckets[bucket][owner] += 1
    return {"deal_aging_by_owner": buckets}
