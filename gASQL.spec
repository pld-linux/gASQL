Summary:	gASQL - program which helps administer a DBMS database using the gnome-db framework
Summary(pl):	gASQL - program pomagaj±cy administrowaæ baz± danych przy u¿yciu gnome-db
Name:		gASQL
Version:	0.5.3
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Source0:	http://malerba.linuxave.net/src/%{name}-%{version}.tar.gz
URL:		http://malerba.linuxave.net/
BuildRequires:	gettext-devel
BuildRequires:	gnome-db-devel
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

%description -l pl
gASQL to program pomagaj±cy administrowaæ systemem baz danych u¿ywaj±c
¶rodowiska gnome-db. Pamiêta ca³± strukturê bazy, niektóre zapytania,
a tak¿e wykonuje zapytania SQL zamiast u¿ytkownika (który nie musi
pisaæ ca³ych komend SQL - ale nadal mo¿e).

%prep
%setup -q

%build
gettextize --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir={_applnkdir}/Office/Databases

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT
							  
%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz examples
%attr(755,root,root) %{_bindir}/gasql
%{_pixmapsdir}/*
%{_applnkdir}/Office/Databases/gasql.desktop
%dir %{_datadir}/gASQL
%dir %{_datadir}/gASQL/plugins
%{_datadir}/gASQL/plugins/*
