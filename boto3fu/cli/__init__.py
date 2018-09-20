import click

from boto3fu import __version__
from boto3fu.cli.list import list_group


@click.group()
@click.version_option(version=__version__, prog_name="Boto3fu")
@click.option(
    '--profile',
    '-p',
    multiple=True,
    required=False,
    default=None,
    help='the aws credential profile')
@click.option(
    '--region',
    '-r',
    multiple=True,
    required=False,
    default=None,
    help='the aws region. Defaults to us-west-2'
)
@click.option(
    '--verify-ssl',
    required=False,
    help='Disable hostname verify for corporate  proxies'
)
@click.option(
    '--debug',
    required=False,
    help='debug logging'
)
@click.pass_context
def cli(ctx, profile, region, verify_ssl, debug):
    ctx.obj = {
        "profile": profile,
        "region": region,
        "verify_ssl": verify_ssl,
        "debug": debug
    }


cli.add_command(list_group)
