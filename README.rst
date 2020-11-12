==================
boto3fu
==================

About
-----

boto3fu is a tool to simplify viewing aws resources.

Features
########

- multi aws accounts and regions support
- vpc views
- route53 views
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
      --version                       Show the version and exit.
      -p, --profile TEXT              the aws credential profile
      -r, --region TEXT               the aws region. Defaults to us-west-2
      --verify-ssl / --no-verify-ssl  Disable hostname verify for man in the
                                      middle proxies

      --debug TEXT                    debug logging
      --help                          Show this message and exit.

    Commands:
      route53
      vpc

Examples
--------

vpc list-eips::

        $ boto3fu -r us-west-2 -r us-east-1 --profile default vpc list-eips
        instance_id          tag_Name                 public_ip       region       account_number  account_alias
        -------------------  -----------------------  --------------  ---------  ----------------  ---------------
        ...
        ...

route53 list-resource-records::

        $ boto3fu route53 list-resource-records --name my.domain --name my-other.domain --name foo.bar --name bar.foo.bar
        boto3fu route53 list-resource-records --name ews.works --name foo.ews.works -o csv
        account_alias,account_number,alias_target,failover,name,region,resource_records,ttl,type,zone_id,zone_name
        ...
        ...

