local_205 = b'\x1c\x18\x04\x48\x47\x46\x48\x5a\x45\x11\x51\x5d\x5d\x5e\x43\x45\x60\x09\x1a\x04\x00\x5a\x0c\x50\x01\x43\x04\x4f\x04\x1b\x4e\x1d\x74\x20\x09\x4c\x1e\x1f\x16\x1c\x00\x06\x51\x08\x1a\x5e\x40\x51\x0b\x05\x06\x41\x08\x12\xa9\x8a\x9c\x20\x61\x6c\x6d\xe4\x47\x50\xa3\xa9\x5e\xec\x83\xbe\xe0\x4e\x6f\x6d\x67\xa9\xb1\xf0\xe0\x7b\x4d\xf8\x14\x69\xe4\x8c\xf0\xb7\x24\x56\xb8\x11\x7a\xb5\x32\x0f\x79\x2e\x21\xcb\x82\x23\x93\xba\x25\x25\x8b\x10\x82\x1d\x16\xd8\x1f\x53\x8e\x57\x1f\xda\x27\x7e\x85\x1e\x86\x3f\x04\x2e\x31\xbb\x94\xc0\x0f\x34\x22\x94\x41\x62\x55\xcc\x9c\x7e\x33\x5f\x87\x60\xe6\xc6\x3a\xa8\x05\x95\x16\x98\x2f\x08\x74\x79\x6d\x7b\xe0\x94\x3f\x09\x57\x3d\x72\x6c\x39\xf6\x97\x67\x26\x4f\xda\x74\xca\x24\x7a\xca\x7a\x1e\x08\x88\x91\x2f\xe2\xb3\x04\xd2\x7f\x28\x21\x3b\x0f\x64\x6d\x24\x66\x5f\x2c\x69\x5f\x75\x63\xc5\xff\xe1\x5f\x11\x65\xce\x46\x54\xec\x89\x71'

# open("out", "wb").write(bytes(local_205))

key = "omg is it almost over?!?"


final = ""
count = 0

for i in local_205:
    s = hex(i ^ ord(key[count % len(key)]))[2:]
    if (len(s) == 1):
        final += "\\x" + "0" + s
    else:
        final += "\\x" +s
    count += 1

open("out5", "w").write(final)

# such.5h311010101@flare-on.com