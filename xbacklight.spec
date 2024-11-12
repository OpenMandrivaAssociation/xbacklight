Name:		xbacklight
Version:	1.2.4
Release:	1
Summary:	Command-line utility to set the display backlight level
Group:		System/X11
License:	MIT
Source:		https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xcb-atom)
BuildRequires:	pkgconfig(xcb-aux)
BuildRequires:	pkgconfig(xorg-macros)

%description
xbacklight is a simple command-line utility to set the backlight level
using the RandR 1.2 BACKLIGHT output property.


%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xbacklight
%{_mandir}/man1/xbacklight.1*

