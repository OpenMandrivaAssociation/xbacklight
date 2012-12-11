Name:		xbacklight
Version:	1.2.0
Release:	1
Summary:	Command-line utility to set the display backlight level
Group:		System/X11
License:	MIT
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xcb-atom)
BuildRequires:	pkgconfig(xcb-aux)

%description
xbacklight is a simple command-line utility to set the backlight level
using the RandR 1.2 BACKLIGHT output property.


%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/xbacklight
%{_mandir}/man1/xbacklight.1*

