from conans import (
    ConanFile,
    python_requires,
    tools,
)
import re


b2 = python_requires('b2-helper/0.5.0@grisumbras/stable')


def get_version():
    try:
        content = tools.load("build.jam")
        match = re.search(r"constant\s*VERSION\s*:\s*(\S+)\s*;", content)
        return match.group(1)
    except:
        pass


@b2.build_with_b2
class {{cookiecutter.project_name.title().replace('-', '').replace(' ', '')}}Conan(ConanFile):
    name = '{{cookiecutter.project_slug}}'
    version = get_version()
    license = 'BSL-1.0'
    description = '{{cookiecutter.project_description}}'
    {% if cookiecutter.git -%}
    {%- set url = 'https://'
                + cookiecutter.remote_server + '/'
                + cookiecutter.remote_username + '/'
                + cookiecutter.project_slug
    -%}
    homepage = '{{url}}'
    url = '{{url}}'
    {%- endif %}
    topics = ()

    author = '{{cookiecutter.full_name}} <{{cookiecutter.email}}>'
    default_user = '{{cookiecutter.conan_username}}'
    default_channel = 'testing'

    {% if cookiecutter.project_type == 'lib' -%}
    settings = 'arch', 'os', 'compiler', 'build_type',
    {%- else -%}
    settings = (
        'arch_build', 'os_build', 'arch_target', 'os_target', 'compiler',
        'build_type',
    )
    {%- endif %}
    {% if cookiecutter.project_type == 'lib' -%}
    options = {
        'shared': [True, False],
    }
    default_options = {
        'shared': True,
    }
    {% endif -%}
    requires = ()

    no_copy_source = True
    exports_sources = (
        'LICENSE*',
        '*build.jam',
        'src/*',
        {% if cookiecutter.project_type == 'lib' -%}
        'include/*',
        {%- endif %}
    )
