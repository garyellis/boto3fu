import click

from boto3fu.cli.helpers import add_common_options
from boto3fu.commands import get_eips


@click.group(name="list")
@click.pass_context
def list_group(ctx):
    """
    """
    pass


@list_group.command(name="eips")
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
