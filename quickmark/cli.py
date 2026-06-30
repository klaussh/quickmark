import click
from .bookmarks import BookmarkStore

@click.group()
def cli():
    """QuickMark - Fast CLI bookmark manager"""
    pass

@cli.command()
@click.argument('url')
@click.option('--tags', '-t', help='Comma-separated tags')
def add(url, tags):
    """Add a new bookmark"""
    store = BookmarkStore()
    tag_list = [t.strip() for t in tags.split(',')] if tags else []
    store.add(url, tags=tag_list)
    click.echo(f'Added: {url}')

@cli.command()
@click.argument('query')
def search(query):
    """Search bookmarks"""
    store = BookmarkStore()
    results = store.search(query)
    for bm in results:
        click.echo(f'{bm["url"]}  [{", ".join(bm["tags"])}]')

@cli.command()
@click.option('--tag', '-t', help='Filter by tag')
def list(tag):
    """List all bookmarks"""
    store = BookmarkStore()
    bookmarks = store.list(tag=tag)
    for bm in bookmarks:
        click.echo(f'{bm["url"]}  [{", ".join(bm["tags"])}]')

if __name__ == '__main__':
    cli()
