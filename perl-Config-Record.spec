#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Config
%define	pnam	Record
Summary:	Config::Record - Configuration file access
#Summary(pl):
Name:		perl-Config-Record
Version:	1.1.2
Release:	0.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3958d3b5221ddf65ba3143d28e0cd4e0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES INSTALL README
%{perl_vendorlib}/Config/*.pm
#%{perl_vendorlib}/Config/Record
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
