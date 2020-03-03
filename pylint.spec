#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pylint
Version  : 2.4.4
Release  : 76
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
README for Pylint - http://pylint.pycqa.org/
============================================

.. image:: https://travis-ci.org/PyCQA/pylint.svg?branch=master
    :target: https://travis-ci.org/PyCQA/pylint

.. image:: https://ci.appveyor.com/api/projects/status/rbvwhakyj1y09atb/branch/master?svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/PCManticore/pylint

.. image:: https://coveralls.io/repos/github/PyCQA/pylint/badge.svg?branch=master
    :target: https://coveralls.io/github/PyCQA/pylint?branch=master


.. image:: https://img.shields.io/pypi/v/pylint.svg
    :alt: Pypi Package version
    :target: https://pypi.python.org/pypi/pylint

.. image:: https://readthedocs.org/projects/pylint/badge/?version=latest
    :target: http://pylint.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black

.. |tideliftlogo| image:: doc/media/Tidelift_Logos_RGB_Tidelift_Shorthand_On-White_small.png
   :width: 75
   :height: 60
   :alt: Tidelift

.. list-table::
   :widths: 10 100

   * - |tideliftlogo|
     - Professional support for pylint is available as part of the `Tidelift
       Subscription`_.  Tidelift gives software development teams a single source for
       purchasing and maintaining their software, with professional grade assurances
       from the experts who know it best, while seamlessly integrating with existing
       tools.

.. _Tidelift Subscription: https://tidelift.com/subscription/pkg/pypi-pylint?utm_source=pypi-pylint&utm_medium=referral&utm_campaign=readme


======
Pylint
======

**It's not just a linter that annoys you!**

Pylint is a Python static code analysis tool which looks for programming errors,
helps enforcing a coding standard, sniffs for code smells and offers simple refactoring
suggestions.

It's highly configurable, having special pragmas to control its errors and warnings
from within your code, as well as from an extensive configuration file.
It is also possible to write your own plugins for adding your own checks or for
extending pylint in one way or another.

It's a free software distributed under the GNU General Public Licence unless
otherwise specified.

Development is hosted on GitHub: https://github.com/PyCQA/pylint/

You can use the code-quality@python.org mailing list to discuss about
Pylint. Subscribe at https://mail.python.org/mailman/listinfo/code-quality/
or read the archives at https://mail.python.org/pipermail/code-quality/

Pull requests are amazing and most welcome.

Install
-------

Pylint can be simply installed by running::

    pip install pylint

If you are using Python 3.6+, upgrade to get full support for your version::

    pip install pylint --upgrade

If you want to install from a source distribution, extract the tarball and run
the following command ::

    python setup.py install


Do make sure to do the same for astroid, which is used internally by pylint.

For debian and rpm packages, use your usual tools according to your Linux distribution.

More information about installation and available distribution format
can be found here_.

Documentation
-------------

The documentation lives at http://pylint.pycqa.org/.

Pylint is shipped with following additional commands:

* pyreverse: an UML diagram generator
* symilar: an independent similarities checker
* epylint: Emacs and Flymake compatible Pylint


Testing
-------

We use tox_ for running the test suite. You should be able to install it with::

    pip install tox pytest


To run the test suite for a particular Python version, you can do::

    tox -e py37


To run individual tests with ``tox``, you can do::

    tox -e py37 -- -k name_of_the_test


We use pytest_ for testing ``pylint``, which you can use without using ``tox`` for a faster development cycle.

If you want to run tests on a specific portion of the code with pytest_, (pytest-cov_) and your local python version::

    # ( pip install pytest-cov )
    # Everything:
    python3 -m pytest tests/
    # Everything in tests/message with coverage for the relevant code:
    python3 -m pytest tests/message/ --cov=pylint.message
    coverage html
    # Only the functional test "missing_kwoa_py3":
    python3 -m pytest "tests/test_functional.py::test_functional[missing_kwoa_py3]"


Do not forget to clone astroid_ and install the last version::


    git clone https://github.com/PyCQA/astroid.git

    # From source
    python3 astroid/setup.py build sdist
    pip3 install astroid/dist/astroid*.tar.gz

    # Using an editable installation
    cd astroid
    python3 -m pip install -e .


For more detailed information, check the documentation.

.. _here: http://pylint.pycqa.org/en/latest/user_guide/installation.html
.. _tox: https://tox.readthedocs.io/en/latest/
.. _pytest: https://docs.pytest.org/en/latest/
.. _pytest-cov: https://pypi.org/project/pytest-cov/
.. _astroid: https://github.com/PyCQA/astroid

License
-------

pylint is, with a few exceptions listed below, `GPLv2 <COPYING>`_.

The icon files are licensed under the `CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>`_ license:

- `doc/logo.png <doc/logo.png>`_
- `doc/logo.svg <doc/logo.svg>`_

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
export SOURCE_DATE_EPOCH=1583207613
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
