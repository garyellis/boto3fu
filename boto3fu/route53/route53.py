import os.path
from boto3fu.common import helpers

def resource_record(record):
    """
    """
    alias_target = ''
    if record.get("AliasTarget"):
        alias_target_dns_name = record.get("AliasTarget")['DNSName'] or None
        alias_target_evaluate_health = str(record.get("AliasTarget")['EvaluateTargetHealth']) or None
        alias_target = '|'.join([i for i in [alias_target_dns_name, alias_target_evaluate_health] if i])

    resource_records = ''
    if record.get("ResourceRecords"):
        resource_records = "|".join([i["Value"] for i in record.get("ResourceRecords") if i])

    return {
        "name": record.get("Name") or '',
        "type": record.get("Type") or '',
        "ttl": record.get("TTL"),
        "alias_target": alias_target,
        "resource_records": resource_records,
        "region": record.get("Region"),
        "failover": record.get("Failover") or '',
        "multivalueanswer": record.get("MultiValueAnswer") or '',
        "healthcheck_id": record.get("HealthCheckId") or '',
        "traffic_policy_instance_id": record.get("TrafficPolicyInstanceId") or ''
    }

def hosted_zone(record):
    """
    """
    return {
        "id": record.get("Id") or '',
        "name": record.get("Name") or '',
        "private_zone": record.get("Config")['PrivateZone'],
        "rrset_count": record.get("ResourceRecordSetCount") or ''
    }

@helpers.add_account_alias
@helpers.add_account_num
@helpers.add_client_region
def get_route53_zones(c, zone_type):
    """
    """

    records = get_zones(c, [], zone_type)
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

def get_zones(c, zone_names, zone_type):
    """
    """
    client = c.GetClient()
    zones = []
    paginator = client.get_paginator('list_hosted_zones')
    pages = paginator.paginate()
    for page in pages:
        for zone in page['HostedZones']:
            # apply zone type filters
            if zone_type == 'public' and zone.get("Config")['PrivateZone']:
                continue
            if zone_type == 'private' and not zone.get("Config")['PrivateZone']:
                continue
            
            # apply the name filter
            if zone['Name'] in zone_names or not zone_names:
                zones.append(hosted_zone(zone))

    return zones


@helpers.add_account_alias
@helpers.add_account_num
@helpers.add_client_region
def get_resource_records(c, zone_names, zone_type):
    """
    """

    # make sure domain name ends with .
    _zone_names = []
    for i, name in enumerate(zone_names):
        if not name.endswith("."):
            name = name + '.'
    
        _zone_names.append(name)

    records = []
    zones = get_zones(c, _zone_names, zone_type)
    for zone in zones:
        zone_name = zone['name']
        zone_records = list_resource_recordsets(c, zone['id'])
        for i in zone_records:

            # extract the zone id only
            zone_id = os.path.basename(zone['id'])

            # move the zone apex record to a decorator?
            apex_alias = 'false'
            if i['type'] == 'A' and i["name"] == zone_name:
                apex_alias = 'true'

            i.update({"zone_id": zone_id, "zone_name": zone_name, "private_zone": zone['private_zone'], 'apex_alias': apex_alias})
        records.extend(zone_records)
    return records
