import click
from sayhello import app, db
from sayhello.models import Message
# 用于生成虚拟数据
from faker import Faker

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        click.confirm("This operation will delete the database, do you want to continue?", abort=True)
        db.drop_all()
        click.echo("Drop tables.")
    db.create_all()
    click.echo("Initialized database.")

@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    """Generate fake messages."""
    db.drop_all()
    db.create_all()

    fake = Faker()
    click.echo("Working...")

    for i in range(count):
        message = Message(name=fake.name(),
                          body=fake.sentence(),
                          timestamp=fake.date_time_this_year())
        db.session.add(message)

    db.session.commit()
    click.echo("Created %d fake messages." % count)