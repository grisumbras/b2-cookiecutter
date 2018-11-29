{% set headerguard = cookiecutter.project_namespace.upper() + '_ALL_HPP' -%}
#ifndef {{headerguard}}
#define {{headerguard}}

namespace {{cookiecutter.project_namespace}} {


void stub();


} // namespace {{cookiecutter.project_namespace}}


#endif // {{headerguard}}
