%define	devname	%mklibname -d %{name}

%bcond_with extract
%bcond_with gumbo-parser
%bcond_without lcms2
%bcond_with	mujs
%bcond_without jpegxr

Name:		mupdf
Version:	1.23.11
Release:	1
Summary:	Lightweight PDF viewer and toolkit written in portable C
License:	GPLv3
Group:		Office
URL:		http://mupdf.com/
Source0:	https://mupdf.com/downloads/archive/mupdf-%{version}-source.tar.gz
Source10:	mupdf.desktop
Source11:	mupdf-gl.desktop
#Patch0:		mupdf-1.21.0-compile.patch

BuildRequires:	imagemagick
BuildRequires:	jxrlib-devel
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(harfbuzz)
BuildRequires:	pkgconfig(jbig2dec)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(lcms2mt)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libopenjp2)
BuildRequires:	pkgconfig(mujs)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(zlib)
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

%files
%license COPYING
%doc README
%{_bindir}/*
%{_datadir}/applications/%{name}*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/pixmaps/%{name}*.xpm
%{_mandir}/man1/*.1.*

#---------------------------------------------------------------------------

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Provides:	lib%{name} = %{version}-%{release}

%description -n	%{devname}
The %{devname} package contains header files for developing
applications that use MuPDF toolkit.

%files -n %{devname}
%doc %{_docdir}/mupdf
%{_libdir}/libmupdf.a
%{_libdir}/libmupdf-third.a
%{_includedir}/mupdf

#---------------------------------------------------------------------------

%prep
%autosetup -n %{name}-%{version}-source -p1

# Force system libs except:
#	extract
#	gumbo-parser
#	mujs
rm -rf thirdparty/{curl,freeglut,freetype,harfbuzz,jbig2dec,lcms2,leptonica,libjpeg,openjpeg,tesseract,zlib}

%build
%setup_compile_flags
export XCFLAGS="%{optflags} -fPIC"
%make \
	build=debug \
	verbose=yes \
	USE_SYSTEM_LIBS=yes \
	USE_SYSTEM_EXTRACT=%{?with_extract:yes}%{!?with_extract:no} \
	USE_SYSTEM_GUMBO=%{?with_gumbo-parser:yes}%{!?with_gumbo-parser:no} \
	USE_SYSTEM_JPEGXR=%{?with_jpegxr:yes}%{!?with_jpegxr:no} \
	USE_SYSTEM_LCMS2=%{?with_lcms2:yes}%{!?with_lcms2:no} \
	USE_SYSTEM_MUJS=%{?with_mujs:yes}%{!?with_mujs:no} \
	SYS_LCMS2_CFLAGS="-llcms2mt" \
	LD=ld.bfd

%install
%make_install \
	prefix=%{_prefix} \
	libdir=%{_libdir} \
	build=debug \
	verbose=yes \
	USE_SYSTEM_LIBS=yes \
	USE_SYSTEM_EXTRACT=%{?with_extract:yes}%{!?with_extract:no} \
	USE_SYSTEM_GUMBO=%{?with_gumbo-parser:yes}%{!?with_gumbo-parser:no} \
	USE_SYSTEM_JPEGXR=%{?with_jpegxr:yes}%{!?with_jpegxr:no} \
	USE_SYSTEM_LCMS2=%{?with_lcms2:yes}%{!?with_lcms2:no} \
	USE_SYSTEM_MUJS=%{?with_mujs:yes}%{!?with_mujs:no} \
	SYS_LCMS2_CFLAGS="-llcms2mt" \
	LD=ld.bfd

# icons
for d in 16 32 48 64 72 128 256
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
	convert -background none -size "${d}x${d}" docs/logo/mupdf-logo.svg \
		%{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
	cp -a %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png \
		%{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}-gl.png
done
install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
convert -size 32x32 docs/logo/mupdf-logo.svg %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
cp -a %{buildroot}%{_datadir}/pixmaps/%{name}.xpm %{buildroot}%{_datadir}/pixmaps/%{name}-gl.xpm
install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/scalable/apps
install -pm 0644 docs/logo/mupdf-logo.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
install -pm 0644 docs/logo/mupdf-logo.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}-gl.svg

# .desktop(s)
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE10}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE11}

# add symlink for mupdf
pushd %{buildroot}/%{_bindir}
ln -s %{name}-x11 %{name}
popd

