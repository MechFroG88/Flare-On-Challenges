s = "\\97\\49\\x31\\68\\x4F\\x54\\116\\104\\x61\\116\\x44\\79\\x54\\106\\97\\118\\97\\53\\x63\\114\\x61\\x70\\65\\84\\102\\x6C\\x61\\114\\101\\x44\\65\\x53\\72\\111\\x6E\\x44\\x4F\\84\\99\\x6F\\x6D"

last = 0

for i in range(len(s)):
    if (s[i] == "\\"):
        t = s[last:i]
        if ('x' in t):
            count = 0
            times = 0
            for k in range(len(t) - 1, 0, -1):
                if (t[k] == 'x'):break
                count += int(t[k], 16) * (16 ** times)
                times += 1
        else:
            count = 0
            times = 0
            for k in range(len(t) - 1, 0, -1):
                if (t[k] == '\\'):break
                count += int(t[k]) * (10 ** times)
                times += 1
        print(chr(count), end='')

        last = i

# t = "\97\49\49\68\x4F\84\116\x68\97\x74\x44\x4F\x54\x6A\97\x76\x61\x35\x63\x72\97\x70\x41\84\x66\x6C\97\x72\x65\x44\65\x53\72\111\110\68\79\84\99\x6F\x6D"

# a11.that.java5crap@flare-on.com