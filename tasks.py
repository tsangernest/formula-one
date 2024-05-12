from typing import NoReturn

from invoke import task
from settings import APP_NAME


@task
def build(c) -> NoReturn:
    cmd: str = f"docker build . -t {APP_NAME}"
    c.run(cmd, pty=True)


@task
def run(c, reset: bool = False) -> NoReturn:
    if reset:
        build(c)
    cmd: str = f"docker run --name {APP_NAME} -it -p 8000:8000 {APP_NAME}"
    c.run(cmd, pty=True)


@task
def logs(c, container_name: str = f"{APP_NAME}") -> NoReturn:
    cmd: str = f"docker logs -f --details {container_name}"
    c.run(cmd, pty=True)


@task
def exec(c) -> NoReturn:
    cmd: str = f"docker exec -it {APP_NAME} /bin/bash"
    c.run(cmd, pty=True)

