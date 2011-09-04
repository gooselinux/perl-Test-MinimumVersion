Name:		perl-Test-MinimumVersion
Version:	0.011
Release:	2.1%{?dist}
Summary:	Check whether your code requires a newer perl
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/Test-MinimumVersion/
Source0:	http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Test-MinimumVersion-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:	noarch

BuildRequires:	perl(File::Find::Rule::Perl)
BuildRequires:	perl(Perl::MinimumVersion) >= 1.20

# For improved tests
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.08

%description
Check whether your code requires a newer perl than you think.

%prep
%setup -q -n Test-MinimumVersion-%{version}
find -type f -exec chmod -x {} \;

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%check
make test

%files
%defattr(-,root,root,-)
%doc Changes LICENSE
%{perl_vendorlib}/Test
%{_mandir}/man3/*

%changelog
* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.011-2.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.011-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 20 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.011-1
- Upstream update.

* Wed Jun 17 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.010-1
- Upstream update.

* Tue May 05 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.009-1
- Upstream update.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon May 26 2008 Ralf Corsépius <rc040203@freenet.de> - 0.008-1
- Upstream update.

* Thu Feb 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.007-4
- Rebuild normally, second pass

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.007-3
- Rebuild for perl 5.10 (again), first pass

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.007-2
- rebuild normally, second pass

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.007-1.1
- rebuild for new perl, first pass, tests and TPC disabled

* Mon Nov 19 2007 Ralf Corsépius <rc040203@freenet.de> - 0.007-1
- Initial version.
