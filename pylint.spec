#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pylint
Version  : 2.9.6
Release  : 109
URL      : https://files.pythonhosted.org/packages/47/18/d148ae88f254cbb9a8763beae34027bc603dc6f57b29c48f7cb3f2e28cde/pylint-2.9.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/47/18/d148ae88f254cbb9a8763beae34027bc603dc6f57b29c48f7cb3f2e28cde/pylint-2.9.6.tar.gz
Summary  : python code static checker
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: pylint-bin = %{version}-%{release}
Requires: pylint-license = %{version}-%{release}
Requires: pylint-python = %{version}-%{release}
Requires: pylint-python3 = %{version}-%{release}
Requires: astroid
Requires: colorama
Requires: isort
Requires: mccabe
Requires: toml
BuildRequires : astroid
BuildRequires : buildreq-distutils3
BuildRequires : colorama
BuildRequires : isort
BuildRequires : mccabe
BuildRequires : toml
Patch1: deps.patch

%description
No detailed description available

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
Provides: pypi(pylint)
Requires: pypi(astroid)
Requires: pypi(isort)
Requires: pypi(mccabe)
Requires: pypi(toml)

%description python3
python3 components for the pylint package.


%prep
%setup -q -n pylint-2.9.6
cd %{_builddir}/pylint-2.9.6
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1629129712
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pylint
cp %{_builddir}/pylint-2.9.6/LICENSE %{buildroot}/usr/share/package-licenses/pylint/909b58c9b803acb8d063ac6b2147e56afc8055f6
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
/usr/share/package-licenses/pylint/909b58c9b803acb8d063ac6b2147e56afc8055f6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
