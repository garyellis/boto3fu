import logging

from boto3fu.connection_manager import client_aggregator
import boto3fu.list.eips
from boto3fu import outputs


logger = logging.getLogger(__name__)


def get_eips(profile, region, output_format='table'):
    """
    """
    if not profile:
        profile = [None]
    if not region:
        region = [None]

    clients = client_aggregator(profile, region, 'ec2')
    eips = []
    for c in clients:
        eips.extend(boto3fu.list.eips.get_eips(c))

    outputs.output(eips, output_format)
