PACKAGE_VERSION := 1.39.12
PACKAGE_NAME := storm-xmlrpc-c
MODULE_NAME := xmlrpc-c

XMLRPC_SVN_URL := svn://svn.code.sf.net/p/xmlrpc-c/code/super_stable

all: checkout-sources clean

checkout-sources:
	svn export $(XMLRPC_SVN_URL) $(PACKAGE_NAME)-$(PACKAGE_VERSION)
	tar cvzf $(PACKAGE_NAME)-$(PACKAGE_VERSION).tar.gz $(PACKAGE_NAME)-$(PACKAGE_VERSION)

clean:
	rm -rf $(PACKAGE_NAME)-$(PACKAGE_VERSION)

distclean: clean
	rm -rf $(PACKAGE_NAME)-$(PACKAGE_VERSION).tar.gz
