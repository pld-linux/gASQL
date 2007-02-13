Summary:	gASQL - program which helps administer a DBMS database using the gnome-db framework
Summary(pl.UTF-8):	gASQL - program pomagający administrować bazą danych przy użyciu gnome-db
Name:		gASQL
Version:	0.5.3
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://malerba.linuxave.net/src/%{name}-%{version}.tar.gz
# Source0-md5:	b580c66eaed3db6df872c97bdf931159
URL:		http://malerba.linuxave.net/
BuildRequires:	gettext-devel
BuildRequires:	gnome-db-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		sysconfdir	/etc/X11/GNOME

%description
gASQL is a program which helps administer a DBMS database using the
gnome-db framework. Basically, it memorizes all the structure of the
database, and some queries, and does the SQL queries instead of the
user (not having to type all over again those SQL commands, although
it is still possible to do so).

%description -l pl.UTF-8
gASQL to program pomagający administrować systemem baz danych używając
środowiska gnome-db. Pamięta całą strukturę bazy, niektóre zapytania,
a także wykonuje zapytania SQL zamiast użytkownika (który nie musi
pisać całych komend SQL - ale nadal może).

%prep
%setup -q

%build
%{__gettextize}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir={_applnkdir}/Office/Databases

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO examples
%attr(755,root,root) %{_bindir}/gasql
%{_pixmapsdir}/*
%{_applnkdir}/Office/Databases/gasql.desktop
%dir %{_datadir}/gASQL
%dir %{_datadir}/gASQL/plugins
%{_datadir}/gASQL/plugins/*
