import click
import chalk

def process(input):
    click.echo(chalk.blue('you are in git module'))
    click.echo('input = %s' % input)
