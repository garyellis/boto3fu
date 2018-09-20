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
