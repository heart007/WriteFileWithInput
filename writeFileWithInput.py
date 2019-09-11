def name():
	while True:
		name=input("Enter Your Name : ")
		if (name == ""):
			print("Enter Your Name...!!!")
			continue
		else:
			try:
				name != int(name)
				print("Enter Your Name...!!!")
				continue
			except Exception as e:
				break 
			pass
name()
def fname():
	while True:
		fname=input("Enter Your Father Name : ")
		if (fname == ""):
			print("Enter Your Father Name...!!!")
			continue
		else:
			try:
				fname != int(fname)
				print("Enter Your Father Name...!!!")
				continue
			except Exception as e:
				break 
			pass
fname()
def mname():
	while True:
		mname = str(input("Enter Your Mother Name : "))
		if (mname == ""):
			print("Enter Your Mother Name...!!!")
			continue
		else:
			try:
				mname != int(mname)
				print("Enter Your Mother Name...!!!")
				continue
			except Exception as e:
				break 
			pass
mname()	
def dob():
	while True:
		dob = input("Enter Your Date Of Birth. e.g(dd/mm/yyyy) : ")
		if (len(dob) >10 or dob == ""):
			print("Enter Correct Date of Birth...!!!")
			continue
		else:
			break
dob()
def univrstyname():
	while True:
		univrstyname = input("Enter Your University Name : ")
		if (univrstyname == ""):
			print("Enter Your University Name...!!!")
			continue
		else:
			try:
				univrstyname != int(univrstyname)
				print("Enter Your University Name...!!!")
				continue
			except Exception as e:
				break 
			pass
univrstyname()
def subjctname():
	while True:
		subjctname = input("Enter Your Subject Name : ")
		if (subjctname == ""):
			print("Enter Your Subject Name...!!!")
			continue
		else:
			try:
				subjctname != int(subjctname)
				print("Enter Your Subject Name...!!!")
				continue
			except Exception as e:
				break 
			pass
subjctname()

files={"name":name,"fname":fname,"mname":mname,"dob":dob,"univrstyname":univrstyname,"subjctname":subjctname}
file = open("name" +'.txt','w')
file.write(str(files))
file.close()

while True:
	entry = input("Press Y or Yes for continue: ").lower()
	if (entry == 'y' or entry == 'yes'):
		name()
		continue
	else:
		exit()
