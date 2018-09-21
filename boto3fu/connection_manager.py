import boto3


def get_session(profile_name=None, region_name=None):
    """
    """
    args = {}
    if profile_name:
        args.update({"profile_name": profile_name})
    if region_name:
        args.update({"region_name": region_name})

    session = boto3.session.Session(**args)

    return session


def get_client(profile_name, region_name, svc, boto_client_params={}):
    """
    Sets up the boto session and client
    """
    session = get_session(profile_name, region_name)
    client = session.client(svc, **boto_client_params)
    return client


def client_aggregator(profiles, regions, svc, boto_client_params):
    """
    Returns a list of boto3 clients from the input list
    """
    if 'all' in regions:
        regions = ['us-west-1', 'us-west-2', 'us-east-1', 'us-east-2']

    clients = [
        get_client(p, r, 'ec2', boto_client_params)
        for p in profiles
        for r in regions
    ]
    return clients
