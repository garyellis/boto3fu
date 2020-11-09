from functools import wraps
import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

def add_account_alias(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        c = args[0]
        account_alias = get_aws_account_alias(c)

        records = f(*args, **kwargs)
        for i, row in enumerate(records):
            records[i].update({'account_alias': account_alias})
        return records
    return wrapped

def add_account_num(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        c = args[0]
        account = get_aws_account(c)
        records = [dict(item, **{'account_number': account}) for item in f(*args, **kwargs)]
        return records
    return wrapped


def add_client_region(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        c = args[0]
        client = c.GetClient()
        region = client.meta.region_name
        records = [dict(item, **{'region': region}) for item in f(*args, **kwargs)]
        return records
    return wrapped


def get_aws_account_alias(c):
    """
    """
    try:
        account_alias = "n/a"
        logger.debug('Getting account alias')
        client = c.GetClient(svc='iam')
        paginator = client.get_paginator('list_account_aliases')
        for response in paginator.paginate():
            account_alias = response['AccountAliases'][0]
        return account_alias

    except ClientError as err:
        logger.error(err)
        
def get_aws_account(c):
    """
    """
    try:
        logger.debug('Get caller identity')
        client = c.GetClient(svc='sts')
        account_id = client.get_caller_identity().get('Account')
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
