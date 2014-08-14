.PHONY: module
module: ROOTFS usr.manifest

KSL:
	git clone -b OSv git@github.com:syuu1228/KSL.git

ROOTFS: ROOTFS/KSL
ROOTFS/KSL: KSL
	mkdir -p ROOTFS
	cp -a KSL ROOTFS/

usr.manifest:
	echo '/KSL/**: $${MODULE_DIR}/ROOTFS/KSL/**' >> usr.manifest
#	find ROOTFS/KSL/vendor/bundle -name '*.so' -exec ldd {} \;|awk '{print $$1,":",$$3}'|grep "/lib64"|grep -v "ld-linux"|grep -v "libc.so"|grep -v "libpthread.so"|grep -v "libdl.so"|grep -v "libm.so"|grep -v "libstdc++"|grep -v "libgcc_s"|grep -v "librt"|grep -v "sqlite3"|grep -v "libssl.so"|sort|uniq|sed -e "s/ //" \
	>> usr.manifest
	
clean:
	rm -rf usr.manifest ROOTFS KSL
