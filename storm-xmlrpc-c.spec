#%global stable_branch 1
#%global svnrev     2181

#%{!?release_func:%global release_func() %1%{?dist}}

Summary: A lightweight RPC library based on XML and HTTP.
Name: emi-storm-xmlrpc-c
Version: 1.25.10
Release: 1206.2181.sl5
License: BSD and MIT
Vendor: EMI
Group: System Environment/Libraries
Packager: Elisabetta Ronchieri
URL:     http://xmlrpc-c.sourceforge.net/
BuildArch: x86_64
BuildRoot: %{_builddir}/%{name}-%{version}-%{release}-root
AutoReqProv: yes
Source: %name-%version-%release.tar.gz
#BuildRoot: %_tmppath/%name-${version}-%release-root
BuildRequires: curl-devel
BuildRequires: libxml2-devel
BuildRequires: readline-devel
BuildRequires: ncurses-devel
BuildRequires: autoconf

%package c++
Summary:  C++ libraries for emi storm xmlrpc-c
Group:    System Environment/Libraries
Requires: %name = %version-%release
Requires: %name-c++ = %version-%release

%package client
Summary:  C client libraries for xmlrpc-c
Group:    System Environment/Libraries
Requires: %name = %version-%release

%package client++
Summary:  C++ client libraries for xmlrpc-c
Group:    System Environment/Libraries
Requires: %name = %version-%release
Requires: %name-c++ = %version-%release
Requires: %name-client = %version-%release

%package devel
Summary:  Development files for xmlrpc-c based programs
Group:    Development/Libraries
Requires: %name = %version-%release
Requires: %name-c++ = %version-%release
Requires: %name-client = %version-%release
Requires: %name-client++ = %version-%release
Requires: libxml2-devel curl-devel
Requires: pkgconfig

%package apps
Summary:  Sample XML-RPC applications
Group:    Applications/Internet
Requires: %name = %version-%release
Requires: %name-c++ = %version-%release
Requires: %name-client = %version-%release
Requires: %name-client++ = %version-%release

%description
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.
This library provides a modular implementation of XML-RPC for C.

%description c++
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.
This library provides a modular implementation of XML-RPC for C++.

%description client
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.
This library provides a modular implementation of XML-RPC for C
clients.
%description client++
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.
This library provides a modular implementation of XML-RPC for C++
clients.

%description devel
Static libraries and header files for writing XML-RPC applications in
C and C++.

%description apps
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.
This package contains some handy XML-RPC demo applications.

%prep


%setup -c

%install


%clean

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post client -p /sbin/ldconfig
%postun client -p /sbin/ldconfig

%post c++ -p /sbin/ldconfig
%postun c++ -p /sbin/ldconfig

%post client++ -p /sbin/ldconfig
%postun client++ -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc doc/*
%_libdir/*.so.3*
%exclude %_libdir/libxmlrpc_client.so*

%files client
%defattr(-,root,root,-)
%_libdir/libxmlrpc_client.so.*

%files c++
%defattr(-,root,root,-)
%_libdir/*.so.7*
%exclude %_libdir/libxmlrpc_client++.so*

%files client++
%defattr(-,root,root,-)
%_libdir/libxmlrpc_client++.so.*

%files devel
%defattr(-,root,root,-)
%_bindir/xmlrpc-c-config
%_includedir/xmlrpc-c
%_includedir/*.h
%_libdir/*.so

%files apps
%defattr(-,root,root,-)
%doc tools/xmlrpc/xmlrpc.html
%doc tools/xmlrpc_transport/xmlrpc_transport.html
%_mandir/man1/*
%_bindir/xmlrpc
%_bindir/xmlrpc_transport
%_bindir/xml-rpc-api2cpp
%_bindir/xmlrpc_cpp_proxy
%_bindir/xml-rpc-api2txt

%changelog
* Mon Sep 27 2011 Elisabetta Ronchieri <elisabetta.ronchieri@cnaf.infn.it> - %version-%release
- Add spec to create package
