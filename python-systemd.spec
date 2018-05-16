#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-systemd
Version  : 234
Release  : 7
URL      : https://github.com/systemd/python-systemd/archive/v234.tar.gz
Source0  : https://github.com/systemd/python-systemd/archive/v234.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: python-systemd-python3
Requires: python-systemd-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(libsystemd)
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

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

%package python
Summary: python components for the python-systemd package.
Group: Default
Requires: python-systemd-python3

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

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507170426
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
