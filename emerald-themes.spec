Summary:	Themes for emerald
Summary(pl):	Motywy do emerald
Name:		emerald-themes
Version:	20061102
Release:	1
License:	GPL/MIT
Group:		X11
#Source0:	http://distfiles.xgl-coffee.org/emerald-themes/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	9143cad6e4396e73ca5e8ffd5cbfc6bb
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
Requires:	emerald
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Themes for emerald.

%description -l pl
Motywy do emerald.

%prep
%setup -q -n %{name}

%build
autoreconf -v --install
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%dir %{_datadir}/emerald
%{_datadir}/emerald/themes
