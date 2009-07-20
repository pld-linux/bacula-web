# TODO
# - package other GUI's:
#   bimagemgr/ brestore/ bweb/
Summary:	Bacula - The Network Backup Solution
Summary(pl.UTF-8):	Bacula - rozwiązanie do wykonywania kopii zapasowych po sieci
Name:		bacula-gui
Version:	2.4.4
Release:	0.11
License:	Extended GPL v2
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/bacula/%{name}-%{version}.tar.gz
# Source0-md5:	1bf3cf1b9b51caaddf2468485044cd36
Patch0:		bacula-web.patch
Source1:	bacula-web.conf
URL:		http://www.bacula.org/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		bacula-web
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{_webapp}
%define		_cachedir	/var/cache/%{_webapp}
%define		_smartyplugindir	%{php_data_dir}/Smarty/plugins
%define		_localedir		%{_datadir}/locale

%description
Bacula - It comes by night and sucks the vital essence from your
computers.

Sets of various Bacula GUIs.

%description -l pl.UTF-8
Bacula przychodzi nocą i wysysa żywotny ekstrakt z komputerów.

Zbiór różnych graficzych interfejsów do Baculi.

%package -n bacula-web
Summary:	A Bacula web interface
Summary(pl.UTF-8):	Interfejs WWW do Baculi
Group:		Applications/WWW
Requires:	Smarty
# system pkg phplot causes dead loop
#Requires:	phplot
Requires:	php-pear-DB
Requires:	php-gd
Requires:	smarty-gettext
Requires:	webapps

%description -n bacula-web
Bacula web apps.

%description -n bacula-web -l pl.UTF-8
WWW dla Baculi.

%prep
%setup -q
%patch0 -p1

cd bacula-web
install -d smarty-plugins
mv external_packages/smarty/plugins/modifier.fsize_format.php smarty-plugins

# system pkg causes dead loop, keep it up cleanup first
mv external_packages/phplot .
rm -rf phplot/{doc,examples,LICENSE*,ChangeLog,README}

rm -rf templates_c external_packages configs/.htaccess test.php messages*.po array_fill.func.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir},%{_cachedir},%{_smartyplugindir},%{_localedir}}

cd bacula-web
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
cp -a . $RPM_BUILD_ROOT%{_appdir}
cp -a smarty-plugins/* $RPM_BUILD_ROOT%{_smartyplugindir}
mv $RPM_BUILD_ROOT{%{_appdir}/configs/*,%{_sysconfdir}}
rm $RPM_BUILD_ROOT%{_appdir}/{tsmarty2c.php,ChangeLog,CONTACT,README,TODO,COPYING}
rm -rf $RPM_BUILD_ROOT%{_appdir}/{locale,smarty-plugins}
for a in locale/*/LC_MESSAGES/*.mo; do
	l=${a#locale/}; l=${l%/LC_MESSAGES/*.mo}
	install -d $RPM_BUILD_ROOT%{_localedir}/$l/LC_MESSAGES
	cp -a $a $RPM_BUILD_ROOT%{_localedir}/$l/LC_MESSAGES/bacula-web.mo
	echo "%%lang($l) %{_localedir}/$l/LC_MESSAGES/bacula-web.mo" >> bacula-web.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%post -n bacula-web
# cleanup cache from previous rpm
echo %{_cachedir}/*.tpl.php | xargs rm -f

%preun
if [ "$1" = 0 ]; then
	echo %{_cachedir}/*.tpl.php | xargs rm -f
fi

%triggerin -n bacula-web -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -n bacula-web -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -n bacula-web -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -n bacula-web -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%files -n bacula-web -f bacula-web/bacula-web.lang
%defattr(644,root,root,755)
%doc bacula-web/{ChangeLog,CONTACT,README,TODO}
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bacula.conf
%{_appdir}
%{_smartyplugindir}/*.php
%dir %attr(730,root,http) %{_cachedir}
