%define	devname	%mklibname -d %{name}
%define debug_package %{nil}

Name:		mupdf
Version:	1.11
Release:	1
Summary:	Lightweight PDF viewer and toolkit written in portable C
License:	GPLv3
Group:		Office
URL:		http://mupdf.com/
Source0:	http://mupdf.com/downloads/%{name}-%{version}-source.tar.gz
Source1:	mupdf.desktop
Patch1:		mupdf-1.10-no_opj_static.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(freetype2)
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
%setup -q -n %{name}-%{version}-source
%apply_patches

%build
# do not use the inlined copies of build dpendencies
rm -rf thirdparty

%setup_compile_flags
%make -j1 verbose=yes

%install
%makeinstall_std prefix=%{_prefix} libdir=%{_libdir}

desktop-file-install \
	 --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE1}

%files
%doc COPYING README
%{_bindir}/mujstest
%{_bindir}/mutool
%{_bindir}/muraster
%{_bindir}/mupdf-x11
%{_bindir}/mupdf-x11-curl
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop

%files -n %{devname}
%{_libdir}/libmupdf.a
%{_libdir}/libmupdfthird.a
%{_includedir}/mupdf
