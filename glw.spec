Summary:	Xt / Motif OpenGL widgets
Name:		glw
Version:	8.0.0
Release:	2
License:	MIT
Group:		System/Libraries
Url:		http://www.mesa3d.org
Source0:	ftp://ftp.freedesktop.org/pub/mesa/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	lesstif-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xt)

%description
Mesa libGLw runtime library.

#----------------------------------------------------------------------------

%define major 1
%define libname %mklibname GLw %{major}

%package -n %{libname}
Summary:	Xt / Motif OpenGL widgets
Group:		System/Libraries

%description -n %{libname}
Mesa libGLw runtime library.

%files -n %{libname}
%doc README
%{_libdir}/libGLw.so.%{major}*

#----------------------------------------------------------------------------

%define devname %mklibname GLw -d

%package -n %{devname}
Summary:	Mesa libGLw development package
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Mesa libGLw development package.

%files -n %{devname}
%{_libdir}/libGLw.so
%{_includedir}/GL/GLwDrawA.h
%{_includedir}/GL/GLwDrawAP.h
%{_includedir}/GL/GLwMDrawA.h
%{_includedir}/GL/GLwMDrawAP.h
%{_libdir}/pkgconfig/glw.pc

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x \
	--enable-motif \
	--disable-static

%install
%makeinstall_std

