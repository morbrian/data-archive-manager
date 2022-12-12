import click
import json
from mediator.mediator import create_mediator

supported_services = ['cats', 'dogs']

def format_result(result):
    if result is not None:
        return json.dumps(result, indent=4)
    else:
        return 'No Results'

@click.group()
def main():
    """
    mediator cli
    """
    pass

@main.command('snapshot')
@click.argument('service_name', type=click.Choice(supported_services))
@click.option('-u', '--url')
@click.option('-f', '--folder')
def snapshot(service_name, url, folder):
    """Store a snapshot of service data"""
    mediator = create_mediator(service_name, url, folder)
    result = mediator.snapshot()
    click.echo(format_result(result))

@main.command('history')
@click.argument('service_name', type=click.Choice(supported_services))
@click.option('-u', '--url')
@click.option('-f', '--folder')
def history(service_name, url, folder):
    """List history of service data snapshots"""
    mediator = create_mediator(service_name, url, folder)
    result = mediator.history()
    click.echo(format_result(result))

@main.command('fetch')
@click.argument('service_name', type=click.Choice(supported_services))
@click.argument('uuid')
@click.option('-u', '--url')
@click.option('-f', '--folder')
def history(service_name, uuid, url, folder):
    """Fetch data for a specific identified snapshot"""
    mediator = create_mediator(service_name, url, folder)
    result = mediator.fetch_snapshot(uuid)
    click.echo(format_result(result))

@main.command('diff')
@click.argument('service_name', type=click.Choice(supported_services))
@click.argument('uuid1')
@click.argument('uuid2')
@click.option('-u', '--url')
@click.option('-f', '--folder')
def diff(service_name, uuid1, uuid2, url, folder):
    """Fetch data for a specific identified snapshot"""
    mediator = create_mediator(service_name, url, folder)
    result = mediator.diff_snapshot_contents(uuid1, uuid2)
    click.echo(result)

if __name__ == "__main__":
    main()