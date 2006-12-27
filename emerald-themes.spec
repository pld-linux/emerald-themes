Summary:	Themes for emerald
Summary(pl):	Motywy do emeralda
Name:		emerald-themes
Version:	0.1.4
Release:	1
Epoch:		1
License:	GPL/MIT
Group:		X11
Source0:	http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	e2a2727f0667f09e82b60f5cb36ecd58
URL:		http://beryl-project.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
Requires:	emerald >= 1:0.1.3
Obsoletes:	cgwd-themes
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Themes for emerald.

%description -l pl
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
