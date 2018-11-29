from conans import (
    ConanFile,
    tools,
)


{{cookiecutter.project_name.title().replace('-', '').replace(' ', '')}}Conan(ConanFile):
    name = '{{cookiecutter.project_slug}}'
    version = '{{cookiecutter.project_version}}'
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
    generators = 'b2',
    requires = ()
    build_requires = 'boost_build/{{cookiecutter.b2_version}}@bincrafers/stable',
    exports_sources = '../LICENSE', '../*.jam', '../src/*', {% if cookiecutter.project_type == 'lib' -%}
    '../include/*',
    {%- endif %}

    def build(self):
        if self.should_build:
            self.run('b2')

    def package(self):
        self.run('b2 install')

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
