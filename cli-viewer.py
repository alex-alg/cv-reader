import click
import parser

@click.command()
@click.option("--section", prompt="Enter cv section (personal, experience, education)", help="Accepted values are: personal, experience, education")
def view_cv(section):
    sections = ["personal", "experience", "education"]

    if section in sections:
        data = parser.get_by_section(section)
        for item in data:
            click.echo(item)
    else:
        click.echo("Unsupported value. type \"cli-viewer.py --help\" for reference")

if __name__ == "__main__":
    view_cv()