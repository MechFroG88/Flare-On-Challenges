f = open("dat_secret", "rb").read()

for i in f:
    print(hex(i),end = ',')

