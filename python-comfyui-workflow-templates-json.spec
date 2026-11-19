Name:		python-comfyui-workflow-templates-json
Version:	0.1.137
Release:	1
Summary:	Workflow template JSON for ComfyUI
License:	MIT
Group:		Development/Python
URL:		https://github.com/Comfy-Org/workflow_templates
Source0:	https://files.pythonhosted.org/packages/source/c/comfyui-workflow-templates-json/comfyui_workflow_templates_json-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

%description
JSON workflow definitions shown in the ComfyUI template browser.

%files
%{py_sitedir}/comfyui_workflow_templates_json
%{py_sitedir}/comfyui_workflow_templates_json-*.*-info
