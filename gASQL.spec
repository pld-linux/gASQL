# Note that this is NOT a relocatable package
# defaults for redhat
%define name	gASQL
%define ver	0.5.3
%define prefix     /usr
%define sysconfdir /etc

%define  RELEASE 1
%define  rel     %{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}

Summary: gASQL
Name: 		%name
Version:	%ver
Release: 	%rel
Copyright: 	GPL
Group: 		X11/GNOME/Applications
Source:		%{name}-%{ver}.tar.gz
BuildRoot: 	/tmp/%{name}-%{ver}-root
URL: 		http://malerba.linuxave.net/
DocDir: 	%{prefix}/doc

%description
gASQL is a database admin tool working with gnome-db

%prep
%setup

%build

# libtool workaround for alphalinux
%ifarch alpha
  ARCH_FLAGS="--host=alpha-redhat-linux"
%endif

CFLAGS="$RPM_OPT_FLAGS" ./configure $ARCH_FLAGS --prefix=%{prefix} --sysconfdir=%{sysconfdir} 

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} sysconfdir=$RPM_BUILD_ROOT%{sysconfdir} \
gASQL_Helpdir=$RPM_BUILD_ROOT%{prefix}/share/gnome/help/gASQL \
gnorbadir=$RPM_BUILD_ROOT%{sysconfdir}/CORBA/servers \
Applicationsdir=$RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Applications \
Pixmapdir=$RPM_BUILD_ROOT%{prefix}/share/pixmaps \
install

%clean
rm -rf $RPM_BUILD_ROOT

							  
%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README TODO
%doc examples/ 
%{prefix}/bin/gasql
%{prefix}/share/pixmaps/*
%{prefix}/share/locale/*
%{prefix}/share/gnome/apps/Applications/gasql.desktop
%{prefix}/share/gnome/help/gASQL/C/*
%{prefix}/share/gnome/help/gASQL/fr/*
%{prefix}/share/gASQL/plugins/*
