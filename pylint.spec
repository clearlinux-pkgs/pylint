#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pylint
Version  : 1.9.2
Release  : 56
URL      : https://pypi.debian.net/pylint/pylint-1.9.2.tar.gz
Source0  : https://pypi.debian.net/pylint/pylint-1.9.2.tar.gz
Summary  : python code static checker
Group    : Development/Tools
License  : GPL-2.0
Requires: pylint-bin
Requires: pylint-python3
Requires: pylint-license
Requires: pylint-python
Requires: astroid
Requires: colorama
Requires: configparser
Requires: isort
Requires: mccabe
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pytest-runner
BuildRequires : python3-dev
BuildRequires : setuptools

%description
==========================================
.. image:: https://travis-ci.org/PyCQA/pylint.svg?branch=master
:target: https://travis-ci.org/PyCQA/pylint

%package bin
Summary: bin components for the pylint package.
Group: Binaries
Requires: pylint-license

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
Requires: pylint-python3

%description python
python components for the pylint package.


%package python3
Summary: python3 components for the pylint package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pylint package.


%prep
%setup -q -n pylint-1.9.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530987566
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pylint
cp COPYING %{buildroot}/usr/share/doc/pylint/COPYING
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
%defattr(-,root,root,-)
/usr/share/doc/pylint/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
