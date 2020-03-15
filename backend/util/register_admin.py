from db.admin import new_admin
import click


@click.command('register')
@click.option('-u', help="admin username", required=True)
@click.option('-p', help="admin password", required=True)
def register_admin(username, password):
    success, msg = new_admin(username, password)
    if success:
        click.echo('注册成功')
    else:
        click.echo(msg)

