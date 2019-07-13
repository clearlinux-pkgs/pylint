#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pylint
Version  : 2.3.1
Release  : 68
URL      : https://files.pythonhosted.org/packages/01/8b/538911c0ebc2529f15004f4cb07e3ca562bb9aacea5df89cc25b62e01891/pylint-2.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/01/8b/538911c0ebc2529f15004f4cb07e3ca562bb9aacea5df89cc25b62e01891/pylint-2.3.1.tar.gz
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
BuildRequires : buildreq-distutils3
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
%setup -q -n pylint-2.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551583731
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pylint
cp COPYING %{buildroot}/usr/share/package-licenses/pylint/COPYING
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
/usr/share/package-licenses/pylint/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
