Summary:	Othello clone (GTK+ version)
Summary(pl.UTF-8):	Klon Othello (wersja GTK+)
Name:		hexxagon
Version:	1.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://nesqi.homeip.net/hexxagon/download/%{name}-%{version}.tar.bz2
# Source0-md5:	f4064f4324598453dacbc1387aa0482c
Source1:	%{name}.png
# Source1-md5:	1548c629ff9f257871dcb16821cdd66e
Source2:	%{name}.desktop
Patch0:		%{name}-gcc4.patch
URL:		http://nesqi.homeip.net/hexxagon/
BuildRequires:	gtkmm-devel >= 2.4
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hexxagon is a clone of Hexxagon, an adaptation of the Othello board
game written for DOS. This is the GTK+ version of Hexxagon.

%description -l pl.UTF-8
Hexxagon to klon gry Hexxagon, adaptacji planszowej gry Othello dla
DOS-a. Jest to wersja GTK+ gry Hexxagon.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} -D $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
install %{SOURCE2} -D $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop
