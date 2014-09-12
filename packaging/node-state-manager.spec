Name:           node-state-manager
Version:        2.0.0
Release:        0
Summary:        GENIVI Node State Manager
License:	MPL-2.0
Group:		Automotive/GENIVI
Url:            http://projects.genivi.org/node-state-manager/
Source0:        %name-%version.tar.xz
Source1001: 	node-state-manager.manifest
BuildRequires:	autoconf >= 2.64, automake >= 1.11
BuildRequires:  libtool >= 2.2
BuildRequires:  pkgconfig
BuildRequires:	pkgconfig(automotive-dlt)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(libsystemd-daemon)
BuildRequires:	pkgconfig(persistence_client_library)

%description
The node state management is the central function for information
regarding the current running state of the embedded system. The Node
State Manager (NSM) component provides a common implementation
framework for the main state machine of the system. The NSM collates
information from multiple sources and uses this to determine the
current state(s).

%package devel
Summary:  Development files for package %{name}
Group:    Automotive/GENIVI
Requires: %{name} = %{version}

%description devel
This package provides header files and other developer related files
for package %{name}.

%package test
Summary:  Test files for package %{name}
Group:    Automotive/GENIVI
Requires: %{name} = %{version}

%description test
This package provides test related files for package %{name}.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%autogen --disable-static --with-systemdsystemunitdir=%{_unitdir}

make %{?_smp_mflags}

%install
%make_install

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_bindir}/NodeStateManager
%config %{_sysconfdir}/dbus-1/system.d/org.genivi.NodeStateManager.conf
%{_unitdir}/nodestatemanager-daemon.service
%{_datadir}/dbus-1/system-services/org.genivi.NodeStateManager.LifeCycleControl.service
%{_datadir}/dbus-1/interfaces/org.genivi.NodeStateManager.*.xml
# These `.so' files are not in the 'devel' subpackage since they are
# not symbolic links.
%{_libdir}/libNodeStateAccess.so
%{_libdir}/libNodeStateMachine.so

%files devel
%manifest %{name}.manifest
%{_includedir}/*.h
%{_libdir}/pkgconfig/node-state-manager.pc

%files test
%manifest %{name}.manifest
%{_bindir}/NodeStateTest
%{_libdir}/libNodeStateMachineTest.so
%{_datadir}/dbus-1/interfaces/org.genivi.NodeStateMachineTest.xml


%changelog
