Summary:	Themes for emerald
Summary(pl.UTF-8):	Motywy do emeralda
Name:		emerald-themes
Version:	0.6.0
Release:	1
Epoch:		1
License:	GPL/MIT
Group:		X11
Source0:	http://releases.compiz-fusion.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	7b3d6dd1b26ca81c706b73414342427c
URL:		http://forum.compiz-fusion.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
Requires:	emerald >= 1:0.5.2
Obsoletes:	cgwd-themes
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Themes for emerald.

%description -l pl.UTF-8
Motywy do emeralda.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%{_datadir}/emerald/themes
