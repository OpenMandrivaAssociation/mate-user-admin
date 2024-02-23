Summary:	User management tool
Name:		mate-user-admin
Version:	1.7.0
Release:	1
License:	GPLv3+ 
Group:		Graphical desktop/Other
URL:		https://github.com/zhuyaliang/user-admin/
Source0:	https://github.com/zhuyaliang/user-admin/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		https://github.com/zhuyaliang/user-admin/commit/094986c6ac77cad0f4c34048cb51b3d345ca7348.patch

BuildRequires:	desktop-file-utils
BuildRequires:	meson
BuildRequires:	pkgconfig(accountsservice)
BuildRequires:	pkgconfig(group-service)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxcrypt)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	pkgconfig(pwquality)

%description
Mate User management tool

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/mate-user-admin
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/nuconfig
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/user-admin.png
%{_datadir}/polkit-1/actions/org.mate.user.admin.policy
%{_metainfodir}/%{name}.appdata.xml

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n user-admin-%{version}

sed -i -e 's/OnlyShowIn=MATE;/OnlyShowIn=MATE;XFCE;LXDE;/g' data/mate-user-admin.desktop.in
sed -i -e 's/nugroups =mail;audio;video;lightdm;/#nugroups =mail;audio;video;lightdm/g' data/mate-user-admin/nuconfig

%build
%meson
%meson_build

%install
%meson_install

desktop-file-install	\
	--delete-original \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/mate-user-admin.desktop

# locales
%find_lang %{name} --with-gnome --all-name

