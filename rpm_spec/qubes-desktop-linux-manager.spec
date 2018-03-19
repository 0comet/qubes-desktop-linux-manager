#
# This is the SPEC file for creating binary RPMs for the Dom0.
#
#
# The Qubes OS Project, http://www.qubes-os.org
#
# Copyright (C) 2010  Joanna Rutkowska <joanna@invisiblethingslab.com>
# Copyright (C) 2010  Rafal Wojtczuk  <rafal@invisiblethingslab.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#

%{!?version: %define version %(cat version)}


Name:       qubes-desktop-linux-manager
Version:	%{version}
Release:	1%{dist}
Summary:	Qubes UI Applications

Group:		Qubes
Vendor:		Invisible Things Lab
License:	GPL
URL:		http://www.qubes-os.org

# because we have "#!/usr/bin/env python" shebangs, RPM puts
# "Requires: $(which # python)" dependency, which, depending on $PATH order,
# may point to /usr/bin/python or /bin/python (because Fedora has this stupid
# /bin -> usr/bin symlink). python*.rpm provides only /usr/bin/python.
AutoReq:	no

BuildArch: noarch

BuildRequires:  python3-devel

Requires:  python3-setuptools
Requires:  python3-dbus
Requires:  python3-gbulb
Requires:  qubes-dbus
Requires:	 libappindicator-gtk3
Requires:	 python3-systemd
Requires:  gtk3
Requires: python3-qubesadmin >= 4.0.13

Provides:   qui = %{version}-%{release}
Obsoletes:  qui < 4.0.0


%define _builddir %(pwd)

%description
A collection of GUI application for enhancing the Qubes UX.

%prep
# we operate on the current directory, so no need to unpack anything
# symlink is to generate useful debuginfo packages
rm -f %{name}-%{version}
ln -sf . %{name}-%{version}
%setup -T -D

%build
%py3_build

%install
%py3_install
mkdir -p $RPM_BUILD_ROOT/etc/xdg/autostart
cp autostart/qui-domains.desktop $RPM_BUILD_ROOT/etc/xdg/autostart
cp autostart/qui-devices.desktop $RPM_BUILD_ROOT/etc/xdg/autostart
cp autostart/qui-clipboard.desktop $RPM_BUILD_ROOT/etc/xdg/autostart
cp autostart/qui-disk-space.desktop $RPM_BUILD_ROOT/etc/xdg/autostart
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/Adwaita/22x22/devices/
cp icons/22x22/generic-usb.png $RPM_BUILD_ROOT/usr/share/icons/Adwaita/22x22/devices/generic-usb.png

%post
touch --no-create %{_datadir}/icons/Adwaita &>/dev/null || :

%postun
if [ $1 -eq 0 ]; then
    touch --no-create %{_datadir}/icons/Adwaita &>/dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/Adwaita &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/Adwaita &>/dev/null || :

%files
%defattr(-,root,root,-)

%dir %{python3_sitelib}/qui-*.egg-info
%{python3_sitelib}/qui-*.egg-info/*


%dir %{python3_sitelib}/qui
%dir %{python3_sitelib}/qui/__pycache__
%{python3_sitelib}/qui/__pycache__/*
%{python3_sitelib}/qui/__init__.py
%{python3_sitelib}/qui/decorators.py
%{python3_sitelib}/qui/domains_table.py
%{python3_sitelib}/qui/clipboard.py

%dir %{python3_sitelib}/qui/models/
%dir %{python3_sitelib}/qui/models/__pycache__
%{python3_sitelib}/qui/models/__pycache__/*
%{python3_sitelib}/qui/models/__init__.py
%{python3_sitelib}/qui/models/base.py
%{python3_sitelib}/qui/models/dbus.py
%{python3_sitelib}/qui/models/qubes.py


%dir %{python3_sitelib}/qui/tray/
%dir %{python3_sitelib}/qui/tray/__pycache__
%{python3_sitelib}/qui/tray/__pycache__/*
%{python3_sitelib}/qui/tray/__init__.py
%{python3_sitelib}/qui/tray/domains.py
%{python3_sitelib}/qui/tray/devices.py
%{python3_sitelib}/qui/tray/disk_space.py

%{_bindir}/qui-ls
%{_bindir}/qui-domains
%{_bindir}/qui-devices
%{_bindir}/qui-disk-space
/etc/xdg/autostart/qui-domains.desktop
/etc/xdg/autostart/qui-devices.desktop
/etc/xdg/autostart/qui-clipboard.desktop
/etc/xdg/autostart/qui-disk-space.desktop
/usr/share/icons/Adwaita/22x22/devices/generic-usb.png
