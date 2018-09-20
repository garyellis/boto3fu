==================
boto3fu
==================

About
-----

boto3fu is a tool to simplify viewing aws resources.

Features
########

- multi aws accounts and regions support
- list aws resources
- describe aws resources (todo)
- output format in table, yaml, json and csv

Install
-------

::

  $ virtualenv --python=python2 boto3fu_venv
  $ source boto3fu_venv/bin/activate
  (boto3fu_venv) $ pip install git+https://github.com/garyellis/boto3fu.git

Usage
-----

::

    Usage: boto3fu [OPTIONS] COMMAND [ARGS]...

    Options:
      --version           Show the version and exit.
      -p, --profile TEXT  the aws credential profile
      -r, --region TEXT   the aws region. Defaults to us-west-2
      --verify-ssl TEXT   Disable hostname verify for corporate  proxies
      --debug TEXT        debug logging
      --help              Show this message and exit.

    Commands:
      list

Examples
--------

list eips::

    boto3fu -r us-west-2 -r us-east-1 --profile default list eips
    instance_id    public_ip      tag_Name
    -------------  -------------  -----------------------
                   35.164.230.25  shared-services-natgw-c
                   52.32.27.116   shared-services-natgw-b
                   52.39.140.93   shared-services-natgw-a
                   52.6.46.100


