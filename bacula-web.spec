# TODO
# - lighttpd support
%define		php_min_version 5.3.4
Summary:	Open source monitoring and reporting tool for Bacula
Name:		bacula-web
Version:	6.0.0
Release:	2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.bacula-web.org/download/articles/bacula-web-600.html?file=files/bacula-web.org/downloads/%{name}-%{version}.tgz
# Source0-md5:	3e99f9626cf4329ce43947f11a9d8f49
Source1:	apache.conf
Patch0:		sys-libs.patch
URL:		http://www.bacula-web.org/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	sed >= 4.0
Requires:	Smarty
Requires:	Smarty-plugin-gettext
Requires:	php(core) >= %{php_min_version}
Requires:	php(gd)
Requires:	php(gettext)
Requires:	php(pdo)
Requires:	php(session)
Requires:	phplot
Requires:	webserver(php)
# Any of the db drivers needed depending where you hold your Bacula DB
Suggests:	php-pdo-mysql
Suggests:	php-pdo-pgsql
Suggests:	php-pdo-sqlite
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{_webapp}
%define		cachedir	/var/cache/%{name}
%define		_smartyplugindir	%{php_data_dir}/Smarty/plugins

# bad depsolver
%define		_noautopear	pear
# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%description
Bacula-Web is a web based tool written in PHP that provide you a
summarized view of your bacula's backup infrastructure. It obtain his
information from your bacula catalog's database.

%prep
%setup -q
%patch -P0 -p1

mv application/config .
mv config/config.php{.sample,}
%{__rm} application/locale/*/LC_MESSAGES/*.po
%{__rm} -r application/view/cache
mv core/external .
mv DOCS/* .

# you'll need this if you cp -a complete dir in source
# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir},%{cachedir}}
cp -a *.php application core $RPM_BUILD_ROOT%{_appdir}
cp -a config/* $RPM_BUILD_ROOT%{_sysconfdir}

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
cp -p $RPM_BUILD_ROOT%{_sysconfdir}/{apache,httpd}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
# cleanup cache from previous rpm
echo %{cachedir}/* | xargs rm -f

%preun
if [ "$1" = 0 ]; then
	echo %{cachedir}/* | xargs rm -f
fi

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%files
%defattr(644,root,root,755)
%doc INSTALL README Changelog
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/config.php

%dir %{_appdir}
%{_appdir}/backupjob-report.php
%{_appdir}/client-report.php
%{_appdir}/index.php
%{_appdir}/joblogs.php
%{_appdir}/jobs.php
%{_appdir}/pools.php
%{_appdir}/test.php

%dir %{_appdir}/core
%{_appdir}/core/bweb.class.php
%{_appdir}/core/const.inc.php
%{_appdir}/core/global.inc.php
%{_appdir}/core/app
%{_appdir}/core/db
%{_appdir}/core/graph
%{_appdir}/core/i18n
%{_appdir}/core/utils

%dir %{_appdir}/application
%{_appdir}/application/libs
%{_appdir}/application/models
%{_appdir}/application/view

%dir %{_appdir}/application/locale
%lang(de) %{_appdir}/application/locale/de_DE
%lang(en) %{_appdir}/application/locale/en_EN
%lang(es) %{_appdir}/application/locale/es_ES
%lang(fr) %{_appdir}/application/locale/fr_FR
%lang(it) %{_appdir}/application/locale/it_IT
%lang(nl) %{_appdir}/application/locale/nl_NL
%lang(pt_BR) %{_appdir}/application/locale/pt_BR
%lang(sv) %{_appdir}/application/locale/sv_SV

%dir %attr(775,root,http) %{cachedir}
