import os
import shutil


def project_type():
    project_type = '{{cookiecutter.project_type}}'
    if project_type == 'lib':
        os.remove(os.path.join('src', 'main.cpp'))
    else:
        shutil.rmtree('include')
        os.remove(os.path.join('src', '{{cookiecutter.project_namespace}}.cpp'))


if __name__ == '__main__':
    project_type()
