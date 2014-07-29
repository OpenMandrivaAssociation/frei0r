%define	major	0
%define	libname	%mklibname nut %{major}
%define	devname	%mklibname -d nut

Name:		frei0r
Version:	1.3
Release:	3
Url:		http://frei0r.dyne.org/
License:	GPLv2+
Group:		System/Libraries
Summary:	Minimalistic plugin API for video effects, plugins collection
Source0:	%{name}-plugins-%{version}.tar.gz
Provides:	%{name}-plugins = %{EVRD}
BuildRequires:	cmake
BuildRequires:	pkgconfig(opencv)
Buildrequires:	pkgconfig(gavl)

%description
Frei0r is a minimalistic plugin API for video effects.

The main emphasis  is on simplicity for an API that  will round up the
most common video effects into simple filters, sources and mixers that
can be controlled by parameters.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
%{_includedir}/frei0r.h
%dir %{_prefix}/lib/frei0r-1
%{_prefix}/lib/frei0r-1/*.so


%changelog
* Thu Nov 24 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.3-2
+ Revision: 733199
- reenable gavl support

* Thu Nov 24 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.3-1
+ Revision: 733158
- drop build dependency on gavl while it's in contrib
- imported package frei0r


* Thu Nov 24 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.3-1
- initial Mandriva package
