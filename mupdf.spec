%define name      mupdf
%define libname   %mklibname %{name}
%define develname %mklibname -d %{name}

Name:           %{name}
Version:        0.7
Release:        %mkrel 1
Summary:        MuPDF is a lightweight PDF viewer and toolkit written in portable C
License:        GPL
Group:          Office
URL:            http://mupdf.com/
Source0:        http://mupdf.com/download/mupdf-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  zlib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  freetype2-devel
BuildRequires:  jbig2dec-devel
BuildRequires:  openjpeg-devel

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

%package -n %{develname}
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:       lib%{name} = %{version}-%{release}

%description -n %{develname}
The %{develname} package contains header files for developing
applications that use %{libname}.

%prep
%setup

%build
%make

%install
rm -rf %{buildroot}
%make install prefix=%{buildroot}/usr

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/mupdf
%{_bindir}/pdfclean
%{_bindir}/pdfdraw
%{_bindir}/pdfextract
%{_bindir}/pdfinfo
%{_bindir}/pdfshow

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libmupdf.a
%{_includedir}/fitz.h
%{_includedir}/mupdf.h
