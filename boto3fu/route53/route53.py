from boto3fu.common import helpers

def resource_record(record):
    """
    """
    alias_target_zone_id = ''
    alias_target_dns_name = ''
    alias_target_evaluate_health = ''
    if record.get("AliasTarget"):
        alias_target_zone_id = record.get("AliasTarget")['HostedZoneId']
        alias_target_dns_name = record.get("AliasTarget")['DNSName']
        alias_target_evaluate_health = str(record.get("AliasTarget")['EvaluateTargetHealth'])

    return {
        "name": record.get("Name") or '',
        "type": record.get("Type") or '',
        "ttl": record.get("TTL"),
        "region": record.get("Region"),
        "failover": record.get("Failover") or '',
        "alias_target": '|'.join([i for i in [alias_target_zone_id, alias_target_dns_name, alias_target_evaluate_health]]),
        "resource_records": "|".join([i["Value"] for i in record.get("ResourceRecords") or []])

    }

def hosted_zone(record):
    """
    """
    return {
        "id": record.get("Id") or '',
        "name": record.get("Name") or '',
        "private_zone": record.get("Config")['PrivateZone'] or '',
        "rrset_count": record.get("ResourceRecordSetCount") or ''
    }

@helpers.add_account_alias
@helpers.add_account_num
@helpers.add_client_region
def get_route53_zones(c):
    """
    """
    client = c.GetClient()
    records = []
    paginator = client.get_paginator('list_hosted_zones')
    pages = paginator.paginate()
    for page in pages:
        for zone in page['HostedZones']:
            records.append(hosted_zone(zone))
    return records


def list_resource_recordsets(c, zone_id):
    """
    """
    client = c.GetClient()
    records = []
    paginator = client.get_paginator('list_resource_record_sets')
    pages = paginator.paginate(HostedZoneId=zone_id)
    for page in pages:
        for record in page['ResourceRecordSets']:
            records.append(resource_record(record))
    return records

def get_zones(c, zone_names):
    """
    """
    client = c.GetClient()
    zones = []
    paginator = client.get_paginator('list_hosted_zones')
    pages = paginator.paginate()
    for page in pages:
        for zone in page['HostedZones']:
            if not zone_names:
                zones.append(hosted_zone(zone))
            else:
                if zone['Name'] in zone_names:
                    zones.append(hosted_zone(zone))
    return zones


@helpers.add_account_alias
@helpers.add_account_num
@helpers.add_client_region
def get_resource_records(c, zone_names):
    """
    """

    client = c.GetClient()
    # make sure domain name ends with .
    _zone_names = []
    for i, name in enumerate(zone_names):
        if not name.endswith("."):
            name = name + '.'
    
        _zone_names.append(name)

    records = []
    zones = get_zones(client, _zone_names)
    for zone in zones:
        zone_records = list_resource_recordsets(client, zone['id'])
        for i in zone_records:
            i.update({"zone_id": zone['id'], "zone_name": zone['name']})
        records.extend(zone_records)
    return records
