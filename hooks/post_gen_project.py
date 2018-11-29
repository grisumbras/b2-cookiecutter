import os
import shutil
import subprocess


def project_type():
    project_type = '{{cookiecutter.project_type}}'
    if project_type == 'lib':
        os.remove(os.path.join('src', 'main.cpp'))
    else:
        shutil.rmtree('include')
        os.remove(os.path.join('src', '{{cookiecutter.project_namespace}}.cpp'))


def conan():
    conan_type = '{{cookiecutter.conan}}'
    if conan_type != 'txt':
        os.remove(os.path.join('conan', 'conanfile.txt'))

    if conan_type != 'py':
        os.remove(os.path.join('conan', 'conanfile.py'))


def git():
    if not {{cookiecutter.git}}:
        return

    subprocess.call(['git', 'init'])

    remote = 'git@{server}:{owner}/{project}.git'.format(
        server="{{cookiecutter.remote_server}}",
        owner="{{cookiecutter.remote_username}}",
        project="{{cookiecutter.project_slug}}",
    )
    subprocess.call(['git', 'remote', 'add', 'origin', remote])


if __name__ == '__main__':
    project_type()
    conan()
    git()
