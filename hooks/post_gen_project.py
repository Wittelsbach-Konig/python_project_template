import subprocess

from cookiecutter.prompt import read_user_variable


def init_git():
    """Инициализирует Git после генерации проекта"""
    if read_user_variable("init_git") == "yes":
        subprocess.run(["git", "init"])
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "Initial commit"])


if __name__ == "__main__":
    init_git()
