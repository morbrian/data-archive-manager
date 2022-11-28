import click
import json
from mediator.mediator import create_mediator

def format_result(result):
    return json.dumps(result, indent=4)

@click.group()
def main():
    """
    mediator cli
    """
    pass

@main.command('snapshot')
@click.argument('service_name', type=click.Choice(['cats', 'dogs']))
@click.option('-u', '--url')
@click.option('-f', '--folder')
def snapshot(service_name, url, folder):
    """Store a snapshot of service data"""
    mediator = create_mediator(service_name, url, folder)
    result = mediator.snapshot()
    click.echo(format_result(result))

@main.command('history')
@click.argument('service_name', type=click.Choice(['cats', 'dogs']))
@click.option('-u', '--url')
@click.option('-f', '--folder')
def history(service_name, url, folder):
    """List history of service data snapshots"""
    mediator = create_mediator(service_name, url, folder)
    result = mediator.history()
    click.echo(format_result(result))

if __name__ == "__main__":
    main()