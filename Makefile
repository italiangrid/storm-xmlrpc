PACKAGE_NAME := storm-xmlrpc-c
PACKAGE_AGE := 1206.2181.2
PACKAGE_VERSION := 1.25.10

MODULE_NAME := xmlrpc-c
SPEC_STORM_XMLRPC_C_FILE := storm-xmlrpc-c.src.spec

RPM_MAIN_DIR := $(PWD)/rpm-build-test
RPM_SOURCE := $(RPM_MAIN_DIR)/SOURCES
RPM_SPEC := $(RPM_MAIN_DIR)/SPECS
RPM_BUILD := $(RPM_MAIN_DIR)/BUILD
RPM_RPM := $(RPM_MAIN_DIR)/RPMS
RPM_SRPM := $(RPM_MAIN_DIR)/SRPMS
RPM_DIRS := $(RPM_MAIN_DIR) $(RPM_SOURCE) $(RPM_SPEC) $(RPM_BUILD) $(RPM_RPM) $(RPM_SRPM)

XMLRPC_C_SERVER := https://xmlrpc-c.svn.sourceforge.net/svnroot/xmlrpc-c
XMLRPC_C_TAG := stable

osdist=`cat /etc/redhat-release | awk -F "release " '{ print $$2 }' | awk -F "." '{ print $$1 }'`

all: storm-xmlrpc-c-rpm

storm-xmlrpc-c-rpm: storm-xmlrpc-c-srpm
	@rpmbuild  --rebuild --define "_topdir $(RPM_MAIN_DIR)" --define "dist .el$(osdist)"  $(RPM_SRPM)/$(PACKAGE_NAME)-$(PACKAGE_VERSION)-$(PACKAGE_AGE)*.src.rpm

storm-xmlrpc-c-srpm: rpm-path checkout src-tar
	@cp -u $(MODULE_NAME)/tgz/$(PACKAGE_NAME)-$(PACKAGE_VERSION).src.tar.gz $(RPM_SOURCE)
	@cp $(SPEC_STORM_XMLRPC_C_FILE) $(RPM_SPEC)
	@rpmbuild  --define "_topdir $(RPM_MAIN_DIR)" --nodeps -bs $(RPM_SPEC)/$(SPEC_STORM_XMLRPC_C_FILE)

checkout:
	@svn co $(XMLRPC_C_SERVER)/$(XMLRPC_C_TAG) $(MODULE_NAME)

src-tar:
	@cd $(MODULE_NAME); \
	mkdir -p tgz/$(PACKAGE_NAME)-$(PACKAGE_VERSION); \
	tar -czf tgz/$(PACKAGE_NAME)-$(PACKAGE_VERSION)/$(PACKAGE_NAME)-$(PACKAGE_VERSION)-$(PACKAGE_AGE).src.tar.gz --exclude=.svn `ls | grep -v tgz$ | grep -v etics-tmp$ | grep -v etics.log$ `; \
	cd tgz/$(PACKAGE_NAME)-$(PACKAGE_VERSION); \
	tar -zxvf $(PACKAGE_NAME)-$(PACKAGE_VERSION)-$(PACKAGE_AGE).src.tar.gz; \
	rm $(PACKAGE_NAME)-$(PACKAGE_VERSION)-$(PACKAGE_AGE).src.tar.gz;\
	cd ..;\
	tar -czf $(PACKAGE_NAME)-$(PACKAGE_VERSION).src.tar.gz $(PACKAGE_NAME)-$(PACKAGE_VERSION);\
	rm -rf $(PACKAGE_NAME)-$(PACKAGE_VERSION);\
	cd ../..

rpm-path:
	@mkdir -p $(RPM_DIRS)

clean:
	@rm -rf $(RPM_MAIN_DIR) $(MODULE_NAME)
