Summary:	Othello clone (GTK version)
Summary(pl.UTF-8):	Klon Othello (wersja GTK)
Name:		hexxagon
Version:	1.0
Release:	0.1
Source0:	http://nesqi.homeip.net/hexxagon/download/%{name}-%{version}.tar.bz2
# Source0-md5:	f4064f4324598453dacbc1387aa0482c
Patch0:		%{name}-gcc4.patch
License:	GPL
Group:		X11/Applications/Games
URL:		http://nesqi.homeip.net/hexxagon/
BuildRequires:	gtk+2-devel
BuildRequires:	gtkmm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hexxagon is a clone of Hexxagon, an adaptation of the Othello board
game written for DOS. This is the GTK1 version of Hexxagon.

%description -l pl.UTF-8
Hexxagon to klon gry Hexxagon, adapcji planszowej gry Othello dla
DOS-a. Jest to wersja GTK1 gry Hexxagon.

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

#install %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
#%{_iconsdir}/%{name}.png
%{_datadir}/%{name}
