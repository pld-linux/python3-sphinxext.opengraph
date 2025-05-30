# TODO: finish doc
#
# Conditional build:
%bcond_with	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Sphinx extension to generate unique OpenGraph metadata
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do generowania unikatowych metadanych OpenGraph
Name:		python3-sphinxext.opengraph
Version:	0.10.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxext-opengraph/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxext-opengraph/sphinxext_opengraph-%{version}.tar.gz
# Source0-md5:	ff6db715b0d85886b5e0ea1328204318
URL:		https://github.com/wpilibsuite/sphinxext-opengraph
BuildRequires:	python3 >= 1:3.9
BuildRequires:	python3-build
BuildRequires:	python3-flit_core >= 3.12
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
%if %{with tests}
BuildRequires:	python3-Sphinx >= 6.0
BuildRequires:	python3-bs4 >= 4.12.3
BuildRequires:	python3-pytest >= 7.4.4
%endif
BuildRequires:	rpmbuild(macros) >= 2.044
%if %{with doc}
BuildRequires:	python3-furo >= 2024
BuildRequires:	python3-matplotlib
BuildRequires:	python3-sphinx_design
BuildRequires:	sphinx-pdg-3 >= 8.1.0
%endif
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx extension to generate unique OpenGraph metadata.

%description -l pl.UTF-8
Rozszerzenie Sphinksa do generowania unikatowych metadanych OpenGraph.

%prep
%setup -q -n sphinxext_opengraph-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE.rst README.rst
%dir %{py3_sitescriptdir}/sphinxext
%dir %{py3_sitescriptdir}/sphinxext/opengraph
%{py3_sitescriptdir}/sphinxext/opengraph/*.py
%{py3_sitescriptdir}/sphinxext/opengraph/__pycache__
%{py3_sitescriptdir}/sphinxext/opengraph/_static
%{py3_sitescriptdir}/sphinxext_opengraph-%{version}.dist-info
