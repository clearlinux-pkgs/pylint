#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pylint
Version  : 1.5.6
Release  : 26
URL      : http://pypi.debian.net/pylint/pylint-1.5.6.tar.gz
Source0  : http://pypi.debian.net/pylint/pylint-1.5.6.tar.gz
Summary  : python code static checker
Group    : Development/Tools
License  : GPL-2.0
Requires: pylint-bin
Requires: pylint-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
.. image:: https://drone.io/bitbucket.org/logilab/pylint/status.png
:alt: drone.io Build Status
:target: https://drone.io/bitbucket.org/logilab/pylint

%package bin
Summary: bin components for the pylint package.
Group: Binaries

%description bin
bin components for the pylint package.


%package python
Summary: python components for the pylint package.
Group: Default

%description python
python components for the pylint package.


%prep
%setup -q -n pylint-1.5.6

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/epylint
/usr/bin/pylint
/usr/bin/pylint-gui
/usr/bin/pyreverse
/usr/bin/symilar

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
