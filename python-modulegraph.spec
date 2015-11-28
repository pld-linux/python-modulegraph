# %bcond_without	tests	# do not perform "make test"

%define 	module	modulegraph
Summary:	Module dependency analysis tool
Name:		python-%{module}
Version:	0.10.2
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/m/modulegraph/modulegraph-%{version}.tar.gz
# Source0-md5:	83c74c264843b83c92f62ed9856e49a8
URL:		http://pypi.python.org/pypi/modulegraph
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
modulegraph determines a dependency graph between Python modules
primarily by bytecode analysis for import statements.

modulegraph uses similar methods to modulefinder from the standard
library, but uses a more flexible internal representation, has more
extensive knowledge of special cases, and is extensible.

%prep
%setup -q -n modulegraph-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/modulegraph
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}*.egg-info
%endif
