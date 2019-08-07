#!/usr/bin/env python
import pkg


def get_packages_info():
	db = pkg.PkgDb()
	pkgs = db.query()
	db.close()
	return pkgs
	

def remote_repo():
	db = pkg.PkgDb(remotedb=True)
	pkgs = db.rquery(pattern='zsh')
	db.close()
	return pkgs

def license_info():
	db = pkg.PkgDb()
	pkgs = db.query()
	pkgs.load_licenses()
	db.close()

def check_deps(pkg, db):
    for dep in pkg.deps():
        if not db.pkg_is_installed(dep.origin()):
            print '%s has a missing dependency: %s' % (pkg.origin(), dep.origin())
			
def get_dep_info():
	db = pkg.PkgDb()
    pkgs = db.query()
    pkgs.load_deps()
    for pkg in pkgs:
        check_deps(pkg, db)
    db.close()
