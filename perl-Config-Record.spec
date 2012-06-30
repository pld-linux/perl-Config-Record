#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Config
%define	pnam	Record
Summary:	Config::Record - Configuration file access
Summary(pl.UTF-8):	Config::Record - dostęp do plików konfiguracyjnych
Name:		perl-Config-Record
Version:	1.1.2
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Config/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3958d3b5221ddf65ba3143d28e0cd4e0
URL:		http://search.cpan.org/dist/Config-Record/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Pod-Coverage
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an API for loading and saving of simple
configuration file records. Entries in the configuration file are
essentially key,value pairs, with the key and values separated by a
single equals symbol. The key consists only of alphanumeric
characters. There are three types of values, scalar values can contain
anything except newlines. Trailing whitespace will be trimmed unless
the value is surrounded in double quotes.

%description -l pl.UTF-8
Ten moduł udostępnia API do odczytu i zapisu rekordów w prostych
plikach konfiguracyjnych. Wpisy w pliku konfiguracyjnym to zasadniczo
pary klucz=wartość. Klucz może zawierać tylko znaki alfanumeryczne. Są
dostępne trzy rodzaje wartości, wartości skalarne mogą zawierać
cokolwiek poza znakami nowej linii. Końcowe znaki odstępu są usuwane,
chyba że wartość jest umieszczona między podwójnymi cudzysłowami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Config/Record.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README
%{perl_vendorlib}/Config/Record.pm
%{_mandir}/man3/Config::Record.3pm*
%{_examplesdir}/%{name}-%{version}
