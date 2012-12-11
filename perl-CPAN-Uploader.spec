%define upstream_name    CPAN-Uploader
%define upstream_version 0.103000

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Upload things to the CPAN
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CPAN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Getopt::Long::Descriptive)
BuildRequires:	perl(HTTP::Request::Common)
BuildRequires:	perl(HTTP::Status)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(URI)

BuildArch:	noarch

%description
This code is mostly derived from cpan-upload-http by Brad Fitzpatrick,
which in turn was based on cpan-upload by Neil Bowers. I (rjbs) didn't
want to have to use a system call to run either of those, so I
refactored the code into this module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/cpan-upload


%changelog
* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.103.0-1mdv2011.0
+ Revision: 654029
- update to new version 0.103000

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.102.150-1mdv2011.0
+ Revision: 569929
- update to 0.102150

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.101.670-1mdv2011.0
+ Revision: 552260
- update to 0.101670

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.760-1mdv2010.1
+ Revision: 526424
- update to 0.100760

* Tue Mar 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.750-1mdv2010.1
+ Revision: 521584
- update to 0.100750

* Mon Mar 08 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.660-1mdv2010.1
+ Revision: 515656
- update to 0.100660

* Sun Dec 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.93.390-1mdv2010.1
+ Revision: 474074
- update to 0.093390

* Tue Dec 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.93.330-1mdv2010.1
+ Revision: 472238
- update to 0.093330

* Mon Aug 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.92.340-1mdv2010.0
+ Revision: 420275
- update to 0.092340

* Fri May 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.91.270-1mdv2010.0
+ Revision: 380979
- adding missing buildrequires
- adding description
- import perl-CPAN-Uploader


* Fri May 29 2009 cpan2dist 0.091270-1mdv
- initial mdv release, generated with cpan2dist

