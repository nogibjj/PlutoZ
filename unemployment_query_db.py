#!/usr/bin/env python3
import click
from dblib.querydb import querydb

# build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL DB"""


# build a click command
@cli.command()
@click.option("--unemployment_rate", help="Type in the countries unemployment rate")
def cli_query(unemployment_rate):
    """Execute a SQL query"""
    result = querydb(unemployment_rate)
    click.echo(result)


# run the CLI
if __name__ == "__main__":
    cli()
