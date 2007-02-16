
%bcond_with	animation	# enable progress bar animation

%define	_name	Clearlooks
%define	_num	19527
Summary:	%{_name} theme
Summary(pl.UTF-8):	Motyw %{_name}
Name:		gtk2-theme-engine-%{_name}
Version:	0.6.2
Release:	1
License:	GPL
Group:		Themes/GTK+
Source0:	http://www.gnome-look.org/content/files/%{_num}-clearlooks-%{version}.tar.bz2
# Source0-md5:	451ef33d1bffa261c5cbe01182199f97
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} theme.

%description -l pl.UTF-8
Temat %{_name}.

%prep
%setup -q -n clearlooks-%{version}

%build
%configure \
    %{?with_animation:--enable-animation}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS TODO
%{_datadir}/themes/Clearlooks
%{_datadir}/themes/Clearlooks-DeepSky
%{_datadir}/themes/Clearlooks-Olive
%{_datadir}/themes/Clearlooks-Quicksilver
%{_datadir}/icons/Clearlooks/index.theme
%{_datadir}/icons/Clearlooks/*/gtk/*.png
%dir %{_libdir}/gtk-2.0/*/engines
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/*.so
