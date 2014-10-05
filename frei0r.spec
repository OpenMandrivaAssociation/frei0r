%define	major	0
%define	libname	%mklibname nut %{major}
%define	devname	%mklibname -d nut

Name:		frei0r
Version:	1.4
Release:	1
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

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -qn %{name}-plugins-%{version}


%build
sed -i \
	-e '/set(CMAKE_C_FLAGS/d' \
	-e "/LIBDIR.*frei0r-1/s:lib:%{_libdir}:" \
	CMakeLists.txt

# http://bugs.gentoo.org/418243
sed -i \
	-e '/set.*CMAKE_C_FLAGS/s:"): ${CMAKE_C_FLAGS}&:' \
	src/filter/*/CMakeLists.txt
# libdir fix
sed -i 's:set (libdir "${CMAKE_INSTALL_PREFIX}/lib"):set (libdir "%{_libdir}"):g' CMakeLists.txt
sed -i 's:lib/pkgconfig:%{_lib}/pkgconfig:g' CMakeLists.txt

%cmake
%make

%install
%makeinstall_std -C build INSTALL="install -p"

%files
%dir %{_libdir}/frei0r-1
%{_libdir}/frei0r-1/*.so

%files devel
%{_includedir}/frei0r.h
%{_libdir}/pkgconfig/frei0r.pc
