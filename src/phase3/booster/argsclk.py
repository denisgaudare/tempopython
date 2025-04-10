import click

@click.command()
@click.option('--name', prompt='Votre nom', help='Nom à afficher')
@click.option('--age', default=30, help='Âge')
def hello(name, age):
    click.echo(f"Bonjour {name}, vous avez {age} ans.")

if __name__ == '__main__':
    hello()