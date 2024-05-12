from invoke import task
from settings import APP_NAME


@task
def build(c) -> None:
    cmd: str = f"docker build . -t {APP_NAME}"
    c.run(cmd, pty=True)


@task
def run(c, reset: bool = False) -> None:
    if reset:
        build(c)

    # Yes spaces are needed at the end for cli commands
    cmd: str = (f"docker run "
                f"--name {APP_NAME} "   # name the container
                f"--rm "                # remove container when exits
                f"-it "                 # interactive 
                f"-p 8000:8000 "        # publish list of ports
                f"{APP_NAME}")          # the image
    c.run(cmd, pty=True)


@task
def logs(c, container_name: str = f"{APP_NAME}") -> None:
    cmd: str = (f"docker logs "
                f"-f "
                f"--details "
                f"{container_name}")
    c.run(cmd, pty=True)


@task
def exec(c) -> None:
    cmd: str = f"docker exec -it {APP_NAME} /bin/bash"
    c.run(cmd, pty=True)

