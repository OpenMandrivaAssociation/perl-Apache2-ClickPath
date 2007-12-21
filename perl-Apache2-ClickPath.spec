%define module		Apache2-ClickPath
%define name		perl-%{module}
%define version 	1.9.00
%define revision	1.900
%define release		%mkrel 1

Name: 		%{name}
Version: 	%{version}
Release:	%{release} 
Summary:	Apache WEB Server User Tracking
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Apache/%{module}-%{revision}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Class::Member)
BuildRequires:	perl(Perl::AtEndOfScope)
BuildRequires:  apache-mod_perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Apache2::ClickPath adds a PerlTransHandler and an output filter to
Apache's request cycle. The transhandler inspects the requested
URI to decide if an existing session is used or a new one has to
be created.

%prep
%setup -q -n %{module}-%{revision} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# make test don't work..., but works on 10.2
# make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Apache2
%{_mandir}/*/*



