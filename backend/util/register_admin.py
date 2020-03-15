from db.admin import new_admin
import click


@click.command('register-admin')
@click.option('--username', help="admin username", required=True)
@click.option('--password', help="admin password", required=True)
def register_admin(username, password):
    success, msg = new_admin(username, password)
    if success:
        click.echo('注册成功')
    else:
        click.echo(msg)

