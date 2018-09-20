import click
import ast


class PythonLiteralOption(click.Option):

    def type_cast_value(self, ctx, value):
        try:
            return ast.literal_eval(value)
        except:
            raise click.BadParameter(value)


common_options = [
    click.option(
        '--output',
        '-o', type=click.Choice(['table', 'yaml', 'json', 'csv']),
        default='table',
        help='the output format'
    ),
]


def add_common_options(options=common_options):
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func
    return _add_options
