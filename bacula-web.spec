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
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/bacula
%define		_localstatedir	/var/lib/bacula

%description
Bacula - It comes by night and sucks the vital essence from your
computers.

Sets of various Bacula GUIs.

%description -l pl.UTF-8
Bacula przychodzi nocą i wysysa żywotny ekstrakt z komputerów.

Zbiór różnych graficzych interfejsów do Baculi.

%package bimagemgr
Summary:	A utility to monitor and burn file backups to CDR
Summary(pl.UTF-8):	Narzędzie do monitorowania i wypalania kopii zapasowych na CDR
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

%description bimagemgr -l pl.UTF-8
Narzędzie do monitorowania i wypalania kopii zapasowych na CDR.

%package web
Summary:	Bacula web base structure
Summary(pl.UTF-8):	Struktura bazowa WWW dla Baculi
Group:		Networking/Utilities
Requires(post):	sed >= 4.0
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	bacula-updatedb

%description web
Base structure for Bacula web apps.

%description web -l pl.UTF-8
Struktura bazowa WWW dla Baculi.

%package libweb
Summary:	Bacula web library
Summary(pl.UTF-8):	Biblioteka WWW Baculi
Group:		Networking/Utilities
Requires(post):	sed >= 4.0
Requires:	%{name}-common = %{version}-%{release}

%description libweb
Bacula web library.

%description libweb -l pl.UTF-8
Biblioteka WWW Baculi.

%package brestore
Summary:	A restoration GUI in Perl/GTK+
Summary(pl.UTF-8):	GUI do odzyskiwania danych w Perlu/GTK+
Group:		Networking/Utilities
Requires(post):	sed >= 4.0
Requires:	%{name}-common = %{version}-%{release}

%description brestore
A restoration GUI for Bacula developed using Perl/GTK+.

It has the following features:
 - Direct SQL access to the database for good performance
 - Fast Time Navigation (switch almost instantaneously between the
   different versions of a directory, by changing the date from a list)
 - Possibility to choose a selected file, then browse all its available
   versions, and see directly if these versions are online in a library
   or not
 - Simple restoration by the generation of a BSR file
 - Works with either PostgreSQL or MySQL

%description brestore -l pl.UTF-8
GUI do odzyskiwania danych dla Baculi stworzone z użyciem Perla/GTK+.

Ma następujące możliwości:
 - bezpośredni dostęp SQL do bazy danych dla uzyskania dobrej
   wydajności
 - szybką nawigację w czasie (prawie natychmiastowe przełączanie
   między różnymi wersjami katalogu poprzez zmianę daty z listy)
 - możliwość wyboru zaznaczonego pliku, a następnie przeglądanie
   dostępnych wersji i oglądanie bezpośrednio, czy wersje są w
   bibliotece
 - proste odzyskiwanie poprzez generowanie pliku BSR
 - działa z PostgreSQL-em lub MySQL-em

%package bweb
Summary:	A Bacula web interface
Summary(pl.UTF-8):	Interfejs WWW do Baculi
Group:		Networking/Utilities
Requires(post):	sed >= 4.0
Requires:	%{name}-common = %{version}-%{release}

%description bweb
A Bacula web interface.

%description bweb -l pl.UTF-8
Interfejs WWW do Baculi.

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
