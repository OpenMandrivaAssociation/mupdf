%define	devname	%mklibname -d %{name}
%define debug_package %{nil}

Name:		mupdf
Version:	1.14.0
Release:	1
Summary:	Lightweight PDF viewer and toolkit written in portable C
License:	GPLv3
Group:		Office
URL:		http://mupdf.com/
Source0:	https://mupdf.com/downloads/archive/mupdf-%{version}-source.tar.xz
Source1:	https://mujs.com/downloads/mujs-1.0.5.tar.xz
Source10:	mupdf.desktop
# Adapt to API changes in current lcms2mt
Patch0:		mupdf-1.14.0-lcms2mt.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(lcms2mt)
BuildRequires:	pkgconfig(glut)
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(harfbuzz)
BuildRequires:	jbig2dec-devel
BuildRequires:	openjpeg2-devel
BuildRequires:	desktop-file-utils

%description
MuPDF is a lightweight PDF viewer and toolkit written in portable C.

The renderer in MuPDF is tailored for high quality anti-aliased
graphics.  MuPDF renders text with metrics and spacing accurate to
within fractions of a pixel for the highest fidelity in reproducing
the look of a printed page on screen.

MuPDF has a small footprint.  A binary that includes the standard
Roman fonts is only one megabyte.  A build with full CJK support
(including an Asian font) is approximately five megabytes.

MuPDF has support for all non-interactive PDF 1.7 features, and the
toolkit provides a simple API for accessing the internal structures of
the PDF document.  Example code for navigating interactive links and
bookmarks, encrypting PDF files, extracting fonts, images, and
searchable text, and rendering pages to image files is provided.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Provides:	lib%{name} = %{version}-%{release}

%description -n	%{devname}
The %{devname} package contains header files for developing
applications that use MuPDF toolkit.

%prep
%autosetup -n %{name}-%{version}-source -p1 -a 1

%build
# do not use the inlined copies of build dpendencies
rm -rf thirdparty
mkdir thirdparty
mv mujs-1.0.5 thirdparty/mujs

%setup_compile_flags
%make -j1 verbose=yes USE_SYSTEM_LIBS=yes USE_SYSTEM_LCMS2=yes SYS_LCMS2_CFLAGS="-llcms2mt"

%install
%make_install prefix=%{_prefix} libdir=%{_libdir} USE_SYSTEM_LIBS=yes USE_SYSTEM_LCMS2=yes

desktop-file-install \
	 --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE10}

%files
%doc COPYING README
%{_bindir}/mutool
%{_bindir}/mupdf-x11
%{_bindir}/mupdf-gl
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop

%files -n %{devname}
%{_libdir}/libmupdf.a
%{_libdir}/libmupdf-third.a
%{_includedir}/mupdf
%doc %{_docdir}/mupdf
