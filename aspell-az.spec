Summary:	Azerbaijani dictionary for aspell
Summary(pl.UTF-8):	Azerski słownik dla aspella
Name:		aspell-az
Version:	0.02
%define	subv	0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/az/aspell6-az-%{version}-%{subv}.tar.bz2
# Source0-md5:	24d9d46c8fc23197666a43a7962a7b0d
URL:		http://aspell.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Azerbaijani dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Azerski słownik (lista słów) dla aspella.

%prep
%setup -q -n aspell6-az-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
