import click
from flask import Blueprint

bp = Blueprint('students', __name__)

@bp.cli.command('view-cv')
@click.argument('section')
def create(section):
    ''' Command does not appear in flask commands and does not work'''
    pass