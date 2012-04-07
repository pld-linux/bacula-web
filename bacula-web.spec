%define		php_min_version 5.2.4
#%include	/usr/lib/rpm/macros.php
Summary:	Open source monitoring and reporting tool for Bacula
Name:		bacula-web
Version:	5.2.2
Release:	0.3
License:	GPL v2
Group:		Applications/WWW
URL:		http://www.bacula-web.org/
Source0:	http://www.bacula-web.org/tl_files/downloads/%{name}.%{version}.tar.gz
# Source0-md5:	b52253963cc6edb6437a0dbe59c6051f
Source1:	apache.conf
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
#Requires:	php-Smarty
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-gd
Requires:	php-gettext
Requires:	php-pdo
Requires:	phplot
Requires:	smarty-gettext
Requires:	webserver(php)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{_webapp}
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
%setup -qc

mv config/config.php{.sample,}
rm locale/*/LC_MESSAGES/*.po

# nonstandard plugins
install -d smarty-plugins
#mv core/external/smarty/libs/plugins/modifier.fsize_format.php smarty-plugins

%{__rm} -r templates_c
#external_packages

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir}}
cp -a *.php core locale style templates $RPM_BUILD_ROOT%{_appdir}
#cp -a smarty-plugins/* $RPM_BUILD_ROOT%{_smartyplugindir}

cp -a config/* $RPM_BUILD_ROOT%{_sysconfdir}
ln -s %{_sysconfdir} $RPM_BUILD_ROOT%{_appdir}/config

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
cp -p $RPM_BUILD_ROOT%{_sysconfdir}/{apache,httpd}.conf

%clean
rm -rf $RPM_BUILD_ROOT

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
%doc INSTALL README
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/config.php
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/global.inc.php

%dir %{_appdir}
%{_appdir}/backupjob-report.php
%{_appdir}/client-report.php
%{_appdir}/index.php
%{_appdir}/jobs.php
%{_appdir}/pools.php
%{_appdir}/test.php
%{_appdir}/config
%{_appdir}/style
%{_appdir}/templates

%dir %{_appdir}/core
%{_appdir}/core/bweb.inc.php
%{_appdir}/core/app
%{_appdir}/core/cfg
%{_appdir}/core/db
%{_appdir}/core/graph
%{_appdir}/core/i18n
%{_appdir}/core/utils

%dir %{_appdir}/locale
%lang(de) %{_appdir}/locale/de_DE
%lang(en) %{_appdir}/locale/en_EN
%lang(es) %{_appdir}/locale/es_ES
%lang(fr) %{_appdir}/locale/fr_FR
%lang(it) %{_appdir}/locale/it_IT
%lang(sv) %{_appdir}/locale/sv_SV

%dir %{_appdir}/core/external
%{_appdir}/core/external/phplot
%{_appdir}/core/external/smarty
%{_appdir}/core/external/smarty_gettext-0.9

#%{_appdir}/templates_c
