import logging

from boto3fu.connection_manager import client_aggregator
#import boto3fu.list.route53
from boto3fu.route53 import route53
from boto3fu import outputs


logger = logging.getLogger(__name__)


def get_route53_zones(profile, region, boto_client_params, zone_type, output_format='table'):
    """
    """
    if not profile:
        profile = [None]
    if not region:
        region = [None]

    clients = client_aggregator(profile, region, 'route53', boto_client_params)
    zones = []
    for c in clients:
        zones.extend(route53.get_route53_zones(c, zone_type))
    outputs.output(zones, output_format)

def get_route53_resource_records(profile, region, boto_client_params, zone_type, output_format='table', zone_names=[], r53_policy_type=[], record_type=[]):
    """
    """
    if not profile:
        profile = [None]
    if not region:
        region = [None]

    clients = client_aggregator(profile, region, 'route53', boto_client_params)
    records = []
    for c in clients:
        records.extend(route53.get_resource_records(c, zone_names, zone_type, r53_policy_type, record_type))
    outputs.output(records, output_format)