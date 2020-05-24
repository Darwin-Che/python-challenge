
f1 = open("evil2.gfx",'rb').read()
for i in range(5):
	open(str(i)+".jpg", 'wb').write(f1[i::5])
