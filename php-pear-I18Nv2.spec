%include	/usr/lib/rpm/macros.php
%define		_class		I18Nv2
%define		_status		beta
%define		_pearname	%{_class}

Summary:	%{_pearname} - internationalization
Summary(pl):	%{_pearname} - umiędzynarodowienie
Name:		php-pear-%{_pearname}
Version:	0.11.3
Release:	3
Epoch:		0
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fb081bc35cc1758dbd40329927194cd4
URL:		http://pear.php.net/package/I18Nv2/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.0.6
Requires:	php-iconv
Requires:	php-pcre
Requires:	php-pear
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides basic support to localize your application, like
locale based formatting of dates, numbers and currency.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa dostarcza podstawowego wsparcia do lokalizacji aplikacji,
takich jak formatowanie dat, liczb czy walut na podstawie locale.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

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
%{php_pear_dir}/%{_class}.php
%{php_pear_dir}/%{_class}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
