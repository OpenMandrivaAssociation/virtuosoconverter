Name:           virtuosoconverter
Summary:        Virtuoso database converter tool
Version:        0.1
Release:        5
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


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-4mdv2011.0
+ Revision: 615411
- the mass rebuild of 2010.1 packages

* Wed Apr 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1-3mdv2010.1
+ Revision: 540283
- Updated tarball

  + Funda Wang <fwang@mandriva.org>
    - rebuild

* Wed Feb 03 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1-1mdv2010.1
+ Revision: 500268
- add buildrequire
- import virtuosoconverter


