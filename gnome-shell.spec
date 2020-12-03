Name:           gnome-shell
Version:        3.30.1
Release:        6
Summary:        Core user interface functions for the GNOME 3 desktop
Group:          User Interface/Desktops
License:        GPLv2+
URL:            https://wiki.gnome.org/Projects/GnomeShell
Source0:        http://download.gnome.org/sources/gnome-shell/3.30/%{name}-%{version}.tar.xz

Patch1: gnome-shell-favourite-apps-firefox.patch
Patch2: 0001-endSessionDialog-Immediately-add-buttons-to-the-dial.patch
Patch3: 0002-endSessionDialog-Support-rebooting-into-the-bootload.patch
Patch4: 0001-keyboardManager-Avoid-idempotent-calls-to-meta_backe.patch
Patch5: 0001-Include-the-libcroco-sources-directly-under-src-st-c.patch

BuildRequires:  meson git ibus-devel chrpath dbus-glib-devel desktop-file-utils
BuildRequires:  evolution-data-server-devel gcr-devel gjs-devel glib2-devel
BuildRequires:  gobject-introspection json-glib-devel upower-devel mesa-libGL-devel
BuildRequires:  NetworkManager-libnm-devel polkit-devel startup-notification-devel
BuildRequires:  sassc gstreamer1-devel gtk3-devel gettext libcanberra-devel
BuildRequires:  libcroco-devel python3-devel libXfixes-devel librsvg2-devel
BuildRequires:  mutter-devel pulseaudio-libs-devel control-center gtk-doc

Requires:       gnome-desktop3 gobject-introspection gjs gtk3 libnma librsvg2
Requires:       json-glib mozilla-filesystem mutter upower polkit glib2
Requires:       gsettings-desktop-schemas libcroco gstreamer1 at-spi2-atk
Requires:       ibus accountsservice-libs gdm control-center python3
Requires:       switcheroo-control geoclue2 libgweather bolt

Provides:       desktop-notification-daemon

%description
The GNOME Shell redefines user interactions with the GNOME desktop. In particular,
it offers new paradigms for launching applications, accessing documents, and
organizing open windows in GNOME. Later, it will introduce a new applets eco-system
and offer new solutions for other desktop features, such as notifications and contacts
management. The GNOME Shell is intended to replace functions handled by the GNOME Panel
and by the window manager in previous versions of GNOME. The GNOME Shell has rich
visual effects enabled by new graphical technologies.


%package        help
Summary:        Help files for %{name}
BuildArch:      noarch

%description    help
Help files for %{name}


%prep
%autosetup -n %{name}-%{version} -p1 -Sgit


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Shell.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/gnome-shell-extension-prefs.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/evolution-calendar.desktop


%preun
glib-compile-schemas --allow-any-name %{_datadir}/glib-2.0/schemas &> /dev/null ||:


%posttrans
glib-compile-schemas --allow-any-name %{_datadir}/glib-2.0/schemas &> /dev/null ||:


%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/gnome-shell
%{_bindir}/gnome-shell-extension-tool
%{_bindir}/gnome-shell-perf-tool
%{_bindir}/gnome-shell-extension-prefs
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/glib-2.0/schemas/00_org.gnome.shell.gschema.override
%{_datadir}/applications/org.gnome.Shell.desktop
%{_datadir}/applications/gnome-shell-extension-prefs.desktop
%{_datadir}/applications/evolution-calendar.desktop
%{_datadir}/applications/org.gnome.Shell.PortalHelper.desktop
%{_datadir}/gnome-control-center/keybindings/50-gnome-shell-system.xml
%{_datadir}/gnome-shell/
%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.PortalHelper.service
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Extensions.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.PadOsd.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screencast.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screenshot.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider2.xml
%{_userunitdir}/gnome-shell.service
%{_userunitdir}/gnome-shell-wayland.target
%{_userunitdir}/gnome-shell-x11.target
%{_sysconfdir}/xdg/autostart/gnome-shell-overrides-migration.desktop
%dir %{_datadir}/xdg-desktop-portal/portals/
%{_datadir}/xdg-desktop-portal/portals/gnome-shell.portal
%{_libdir}/gnome-shell/
%{_libdir}/mozilla/plugins/*.so
%{_libexecdir}/gnome-shell-calendar-server
%{_libexecdir}/gnome-shell-perf-helper
%{_libexecdir}/gnome-shell-hotplug-sniffer
%{_libexecdir}/gnome-shell-portal-helper
%{_libexecdir}/gnome-shell-overrides-migration.sh
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/gnome-shell-overrides.convert

%files help
%{_mandir}/man1/%{name}.1.gz

%changelog
* Thu Dec 03 2020 wangxiao<wangxia65@huawei.com> -3.30.1-6
- move the libcroco sources directly under src/st
  remove the libcroco dependency from the meson.build files

* Fri Dec 27 2019 Jiangping Hu<hujiangping@huawei.com> - 3.30.1-5
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:remove the xdg-desktop-portal-gtk in recommends

* Wed Nov 27 2019 openEuler Buildteam<buildteam@openeuler.org> - 3.30.1-4
- Package Init
