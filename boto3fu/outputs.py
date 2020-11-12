import sys
import csv
import json
import yaml

import tabulate


def to_table(items):
    """
    """
    print(tabulate.tabulate(
        tabular_data=items,
        headers='keys'
    ))


def to_csv(content, filename, append=False, keys=[]):
    """
    """
    if not keys:
        keys = sorted(content[0].keys())

    if filename:
        with open(filename, 'w') as stream:
            csv_writer = csv.DictWriter(stream, keys)
    else:
        csv_writer = csv.DictWriter(sys.stdout, keys)

        csv_writer.writeheader()
        csv_writer.writerows(content)


def to_yaml(items, filename):
    """
    """
    # convert ordered dict to regular dict to bypass adding yaml representer
    i = json.loads(json.dumps(items))

    opts = dict(default_flow_style=False, encoding='utf-8', allow_unicode=True)
    if not filename:
        print(yaml.safe_dump(data=i, stream=None, **opts))
    else:
        with open(filename, 'w') as s:
            yaml.safe_dump(data=i, stream=s, **opts)


def to_json(items, filename):
    """
    """
    if not filename:
        print(json.dumps(items))
    else:
        with open(filename, 'w') as s:
            json.dump(items, filename)


def output(items, output_format, filename=None):
    """
    """
    if output_format == 'table':
        to_table(items=items)

    elif output_format == 'json':
        to_json(items, filename)

    elif output_format == 'yaml':
        to_yaml(items, filename)

    elif output_format == 'csv':
        if items:
            to_csv(content=items, filename=filename)
