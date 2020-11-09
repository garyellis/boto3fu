import click

from boto3fu.cli.helpers import add_common_options
#from boto3fu.commands import get_eips, get_route53_zones, get_route53_resource_records
from boto3fu.vpc.commands import get_eips


@click.group(name="vpc")
@click.pass_context
def vpc_group(ctx):
    """
    """
    pass


@vpc_group.command(name="list-eips")
@add_common_options()
@click.pass_context
def report_eips(ctx, output):
    """
    """
    get_eips(
        profile=ctx.obj["profile"],
        region=ctx.obj["region"],
        boto_client_params=ctx.obj["boto_client_params"],
        output_format=output,
    )