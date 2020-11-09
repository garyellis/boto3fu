import boto3


class Client(object):
    def __init__(self, svc=None, profile_name=None, region_name=None, boto_client_params={}):
        self.profile_name = profile_name
        self.region_name = region_name
        self.svc = svc
        self.boto_client_params = boto_client_params
        self.client = None
        self.session = None

        self.SetSession()

    def SetSession(self):
        """
        """
        args = {}
        if self.profile_name:
            args.update({"profile_name": self.profile_name})
        if self.region_name:
            args.update({"region_name": self.region_name})
        session = boto3.session.Session(**args)
        self.session = session
    
    def SetClient(self, svc=None):
        if svc:
            client = self.session.client(svc, **self.boto_client_params)
            self.client = client
        else:
            if self.svc:
                client = self.session.client(self.svc, **self.boto_client_params)
                self.client = client
    
    def GetClient(self, svc=None):
        self.SetClient(svc)
        return self.client





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

    clients = []
    for p in profiles:
        for r in regions:
            c = Client(svc=svc,profile_name=p,region_name=r)
            clients.append(c)
    return clients