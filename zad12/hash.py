import hashlib

m1=hashlib.sha256()
m2=hashlib.sha256()

with open("obrazek2.bmp","rb") as f:
    img1=f.read()

with open("obrazek3.bmp","rb") as f:
    img2=f.read()

m1.update(img1)
m2.update(img2)

md51 = hashlib.md5(img1)
md52 = hashlib.md5(img2)

print("SHA-256:")
print("Orginał:", m1.hexdigest())
print("Zmieniony:",m2.hexdigest())

print(len(img1))

for i in range(0,len(img1)):
    if img1[i] != img2[i]:
        print(img1[i],img2[i])

print("MD5:")
print(md51.hexdigest())
print(md52.hexdigest())