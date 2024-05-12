from invoke import task
from settings import APP_NAME


@task
def build(c) -> None:
    cmd: str = f"docker build . -t {APP_NAME}"
    c.run(cmd, pty=True)


@task
def run(c):
    build(c)
    cmd: str = f"docker run --name {APP_NAME} -it -p 8000:8000 {APP_NAME}"
    c.run(cmd, pty=True)


@task
def logs(c):
    cmd: str = f"docker logs -f --details {APP_NAME}"
    c.run(cmd)




