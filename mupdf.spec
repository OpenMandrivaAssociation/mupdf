%define	devname	%mklibname -d %{name}
%define debug_package %{nil}

Name:		mupdf
Version:	1.21.1
Release:	2
Summary:	Lightweight PDF viewer and toolkit written in portable C
License:	GPLv3
Group:		Office
URL:		http://mupdf.com/
Source0:	https://mupdf.com/downloads/archive/mupdf-%{version}-source.tar.lz
Source10:	mupdf.desktop
Patch0:		mupdf-1.21.0-compile.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(lcms2mt)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(glu)
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(harfbuzz)
BuildRequires:	jbig2dec-devel
BuildRequires:	openjpeg2-devel
BuildRequires:	desktop-file-utils
BuildRequires:	lzip

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
%autosetup -n %{name}-%{version}-source -p1

%build
cd thirdparty
# Force system libs
#curl
#extract
#freeglut
#freetype
#gumbo-parser
#harfbuzz
#jbig2dec
#lcms2
#leptonica
#libjpeg
#mujs
#openjpeg
#README
#tesseract
#tesseract.txt
#zlib
rm -rf curl freeglut freetype harfbuzz jbig2dec lcms2 leptonica libjpeg openjpeg tesseract zlib
cd ..

%setup_compile_flags
%make -j1 verbose=yes USE_SYSTEM_LIBS=yes USE_SYSTEM_LCMS2=yes SYS_LCMS2_CFLAGS="-llcms2mt" USE_SYSTEM_GUMBO=no LD=ld.bfd

%install
%make_install prefix=%{_prefix} libdir=%{_libdir} USE_SYSTEM_LIBS=yes USE_SYSTEM_LCMS2=yes USE_SYSTEM_GUMBO=no LD=ld.bfd

desktop-file-install \
	 --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE10}

%files
%doc COPYING README
%{_bindir}/mutool
%{_bindir}/muraster
%{_bindir}/mupdf-x11
%{_bindir}/mupdf-x11-curl
%{_bindir}/mupdf-gl
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop

%files -n %{devname}
%{_libdir}/libmupdf.a
%{_libdir}/libmupdf-third.a
%{_includedir}/mupdf
%doc %{_docdir}/mupdf
