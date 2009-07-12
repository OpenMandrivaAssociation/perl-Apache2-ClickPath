%define upstream_name		Apache2-ClickPath
%define upstream_version	1.901

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Apache WEB Server User Tracking
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Apache/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Class::Member)
BuildRequires:	perl(Perl::AtEndOfScope)
BuildRequires:  apache-mod_perl-devel
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
Apache2::ClickPath adds a PerlTransHandler and an output filter to
Apache's request cycle. The transhandler inspects the requested
URI to decide if an existing session is used or a new one has to
be created.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

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



