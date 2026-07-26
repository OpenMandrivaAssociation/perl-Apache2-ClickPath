%define upstream_name		Apache2-ClickPath
Name:		perl-%{upstream_name}
Version:	1.901
Release:	7

Summary:	Apache WEB Server User Tracking
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://metacpan.org/dist/Apache2-ClickPath
Source0:	https://cpan.metacpan.org/authors/id/O/OP/OPI/Apache2-ClickPath-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Class::Member)
BuildRequires:	perl(Perl::AtEndOfScope)
BuildRequires:	apache-mod_perl-devel
BuildArch:	noarch

%description
Apache2::ClickPath adds a PerlTransHandler and an output filter to
Apache's request cycle. The transhandler inspects the requested
URI to decide if an existing session is used or a new one has to
be created.

%prep
%setup -q -n %{upstream_name}-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# make test don't work..., but works on 10.2
# make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Apache2
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.901.0-2mdv2011.0
+ Revision: 680461
- mass rebuild

* Sun Jul 12 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.901.0-1mdv2011.0
+ Revision: 395037
- update to 1.901
- using %1.901 fixed license field

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.9.00-4mdv2009.0
+ Revision: 255268
- rebuild

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.9.00-2mdv2008.1
+ Revision: 138101
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.9.00-1mdv2007.0
+ Revision: 73245
- import perl-Apache2-ClickPath-1.9.00-1mdv2007.0

* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.9.00-1mdv2007.0
- New version (upstream version 1.900)
- spec cleanup
- fix directory ownership

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.8-3mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Sat Oct 01 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.8-2mdk
- Buildrequires fix

* Wed Aug 17 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.8-1mdk
- New release 1.8

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 1.7-1mdk
- initial Mandriva package

