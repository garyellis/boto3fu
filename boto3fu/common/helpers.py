from functools import wraps
import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

def add_account_alias(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        account_alias = get_aws_account_alias()
        records = f(*args, **kwargs)
        # for i, row in enumerate([r['user'] for r in records]):
        for i, row in enumerate(records):
            records[i].update({'account_alias': account_alias})
        return records
    return wrapped

def add_account_num(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        account = get_aws_account()
        records = [dict(item, **{'account_number': account}) for item in f(*args, **kwargs)]
        return records
    return wrapped


def add_client_region(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        client = args[0]
        region = client.meta.region_name
        records = [dict(item, **{'region': region}) for item in f(*args, **kwargs)]
        return records
    return wrapped


def get_aws_account_alias():
    """
    """
    try:
        account_alias = "n/a"
        logger.debug('Getting account alias')
        iam = boto3.client('iam')
        paginator = iam.get_paginator('list_account_aliases')
        for response in paginator.paginate():
            account_alias = response['AccountAliases'][0]
        return account_alias

    except ClientError as err:
        logger.error(err)
        
def get_aws_account():
    """
    """
    try:
        logger.debug('Get caller identity')
        sts_client = boto3.client('sts')
        account_id = sts_client.get_caller_identity().get('Account')
        logger.debug('Account: {}'.format(account_id))
        return account_id

    except ClientError as err:
        logger.error(err)


def get_tag_value(tags, key='Name'):
    """
    tags helper
    """
    value = ''
    if tags:
        for tag in tags:
            if key == tag['Key']:
                value = tag['Value']
    return value
