import logging

from boto3fu.connection_manager import client_aggregator
from boto3fu.vpc import eips
from boto3fu import outputs



logger = logging.getLogger(__name__)


def get_eips(profile, region, boto_client_params, output_format='table'):
    """
    """
    if not profile:
        profile = [None]
    if not region:
        region = [None]

    clients = client_aggregator(profile, region, 'ec2', boto_client_params)
    records = []
    for c in clients:
        records.extend(eips.get_eips(c))

    outputs.output(records, output_format)