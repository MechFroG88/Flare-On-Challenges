import zlib

f = open("80.zlib", 'rb').read()
open("out", "w").write(zlib.decompress(f).hex())