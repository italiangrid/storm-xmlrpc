#%global stable_branch 1
#%global svnrev     2181

#%{!?release_func:%global release_func() %1%{?dist}}

Summary: A lightweight RPC library based on XML and HTTP.
Name: storm-xmlrpc-c
Version: 1.25.10
Release: 1206.2181.sl5
License: BSD and MIT
Vendor: EMI
Group: System Environment/Libraries
Packager: Elisabetta Ronchieri
URL:     http://xmlrpc-c.sourceforge.net/
BuildArch: x86_64
BuildRoot: %{_builddir}/var/tmp/%{name}-%{version}
AutoReqProv: yes
Source: %name-%version-%release.src.tar.gz
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
%setup -q
rm doc/{INSTALL,configure_doc}

#%setup -n @PACKAGE@-%{version}
#rm doc/{INSTALL,configure_doc}

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"

autoconf
%configure --enable-curl-client --disable-libwww-client --enable-cplusplus --enable-shared-libs --prefix=/usr --bindir=/usr/bin/storm --sbindir=/usr/sbin/storm --datadir=/usr/share/ --includedir=/usr/include/storm --libdir=/usr/lib64/storm --mandir=/usr/man/storm --localstatedir=/usr/var/storm
make VERBOSE=1
cd tools
make
cd ..

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
cd tools
make install DESTDIR=$RPM_BUILD_ROOT
cd ..
#install -m 755 %{SOURCE1} ${RPM_BUILD_ROOT}%_bindir

chmod +x $RPM_BUILD_ROOT%_libdir/storm/*.so
rm -f $RPM_BUILD_ROOT%_libdir/storm/*.a

mkdir -p $RPM_BUILD_ROOT%_mandir/storm/man1/
#cp $RPM_BUILD_ROOT/usr/man/storm/man1/* $RPM_BUILD_ROOT%_mandir/storm/man1/

%clean
rm -rf $RPM_BUILD_ROOT

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
#%doc doc/*
%_libdir/storm/*.so.3*
%exclude %_libdir/storm/libxmlrpc_client.so*

%files client
%defattr(-,root,root,-)
%_libdir/storm/libxmlrpc_client.so.*

%files c++
%defattr(-,root,root,-)
%_libdir/storm/*.so.7*
%exclude %_libdir/storm/libxmlrpc_client++.so*

%files client++
%defattr(-,root,root,-)
%_libdir/storm/libxmlrpc_client++.so.*

%files devel
%defattr(-,root,root,-)
%_bindir/storm/xmlrpc-c-config
%_includedir/storm/xmlrpc-c
%_includedir/storm/*.h
%_libdir/storm/*.so

%files apps
%defattr(-,root,root,-)
#%doc tools/xmlrpc/xmlrpc.html
#%doc tools/xmlrpc_transport/xmlrpc_transport.html
#%_mandir/storm/man1/*
%_bindir/storm/xmlrpc
%_bindir/storm/xmlrpc_transport
%_bindir/storm/xml-rpc-api2cpp
%_bindir/storm/xmlrpc_cpp_proxy
%_bindir/storm/xml-rpc-api2txt
%exclude /usr/man/storm/man1/*

%changelog
* Mon Sep 27 2011 Elisabetta Ronchieri <elisabetta.ronchieri@cnaf.infn.it> - %version-%release
- Add spec to create package
