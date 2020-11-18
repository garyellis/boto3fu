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
@click.option('--zone-type', type=click.Choice(['public', 'private', '',]), default='', help='the hosted zone type')
@click.pass_context
def report_r53_zones(ctx, output, zone_type):
    """
    """
    get_route53_zones(
        profile=ctx.obj["profile"],
        region=ctx.obj["region"],
        boto_client_params=ctx.obj["boto_client_params"],
        zone_type=zone_type,
        output_format=output,
    )


@route53_group.command(name="list-resource-records")
@add_common_options()
@click.option('--name', '-n', multiple=True)
@click.option('--zone-type', type=click.Choice(['public', 'private', '',]), default='', help='the hosted zone type')
@click.option('--r53-policy-type', '-rt', multiple=True, help='filter by the route53 record policy type')
@click.option('--record-type', '-t', multiple=True, help='filter by the dns record type')
@click.pass_context
def report_r53_resource_records(ctx, output, name, zone_type, r53_policy_type, record_type):
    """
    """
    get_route53_resource_records(
        profile=ctx.obj["profile"],
        region=ctx.obj["region"],
        boto_client_params=ctx.obj["boto_client_params"],
        output_format=output,
        zone_names=name,
        zone_type=zone_type,
        r53_policy_type=r53_policy_type,
        record_type=record_type
    )