%global pypi_name pycotap

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        %mkrel 6
Summary:        A tiny test runner that outputs TAP results to standard output
Group:          Development/Python
License:        MIT
URL:            https://el-tramo.be/pycotap
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
pycotap is a simple Python test runner for unittest that outputs Test Anything
Protocol <>_ results directly to standard output.Contrary to other TAP runners
for Python, pycotap ...- ... prints TAP (and *only* TAP) to standard output
instead of to a separate file, allowing you to pipe it directly to TAP pretty
printers and processors (such as the ones listed on the tape page < By piping
it to...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
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
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
