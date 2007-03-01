Summary:	Bacula - The Network Backup Solution
Summary(pl.UTF-8):	Bacula - rozwiązanie do wykonywania kopii zapasowych po sieci
Name:		bacula-gui
Version:	2.0.2
Release:	0.1
License:	extended GPL v2
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/bacula/%{name}-%{version}.tar.gz
# Source0-md5:	8ac3ed8f4eaf1809bd110b70d966157a
URL:		http://www.bacula.org/
BuildArc:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/bacula
%define		_localstatedir	/var/lib/bacula

%description
Bacula - It comes by night and sucks the vital essence from your
computers.

Sets of various Bacula GUIs.

%package bimagemgr
Summary:	A utility to monitor and burn file backups to CDR
Group:		Networking/Utilities
Requires(post):	sed >= 4.0
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	bacula-server
Requires:	cdrecord
Requires:	mkisofs
Requires:	perl-DBI

%description bimagemgr
A utility to monitor and burn file backups to CDR.

%package web
Summary:	Bacula web base structure
Group:		Networking/Utilities
Requires(post):	sed >= 4.0
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Obsoletes:	bacula-updatedb

%description web
Bacula - It comes by night and sucks the vital essence from your
computers.

Base structure for Bacula web apps.

%package libweb
Summary:	Bacula web library
Group:		Networking/Utilities
Requires(post):	sed >= 4.0
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description libweb
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula web library.

%package brestore
Summary:	A restoration GUI in Perl/GTK
Group:		Networking/Utilities
Requires(post):	sed >= 4.0
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description brestore
Bacula - It comes by night and sucks the vital essence from your
computers.

A restoration GUI for bacula, we developed a simple Perl/GTK GUI.

It has the following features :
    - Direct SQL access to the database for good performance
    - Fast Time Navigation (switch almost instantaneously between the
      different versions of a directory, by changing the date from a list)
    - Possibility to choose a selected file, then browse all its available
      versions, and see directly if these versions are online in a library
      or not
    - Simple restoration by the generation of a BSR file
    - Works with either PostgreSQL or MySQL


%package bweb
Summary:	A Bacula web interface
Group:		Networking/Utilities
Requires(post):	sed >= 4.0
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description bweb
Bacula - It comes by night and sucks the vital essence from your
computers.

A Bacula web interface.

%prep
%setup -q -a 1

%build
# no building; yes there is configure file there but it's useless

%install
rm -rf $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files bimagemgr
%defattr(644,root,root,755)

%files web
%defattr(644,root,root,755)

%files libweb
%defattr(644,root,root,755)

%files brestore
%defattr(644,root,root,755)

%files bweb
%defattr(644,root,root,755)
