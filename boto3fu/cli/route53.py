import click

from boto3fu.cli.helpers import add_common_options
from boto3fu.route53.commands import get_route53_zones, get_route53_resource_records


@click.group(name="route53")
@click.pass_context
def route53_group(ctx):
    """
    """
    pass


@route53_group.command(name="list-zones")
@add_common_options()
@click.pass_context
def report_r53_zones(ctx, output):
    """
    """
    get_route53_zones(
        profile=ctx.obj["profile"],
        region=ctx.obj["region"],
        boto_client_params=ctx.obj["boto_client_params"],
        output_format=output,
    )


@route53_group.command(name="list-resource-records")
@add_common_options()
@click.option('--name', '-n', multiple=True)
@click.pass_context
def report_r53_resource_records(ctx, output, name):
    """
    """
    get_route53_resource_records(
        profile=ctx.obj["profile"],
        region=ctx.obj["region"],
        boto_client_params=ctx.obj["boto_client_params"],
        output_format=output,
        zone_names=name
    )