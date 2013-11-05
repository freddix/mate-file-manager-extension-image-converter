Summary:	Image converter plugin for Caja file manager
Name:		mate-file-manager-extension-image-converter
Version:	1.6.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.6/mate-file-manager-image-converter-%{version}.tar.xz
# Source0-md5:	9af61933104bf154219ee64a2649d154
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	mate-file-manager-devel
BuildRequires:	pkg-config
Requires:	ImageMagick-coders
Requires:	mate-file-manager
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Adds a "Resize Images..." menu item to the context menu of all images.
This opens a dialog where you set the desired image size and file name.
A click on "Resize" finally resizes the image(s) using ImageMagick's
convert tool.

%prep
%setup -qn mate-file-manager-image-converter-%{version}

# kill mate common deps
%{__sed} -i -e '/MATE_COMPILE_WARNINGS.*/d'	\
    -i -e '/MATE_MAINTAINER_MODE_DEFINES/d'	\
    -i -e '/MATE_COMMON_INIT/d'			\
    -i -e '/MATE_CXX_WARNINGS.*/d'		\
    -i -e '/MATE_DEBUG_CHECK/d' configure.ac

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*/*/*.la

%find_lang caja-image-converter

%clean
rm -rf $RPM_BUILD_ROOT

%files -f caja-image-converter.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/*.so
%{_datadir}/caja-image-converter

