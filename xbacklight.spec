Name: xbacklight
Version: 1.1
Release: %mkrel 6
Summary: Command-line utility to set the display backlight level
Group: System/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libxrandr-devel >= 1.2

%description
xbacklight is a simple command-line utility to set the backlight level
using the RandR 1.2 BACKLIGHT output property.


%prep
%setup -q -n %{name}-%{version}

%build
%configure

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xbacklight
%defattr(-,root,man)
%{_mandir}/man1/xbacklight.*
