#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-pyramid
Version  : 2.0.2
Release  : 6
URL      : https://files.pythonhosted.org/packages/47/c3/5d5736e692fc7ff052577f03136b5edfdf1e2e177eff2f4b91206acae11d/pyramid-2.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/47/c3/5d5736e692fc7ff052577f03136b5edfdf1e2e177eff2f4b91206acae11d/pyramid-2.0.2.tar.gz
Summary  : The Pyramid Web Framework, a Pylons project
Group    : Development/Tools
License  : ZPL-2.1
Requires: pypi-pyramid-bin = %{version}-%{release}
Requires: pypi-pyramid-license = %{version}-%{release}
Requires: pypi-pyramid-python = %{version}-%{release}
Requires: pypi-pyramid-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Pyramid
=======
.. image:: https://github.com/Pylons/Pyramid/workflows/Build%20and%20test/badge.svg?branch=2.0-branch
:target: https://github.com/Pylons/Pyramid/actions?query=workflow%3A%22Build+and+test%22
:alt: 2.0-branch Travis CI Status

%package bin
Summary: bin components for the pypi-pyramid package.
Group: Binaries
Requires: pypi-pyramid-license = %{version}-%{release}

%description bin
bin components for the pypi-pyramid package.


%package license
Summary: license components for the pypi-pyramid package.
Group: Default

%description license
license components for the pypi-pyramid package.


%package python
Summary: python components for the pypi-pyramid package.
Group: Default
Requires: pypi-pyramid-python3 = %{version}-%{release}

%description python
python components for the pypi-pyramid package.


%package python3
Summary: python3 components for the pypi-pyramid package.
Group: Default
Requires: python3-core
Provides: pypi(pyramid)
Requires: pypi(hupper)
Requires: pypi(plaster)
Requires: pypi(plaster_pastedeploy)
Requires: pypi(setuptools)
Requires: pypi(translationstring)
Requires: pypi(venusian)
Requires: pypi(webob)
Requires: pypi(zope.deprecation)
Requires: pypi(zope.interface)

%description python3
python3 components for the pypi-pyramid package.


%prep
%setup -q -n pyramid-2.0.2
cd %{_builddir}/pyramid-2.0.2
pushd ..
cp -a pyramid-2.0.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695771605
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyramid
cp %{_builddir}/pyramid-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pyramid/d73217e5856de88d31964bfd23238502f72f85c9 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pdistreport
/usr/bin/prequest
/usr/bin/proutes
/usr/bin/pserve
/usr/bin/pshell
/usr/bin/ptweens
/usr/bin/pviews

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyramid/d73217e5856de88d31964bfd23238502f72f85c9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
