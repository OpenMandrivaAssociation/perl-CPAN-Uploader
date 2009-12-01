%define upstream_name    CPAN-Uploader
%define upstream_version 0.093330

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Upload things to the CPAN
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CPAN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Getopt::Long::Descriptive)
BuildRequires: perl(HTTP::Request::Common)
BuildRequires: perl(HTTP::Status)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(URI)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This code is mostly derived from cpan-upload-http by Brad Fitzpatrick,
which in turn was based on cpan-upload by Neil Bowers. I (rjbs) didn't
want to have to use a system call to run either of those, so I
refactored the code into this module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/cpan-upload

