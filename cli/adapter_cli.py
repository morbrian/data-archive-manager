import click
import json
from adapter.generic_adapter import GenericAdapter

supported_services = ['cats', 'dogs']

def get_adapter(service_name, service_url):
    return GenericAdapter(service_name, service_url)

@click.group()
def main():
    """
    adapter cli
    """
    pass

@main.command('export')
@click.argument('service_name', type=click.Choice(supported_services))
@click.option('-u', '--url')
def export(service_name, url):
    """export all data from the service"""
    adapter = get_adapter(service_name, url)
    data = adapter.export_all() if adapter is not None else '{} service type not implemented'.format(service_name)
    click.echo(data)

@main.command('get')
@click.argument('service_name', type=click.Choice(supported_services))
@click.argument('id')
@click.option('-u', '--url')
def get(service_name, id, url):
    """get a specific identified data item from the service"""
    adapter = get_adapter(service_name, url)
    data = adapter.get(id) if adapter is not None else '{} service type not implemented'.format(service_name)
    click.echo(data)

@main.command('put')
@click.argument('service_name', type=click.Choice(supported_services))
@click.argument('id')
@click.argument('data')
@click.option('-u', '--url')
def put(service_name, id, data, url):
    """get a specific identified data item from the service"""
    adapter = get_adapter(service_name, url)
    data = adapter.put(id, json.loads(data)) if adapter is not None else '{} service type not implemented'.format(service_name)
    click.echo(data)

if __name__ == "__main__":
    main()