Name:           gnome-shell
Version:        3.38.4
Release:        3
Summary:        Core user interface functions for the GNOME 3 desktop
Group:          User Interface/Desktops
License:        GPLv2+
URL:            https://wiki.gnome.org/Projects/GnomeShell
Source0:        http://download.gnome.org/sources/gnome-shell/3.38/%{name}-%{version}.tar.xz

Patch1: gnome-shell-favourite-apps-firefox.patch

BuildRequires:  meson ibus-devel chrpath dbus-glib-devel desktop-file-utils
BuildRequires:  evolution-data-server-devel gcr-devel gjs-devel glib2-devel
BuildRequires:  gobject-introspection json-glib-devel upower-devel mesa-libGL-devel
BuildRequires:  NetworkManager-libnm-devel polkit-devel startup-notification-devel
BuildRequires:  sassc gstreamer1-devel gtk3-devel gettext libcanberra-devel
BuildRequires:  python3-devel libXfixes-devel librsvg2-devel asciidoc
BuildRequires:  mutter-devel pulseaudio-libs-devel control-center gtk-doc
BuildRequires:  bash-completion gnome-autoar-devel gnome-desktop3-devel 
BuildRequires:  mesa-libEGL-devel systemd-devel python3
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.0 gnome-bluetooth-libs-devel

Requires:       gnome-desktop3 gobject-introspection gjs gtk3 libnma librsvg2
Requires:       json-glib mozilla-filesystem mutter upower polkit glib2
Requires:       gsettings-desktop-schemas gstreamer1 at-spi2-atk gnome-bluetooth
Requires:       ibus accountsservice-libs gdm control-center python3 gnome-settings-daemon
Requires:       switcheroo-control geoclue2 libgweather bolt gnome-session-xsession
Requires:	geoclue2-libs pipewire xdg-desktop-portal-gtk >= 1.8.0

Provides:       desktop-notification-daemon PolicyKit-authentication-agent

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
%autosetup -n %{name}-%{version} -p1


%build
%meson -Dextensions_app=false
%meson_build


%install
%meson_install

%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Shell.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/evolution-calendar.desktop


%preun
glib-compile-schemas --allow-any-name %{_datadir}/glib-2.0/schemas &> /dev/null ||:


%posttrans
glib-compile-schemas --allow-any-name %{_datadir}/glib-2.0/schemas &> /dev/null ||:


%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/gnome-*
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/glib-2.0/schemas/00_org.gnome.shell.gschema.override
%{_datadir}/applications/org.gnome.Shell.Extensions.desktop
%{_datadir}/applications/org.gnome.Shell.desktop
%{_datadir}/applications/evolution-calendar.desktop
%{_datadir}/applications/org.gnome.Shell.PortalHelper.desktop
%{_datadir}/gnome-control-center/keybindings/50-gnome-shell-system.xml
%{_datadir}/gnome-shell/

%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.Extensions.service
%{_datadir}/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.Notifications.service
%{_datadir}/dbus-1/services/org.gnome.Shell.PortalHelper.service
%{_datadir}/dbus-1/services/org.gnome.Shell.Screencast.service
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Extensions.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Introspect.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.PadOsd.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screencast.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screenshot.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider2.xml

%{_userunitdir}/org.gnome.Shell-disable-extensions.service
%{_userunitdir}/org.gnome.Shell.target
%{_userunitdir}/org.gnome.Shell@wayland.service
%{_userunitdir}/org.gnome.Shell@x11.service
%{_sysconfdir}/xdg/autostart/gnome-shell-overrides-migration.desktop

%dir %{_datadir}/xdg-desktop-portal/portals/
%{_datadir}/xdg-desktop-portal/portals/gnome-shell.portal
%{_datadir}/bash-completion/completions/gnome-extensions
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Shell.Extensions.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Shell.Extensions-symbolic.svg
%{_libdir}/gnome-shell/
%{_libexecdir}/gnome-shell-calendar-server
%{_libexecdir}/gnome-shell-perf-helper
%{_libexecdir}/gnome-shell-hotplug-sniffer
%{_libexecdir}/gnome-shell-portal-helper
%{_libexecdir}/gnome-shell-overrides-migration.sh
%{_datadir}/GConf/*

%files help
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/gnome-extensions.1.gz

%changelog
* Fri Jul 30 2021 chenyanpanHW <chenyanpan@huawei.com> - 3.38.4-3
- DESC: delete -Sgit from %autosetup, and delete BuildRequires git

* Wed Jun 23 2021 weijin deng <weijin.deng@turbolinux.com.cn> - 3.38.4-2
- Delete requires gdm-libs which gdm contains it
- Use pipewire replace pipewire-gstreamer which pipewire contains it
- Add xdg-desktop-portal-gtk for launching flatpak apps etc

* Mon May 31 2021 weijin deng <weijin.deng@turbolinux.com.cn> - 3.38.4-1
- Upgrade to 3.38.4
- Update Version, Release, Source0, BuildRequires, Requires
- Delete patches which existed in current version, modify one patch
- Update stage 'build', 'check', 'files'

* Tue Mar 30 2021 wangyue<wangyue92@huawei.com> - 3.30.1-7
- fix CVE-2020-17489

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
