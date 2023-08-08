import zlib

open("test", "wb").write(zlib.compress(b'testing1234'))