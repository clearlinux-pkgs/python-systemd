#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-systemd
Version  : 234
Release  : 32
URL      : https://github.com/systemd/python-systemd/archive/v234.tar.gz
Source0  : https://github.com/systemd/python-systemd/archive/v234.tar.gz
Summary  : Python bindings for systemd
Group    : Development/Tools
License  : LGPL-2.1
Requires: python-systemd-license = %{version}-%{release}
Requires: python-systemd-python = %{version}-%{release}
Requires: python-systemd-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(systemd)

%description
python-systemd
===============
Python module for native access to the systemd facilities. Functionality
is separated into a number of modules:
- systemd.journal supports sending of structured messages to the journal
and reading journal files,
- systemd.daemon wraps parts of libsystemd useful for writing daemons
and socket activation,
- systemd.id128 provides functions for querying machine and boot identifiers
and a lists of message identifiers provided by systemd,
- systemd.login wraps parts of libsystemd used to query logged in users
and available seats and machines.

%package license
Summary: license components for the python-systemd package.
Group: Default

%description license
license components for the python-systemd package.


%package python
Summary: python components for the python-systemd package.
Group: Default
Requires: python-systemd-python3 = %{version}-%{release}

%description python
python components for the python-systemd package.


%package python3
Summary: python3 components for the python-systemd package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-systemd package.


%prep
%setup -q -n python-systemd-234
cd %{_builddir}/python-systemd-234

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583215253
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
mkdir -p %{buildroot}/usr/share/package-licenses/python-systemd
cp %{_builddir}/python-systemd-234/LICENSE.txt %{buildroot}/usr/share/package-licenses/python-systemd/01a6b4bf79aca9b556822601186afab86e8c4fbf
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-systemd/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
