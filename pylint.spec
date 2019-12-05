#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pylint
Version  : 2.4.4
Release  : 73
URL      : https://files.pythonhosted.org/packages/93/eb/851ab1d1ca6b37babd326dfa517b432963c54eda26c730353306aa0cdf4d/pylint-2.4.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/93/eb/851ab1d1ca6b37babd326dfa517b432963c54eda26c730353306aa0cdf4d/pylint-2.4.4.tar.gz
Summary  : python code static checker
Group    : Development/Tools
License  : GPL-2.0
Requires: pylint-bin = %{version}-%{release}
Requires: pylint-license = %{version}-%{release}
Requires: pylint-python = %{version}-%{release}
Requires: pylint-python3 = %{version}-%{release}
Requires: astroid
Requires: colorama
Requires: isort
Requires: mccabe
BuildRequires : astroid
BuildRequires : buildreq-distutils3
BuildRequires : colorama
BuildRequires : isort
BuildRequires : mccabe
BuildRequires : pytest-runner

%description
============================================
.. image:: https://travis-ci.org/PyCQA/pylint.svg?branch=master
:target: https://travis-ci.org/PyCQA/pylint

%package bin
Summary: bin components for the pylint package.
Group: Binaries
Requires: pylint-license = %{version}-%{release}

%description bin
bin components for the pylint package.


%package license
Summary: license components for the pylint package.
Group: Default

%description license
license components for the pylint package.


%package python
Summary: python components for the pylint package.
Group: Default
Requires: pylint-python3 = %{version}-%{release}

%description python
python components for the pylint package.


%package python3
Summary: python3 components for the pylint package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pylint package.


%prep
%setup -q -n pylint-2.4.4
cd %{_builddir}/pylint-2.4.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573743923
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pylint
cp %{_builddir}/pylint-2.4.4/COPYING %{buildroot}/usr/share/package-licenses/pylint/4d1d37f306ed270cda5b2741fac3abf0a7b012e5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/epylint
/usr/bin/pylint
/usr/bin/pyreverse
/usr/bin/symilar

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pylint/4d1d37f306ed270cda5b2741fac3abf0a7b012e5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
