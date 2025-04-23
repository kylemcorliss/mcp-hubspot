
from mcp_server_hubspot.hubspot_client import get_all_deals

def find_deals_missing_value():
    deals = get_all_deals(properties=["amount", "dealstage"])
    missing = []
    value_expected_stages = {"appointmentscheduled", "qualifiedtobuy", "presentation", "decisionmakerboughtin", "contractsent"}
    for d in deals:
        stage = d["properties"].get("dealstage", "")
        amount = d["properties"].get("amount")
        if stage in value_expected_stages and (not amount or amount == "0"):
            missing.append({"id": d["id"], "stage": stage})
    return {"deals_missing_value": missing}

def find_tcv_discrepancies():
    deals = get_all_deals(properties=["amount", "hs_tcv"])
    discrepancies = []
    for d in deals:
        try:
            total = float(d["properties"].get("hs_tcv", "0"))
            amount = float(d["properties"].get("amount", "0"))
            if abs(total - amount) > 1:  # small threshold
                discrepancies.append({
                    "id": d["id"],
                    "amount": amount,
                    "hs_tcv": total
                })
        except:
            continue
    return {"tcv_discrepancies": discrepancies}
