%if 0%{?fedora}
%global with_python3 1
%endif

%global pypi_name sphinxcontrib-websupport

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        1%{?dist}
Summary:        Sphinx API for Web Apps

License:        BSD
URL:            http://sphinx-doc.org/
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
 
%description
sphinxcontribwebuspport provides a Python API to easily integrate Sphinx
documentation into your Web application.

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
BuildRequires:  python2-devel
BuildRequires:  python-docutils
BuildRequires:  python-jinja2
BuildRequires:  python-mock
BuildRequires:  python-pytest
BuildRequires:  python-setuptools
BuildRequires:  python-six
BuildRequires:  python-sphinx
BuildRequires:  python-sqlalchemy
BuildRequires:  python-whoosh
BuildRequires:  xapian-bindings-python
Requires:       python-docutils
Requires:       python-jinja2
Requires:       python-six
Requires:       python-sphinx
Requires:       python-sqlalchemy
Requires:       python-whoosh

%description -n python2-%{pypi_name}
sphinxcontribwebuspport provides a Python API to easily integrate Sphinx
documentation into your Web application.

%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-setuptools
BuildRequires:  python3-jinja2
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
BuildRequires:  python3-six
BuildRequires:  python3-sphinx
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-whoosh
# FIXME(jpena) there are no xapian python3 bindings in Fedora
# BuildRequires:  xapian-bindings-python3
Requires:       python3-docutils
Requires:       python3-jinja2
Requires:       python3-six
Requires:       python3-sphinx
Requires:       python3-sqlalchemy
Requires:       python3-whoosh

%description -n python3-%{pypi_name}
sphinxcontribwebuspport provides a Python API to easily integrate Sphinx
documentation into your Web application.
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if 0%{?with_python3}
%py3_build
%endif
%py2_build

%install
%if 0%{?with_python3}
%py3_install
%endif
%py2_install

%check
py.test tests/
%if 0%{?with_python3}
py.test-3 tests/
%endif

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/sphinxcontrib/websupport
%{python2_sitelib}/sphinxcontrib_websupport-%{version}-py?.?-*.pth
%{python2_sitelib}/sphinxcontrib_websupport-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/sphinxcontrib/websupport
%{python3_sitelib}/sphinxcontrib_websupport-%{version}-py?.?-*.pth
%{python3_sitelib}/sphinxcontrib_websupport-%{version}-py?.?.egg-info
%endif

%changelog
* Fri Jun 30 2017 Javier Peña <jpena@redhat.com> - 1.0.1-1
- Initial package.

