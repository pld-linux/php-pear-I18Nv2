%include	/usr/lib/rpm/macros.php
%define		_class		I18Nv2
%define		_status		beta
%define		_pearname	%{_class}

Summary:	%{_pearname} - internationalization
Summary(pl):	%{_pearname} - umiêdzynarodowienie
Name:		php-pear-%{_pearname}
Version:	0.11.1
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4cb3b382d5bdb2e420fe565d264cefaa
URL:		http://pear.php.net/package/I18Nv2/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{Country,DecoratedList,Language,Locale}

install %{_pearname}-%{version}/I18Nv2.php $RPM_BUILD_ROOT%{php_pear_dir}
install %{_pearname}-%{version}/{CommonList,Country,DecoratedList,Language,Locale,Negotiator}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/Country/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Country
install %{_pearname}-%{version}/DecoratedList/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/DecoratedList
install %{_pearname}-%{version}/Language/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Language
install %{_pearname}-%{version}/Locale/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Locale

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/tests
%{php_pear_dir}/%{_class}.php
%{php_pear_dir}/%{_class}
