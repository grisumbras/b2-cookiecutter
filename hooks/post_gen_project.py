import os
import shutil
import subprocess


def project_type():
    if '{{cookiecutter.project_type}}' == 'lib':
        os.remove(os.path.join('src', 'main.cpp'))
    else:
        shutil.rmtree('include')
        os.remove(os.path.join('src', '{{cookiecutter.project_namespace}}.cpp'))


def conan():
    for ext in ['py', 'txt']:
        if '{{cookiecutter.conan}}' != ext:
            os.remove('conanfile.' + ext)


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
    subprocess.call(['git', 'config', '--add', 'user.name', '{{cookiecutter.full_name}}'])
    subprocess.call(['git', 'config', '--add', 'user.email', '{{cookiecutter.email}}'])


if __name__ == '__main__':
    project_type()
    conan()
    git()
