Summary:	gASQL - program which helps administer a DBMS database using the gnome-db framework
Name:		gASQL
Version:	0.5.3
Release:	2
License:	GPL
Group:		X11/GNOME/Applications
Group(pl):	X11/GNOME/Aplikacje
Source0:	http://malerba.linuxave.net/src/%{name}-%{version}.tar.gz
URL:		http://malerba.linuxave.net/
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		sysconfdir	/etc/X11/GNOME

%description
gASQL is a program which helps administer a DBMS database using the
gnome-db framework. Basically, it memorizes all the structure of the
database, and some queries, and does the SQL queries instead of the
user (not having to type all over again those SQL commands, although
it is still possible to do so).

%prep
%setup -q

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir={_applnkdir}/Office/Databases

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT
							  
%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz examples/
%attr(755,root,root) %{_bindir}/gasql
%{_datadir}/pixmaps/*
%{_applnkdir}/Office/Databases/gasql.desktop
%dir %{_datadir}/gASQL/
%dir %{_datadir}/gASQL/plugins
%{_datadir}/gASQL/plugins/*
