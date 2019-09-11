while True:
	def name(name):
		while True:
			name=input("Enter Your Name : ")
			if (name == "" or name == "	"):
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
		return name		

	def fname(fname):
		while True:
			fname=input("Enter Your Father Name : ")
			if (fname == "" or fname == "	"):
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
		return fname	

	def mname(mname):
		while True:
			mname = str(input("Enter Your Mother Name : "))
			if (mname == "" or mname == "	"):
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
		return mname	

	def dob(dob):
		while True:
			dob = input("Enter Your Date Of Birth. e.g(dd/mm/yyyy) : ")
			if (len(dob) >10 or dob == "" or dob == "	"):
				print("Enter Correct Date of Birth...!!!")
				continue
			else:
				break
		return dob

	def univrstyname(univrstyname):
		while True:
			univrstyname = input("Enter Your University Name : ")
			if (univrstyname == "" or univrstyname == "	"):
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
		return univrstyname

	def subjctname(subjctname):
		while True:
			subjctname = input("Enter Your Subject Name : ")
			if (subjctname == "" or subjctname == "	"):
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
		return subjctname

	name = name(name)
	fname = fname(fname)
	mname = mname(mname)
	dob = dob(dob)
	univrstyname = univrstyname(univrstyname)
	subjctname = subjctname(subjctname)

	files={"name":name,"fname":fname,"mname":mname,"dob":dob,"univrstyname":univrstyname,"subjctname":subjctname}
	file = open(name +'.txt','w')
	file.write(str(files))
	file.close()
	print("Done....>>>>>>>>")


	entry = input("Press Y or Yes for continue: ").lower()
	if (entry == 'y' or entry == 'yes'):
		continue
	else:
		exit()
