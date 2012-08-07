%define		_class		I18Nv2
%define		_status		beta
%define		_pearname	I18Nv2
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - internationalization
Summary(pl.UTF-8):	%{_pearname} - umiędzynarodowienie
Name:		php-pear-%{_pearname}
Version:	0.11.4
Release:	6
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d8679404737a85e7a36b5018b1abf156
URL:		http://pear.php.net/package/I18Nv2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(iconv)
Requires:	php(pcre)
Requires:	php-common >= 3:4.0.6
Requires:	php-pear
Requires:	php-pear-PEAR-core
Obsoletes:	php-pear-I18Nv2-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides basic support to localize your application, like
locale based formatting of dates, numbers and currency.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa dostarcza podstawowego wsparcia do lokalizacji aplikacji,
takich jak formatowanie dat, liczb czy walut na podstawie locale.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/I18Nv2.php
%{php_pear_dir}/I18Nv2
