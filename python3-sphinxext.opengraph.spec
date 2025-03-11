Summary:	Sphinx extension to generate unique OpenGraph metadata
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do generowania unikatowych metadanych OpenGraph
Name:		python3-sphinxext.opengraph
Version:	0.9.1
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxext-opengraph/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxext-opengraph/sphinxext-opengraph-%{version}.tar.gz
# Source0-md5:	c67696654492bdca614f151b77c224d3
URL:		https://github.com/wpilibsuite/sphinxext-opengraph
BuildRequires:	python3 >= 1:3.8
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx extension to generate unique OpenGraph metadata.

%description -l pl.UTF-8
Rozszerzenie Sphinksa do generowania unikatowych metadanych OpenGraph.

%prep
%setup -q -n sphinxext-opengraph-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%dir %{py3_sitescriptdir}/sphinxext
%dir %{py3_sitescriptdir}/sphinxext/opengraph
%{py3_sitescriptdir}/sphinxext/opengraph/*.py
%dir %{py3_sitescriptdir}/sphinxext/opengraph/__pycache__
%{py3_sitescriptdir}/sphinxext/opengraph/__pycache__/*.py[co]
%{py3_sitescriptdir}/sphinxext/opengraph/_static
%{py3_sitescriptdir}/sphinxext_opengraph-%{version}-py*.egg-info
