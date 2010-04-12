Name:           virtuosoconverter
Summary:        Virtuoso database converter tool
Version:        0.1
Release:        %mkrel 2
Group:          Graphical desktop/KDE
License:        GPLv2+
URL:            http://www.kde.org
Source0:        %name-%version.tar.bz2
BuildRequires:  kdelibs4-devel
BuildRequires:	kdebase4-workspace-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
virtuosoconverter is a tool that convert database created with
virtuoso 5 to virtuoso 6 format.

%files
%defattr(-,root,root)
%_kde_bindir/virtuosoconverter
%_kde_appsdir/virtuosoconverter

#--------------------------------------------------------------------

%prep
%setup -q -n %name

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %{buildroot}
