%define	devname	%mklibname -d %{name}
%define debug_package %{nil}

Name:		mupdf
Version:	1.10a
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
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop

%files -n %{devname}
%{_libdir}/libmupdf.a
%{_libdir}/libmupdfthird.a
%{_includedir}/mupdf


%changelog
* Wed Aug 22 2012 Götz Waschk <waschk@mandriva.org> 1.1-1
+ Revision: 815596
- new version
- update file list

* Thu May 31 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0-2
+ Revision: 801569
- use pkgconfig() deps for buildrequires
- drop bogus dependency
- cleanups

  + Götz Waschk <waschk@mandriva.org>
    - add cbz to supported formats
    - bump openjpeg dep

* Wed May 02 2012 Götz Waschk <waschk@mandriva.org> 1.0-1
+ Revision: 795137
- update file list
- fix cflags for optimization and openjpeg header
- new version

* Wed Sep 28 2011 Götz Waschk <waschk@mandriva.org> 0.9-2
+ Revision: 701611
- install an icon file
- add desktop entry from Fedora

* Wed Sep 28 2011 Götz Waschk <waschk@mandriva.org> 0.9-1
+ Revision: 701609
- new version
- update license
- fix source URL
- drop patch
- fix installation
- add man pages, xpsdraw and new development files

* Wed Aug 25 2010 Florent Monnier <blue_prawn@mandriva.org> 0.7-1mdv2011.0
+ Revision: 573357
- patch for lib64
- BuildRequires: libxext-devel
- BuildRequires: libx11-devel
- import mupdf

