%global pypi_name pycotap

Name:           python-%{pypi_name}
Version:        1.2.2
Release:        2
Summary:        A tiny test runner that outputs TAP results to standard output
Group:          Development/Python
License:        MIT
URL:            https://el-tramo.be/pycotap
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description
pycotap is a simple Python test runner for unittest that outputs Test Anything
Protocol <>_ results directly to standard output.Contrary to other TAP runners
for Python, pycotap ...- ... prints TAP (and *only* TAP) to standard output
instead of to a separate file, allowing you to pipe it directly to TAP pretty
printers and processors (such as the ones listed on the tape page < By piping
it to...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%files
%{_prefix}/COPYING
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py*.*.egg-info
