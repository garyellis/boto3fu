from boto3fu.common import helpers


def get_instance(client, instance_id):
    """
    """
    instance = client.describe_instances(
        Filters=[{'Name': 'instance-id', 'Values': [instance_id]}]
    )

    return instance['Reservations'][0]


def eip_address(address):
    """
    """
    return {
        "instance_id": address.get("InstanceId") or '',
        "tag_Name": helpers.get_tag_value(address.get("Tags")),
        "public_ip": address.get("PublicIp")
    }

@helpers.add_account_alias
@helpers.add_account_num
@helpers.add_client_region
def get_eips(client):
    """
    """
    addresses = []
    for i in client.describe_addresses()['Addresses']:
        addresses.append(eip_address(i))
    return addresses