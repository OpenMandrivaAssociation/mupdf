%define	libname	%mklibname %{name}
%define	devname	%mklibname -d %{name}

Name:		mupdf
Version:	1.0
Release:	2
Summary:	MuPDF is a lightweight PDF viewer and toolkit written in portable C
License:	GPLv3
Group:		Office
URL:		http://mupdf.com/
Source0:	http://mupdf.googlecode.com/files/%{name}-%{version}-source.tar.gz
Source1:	mupdf.desktop
BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:	zlib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	freetype2-devel
BuildRequires:	jbig2dec-devel
BuildRequires:	openjpeg-devel >= 1.5

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
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name} = %{version}-%{release}

%description -n	%{devname}
The %{devname} package contains header files for developing
applications that use %{libname}.

%prep
%setup -q -n %{name}-%{version}-source

%build
#gw pkg-config --cflags doesn't have the right openjpeg flags
%make XCFLAGS="%{optflags} -I%{_includedir}/openjpeg-1.5"

%install
%makeinstall
install -m644 %{SOURCE1} -D %{buildroot}%{_datadir}/applications/%{name}.desktop
install -m644 debian/mupdf.png -D %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%doc COPYING README
%{_bindir}/mudraw
%{_bindir}/mupdf
%{_bindir}/mupdfclean
%{_bindir}/mupdfextract
%{_bindir}/mupdfinfo
%{_bindir}/mupdfshow
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%files -n %{devname}
%{_libdir}/libfitz.a
%{_includedir}/fitz.h
%{_includedir}/memento.h
%{_includedir}/mucbz.h
%{_includedir}/mupdf.h
%{_includedir}/muxps.h
