import gc
import vfs
from flashbdev import bdev

try:
    if bdev:
        vfs.mount(bdev, "/")
except OSError:
    import inisetup

    inisetup.setup()

try:
    from _todefrost import package_md5sum

    md5 = None
    try:
        with open('/package.md5') as f:
            md5 = f.read().strip()
    except Exception as e:
        pass

    if md5 != package_md5sum.md5sum:
        print("package md5 changed....defrosting...")
        from _todefrost import microwave
        microwave.defrost()
        import machine
        machine.reset()
    else:
        print("no firmware change")
except Exception as e:
    print("exception during unfreeze....")
    print(e)
    pass

gc.collect() 
