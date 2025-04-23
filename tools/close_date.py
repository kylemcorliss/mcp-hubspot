
from datetime import datetime
from mcp_server_hubspot.hubspot_client import get_all_deals

def find_deals_with_past_close_date():
    today = datetime.utcnow()
    deals = get_all_deals(properties=["closedate"])
    past_due = []
    for d in deals:
        closedate = d["properties"].get("closedate")
        if closedate:
            try:
                cd = datetime.strptime(closedate, "%Y-%m-%dT%H:%M:%S.%fZ")
            except ValueError:
                cd = datetime.strptime(closedate, "%Y-%m-%dT%H:%M:%SZ")
            if cd < today:
                past_due.append({"id": d["id"], "closedate": closedate})
    return {"deals_with_past_close_date": past_due}

def check_close_date_health():
    # Basic heuristic: add 30 days per stage past CreateDate and compare to CloseDate
    stage_durations = {
        "appointmentscheduled": 10,
        "qualifiedtobuy": 15,
        "presentation": 20,
        "decisionmakerboughtin": 25,
        "contractsent": 30
    }
    unhealthy = []
    today = datetime.utcnow()
    deals = get_all_deals(properties=["dealstage", "closedate", "createdate"])
    for d in deals:
        stage = d["properties"].get("dealstage", "")
        createdate = d["properties"].get("createdate")
        closedate = d["properties"].get("closedate")
        try:
            created = datetime.strptime(createdate, "%Y-%m-%dT%H:%M:%S.%fZ")
            close = datetime.strptime(closedate, "%Y-%m-%dT%H:%M:%S.%fZ")
        except:
            continue
        extra_days = stage_durations.get(stage, 15)
        ideal_close = created + timedelta(days=extra_days)
        if close < ideal_close:
            unhealthy.append({
                "id": d["id"],
                "stage": stage,
                "createdate": createdate,
                "closedate": closedate,
                "ideal_min_close_date": ideal_close.isoformat()
            })
    return {"close_date_health_issues": unhealthy}
