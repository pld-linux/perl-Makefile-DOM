#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Makefile
%define		pnam	DOM
%include	/usr/lib/rpm/macros.perl
Summary:	Makefile::DOM - Simple DOM parser for Makefiles
Summary(pl.UTF-8):	Makefile::DOM - prosty analizator DOM dla plików Makefile
Name:		perl-Makefile-DOM
Version:	0.006
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AG/AGENT/Makefile-DOM-%{version}.tar.gz
# Source0-md5:	c9136d35514d3445288d5f4b8cea5703
URL:		http://search.cpan.org/dist/Makefile-DOM/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Clone >= 0.18
BuildRequires:	perl-List-MoreUtils >= 0.21
BuildRequires:	perl-Params-Util >= 0.22
%endif
Requires:	perl-Clone >= 0.18
Requires:	perl-List-MoreUtils >= 0.21
Requires:	perl-Params-Util >= 0.22
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library can serve as an advanced lexer for (GNU) makefiles. It
parses makefiles as "documents" and the parsing is lossless. The
results are data structures similar to DOM trees. The DOM trees hold
every single bit of the information in the original input files,
including white spaces, blank lines and makefile comments. That means
it's possible to reproduce the original makefiles from the DOM trees.
In addition, each node of the DOM trees is modifiable and so is the
whole tree, just like the PPI module used for Perl source parsing and
the HTML::TreeBuilder module used for parsing HTML source.

%description -l pl.UTF-8
Ta biblioteka może służyć jako zaawansowany analizator leksykalny dla
plików (GNU) Makefile. Analizuje pliki Makefile jako "dokumenty" w
sposób bezstratny. Wynikiem są struktury danych podobne do drzew DOM.
Drzewa DOM przechowują każdy fragment informacji z oryginalnych plików
wejściowych, wraz z odstępami, pustymi liniami i komentarzami. Oznacza
to, że z drzew DOM można odtworzyć oryginalne pliki Makefile. Ponadto
każdy węzeł w drzewie DOM może być modyfikowany, podobnie jak całe
drzewo, podobnie jak w przypadku modułu PPI przy analizie źródeł
perlowych czy modułu HTML::TreeBuilder przy analizie źródeł HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

# fails
%{__rm} t/pod-coverage.t

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes TODO
%{perl_vendorlib}/MDOM
%dir %{perl_vendorlib}/Makefile
%{perl_vendorlib}/Makefile/DOM.pm
%{_mandir}/man3/MDOM*.3pm*
%{_mandir}/man3/Makefile::DOM.3pm*
