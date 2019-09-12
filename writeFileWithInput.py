import datetime 
import numpy as np
while True:
	def namee(_str):
		while True:
			_name = input("Enter "+_str+" Name : ")
			if (_name == ""):
				print("Enter Proper Requrements...!!!")
				continue
			else:
				try:
					_name != int(_name)
					print("Enter Proper Requrements...!!!")
					continue
				except Exception as e:
					return _name
					break

	_yName = namee("Your")
	_fName = namee("Father")
	_mName = namee("Mother")

	# def dob(_dob):
	# 	while True:
	# 		_dob = input("Enter Your Date Of Birth. e.g(dd/mm/yyyy) : ")
	# 		if (len(str(_dob)) >10 or _dob == "" or _dob == "	"):
	# 			print("Enter Correct Date of Birth...!!!")
	# 			continue
	# 		else:
	# 			_dob = _dob.split('/') 
	# 			if (len(str(_dob[0]))==2 or len(str(_dob[0]))==1):
	# 				continue
	# 			elif (len(str(_dob[1]))==2 or len(str(_dob[1]))==2):
	# 				continue
	# 			elif (len(str(_dob[2]))==4):
	# 				continue
	# 			else:
	# 				print("Enter Correct Date of Birth...!!!")
	# 			return _dob

	def mob(mob):
		while True:
			try:
				mob = int(input("Enter Your Mobile Number, i.g.(01xxxxxxxxx) : +88"))
				if (len(str(mob)) > 12 or len(str(mob)) < 10):
					print("Input Correct Mobile Number...!!!")
					continue
				else:
					return mob
			except Exception as e:
				print("Input Correct Mobile Number...!!!")
				continue
	# _dob = dob(_dob)
	mob = mob(mob)
	_uName = namee("University")
	_sName = namee("Subject")

	# def name(name):
	# 	while True:
	# 		name=input("Enter Your Name : ")
	# 		if (name == "" or name == "	"):
	# 			print("Enter Your Name...!!!")
	# 			continue
	# 		else:
	# 			try:
	# 				name != int(name)
	# 				print("Enter Your Name...!!!")
	# 				continue
	# 			except Exception as e:
	# 				break 
	# 			pass
	# 	return name		

	# def fname(fname):
	# 	while True:
	# 		fname=input("Enter Your Father Name : ")
	# 		if (fname == "" or fname == "	"):
	# 			print("Enter Your Father Name...!!!")
	# 			continue
	# 		else:
	# 			try:
	# 				fname != int(fname)
	# 				print("Enter Your Father Name...!!!")
	# 				continue
	# 			except Exception as e:
	# 				break 
	# 			pass
	# 	return fname	

	# def mname(mname):
	# 	while True:
	# 		mname = str(input("Enter Your Mother Name : "))
	# 		if (mname == "" or mname == "	"):
	# 			print("Enter Your Mother Name...!!!")
	# 			continue
	# 		else:
	# 			try:
	# 				mname != int(mname)
	# 				print("Enter Your Mother Name...!!!")
	# 				continue
	# 			except Exception as e:
	# 				break 
	# 			pass
	# 	return mname	

	# def dob(dob):
	# 	while True:
	# 		dob = input("Enter Your Date Of Birth. e.g(dd/mm/yyyy) : ")
	# 		if (len(dob) >10 or dob == "" or dob == "	"):
	# 			print("Enter Correct Date of Birth...!!!")
	# 			continue
	# 		else:
	# 			break
	# 	return dob

	# def univrstyname(univrstyname):
	# 	while True:
	# 		univrstyname = input("Enter Your University Name : ")
	# 		if (univrstyname == "" or univrstyname == "	"):
	# 			print("Enter Your University Name...!!!")
	# 			continue
	# 		else:
	# 			try:
	# 				univrstyname != int(univrstyname)
	# 				print("Enter Your University Name...!!!")
	# 				continue
	# 			except Exception as e:
	# 				break 
	# 			pass
	# 	return univrstyname

	# def subjctname(subjctname):
	# 	while True:
	# 		subjctname = input("Enter Your Subject Name : ")
	# 		if (subjctname == "" or subjctname == "	"):
	# 			print("Enter Your Subject Name...!!!")
	# 			continue
	# 		else:
	# 			try:
	# 				subjctname != int(subjctname)
	# 				print("Enter Your Subject Name...!!!")
	# 				continue
	# 			except Exception as e:
	# 				break 
	# 			pass
	# 	return subjctname

	# name = namee(_yName)
	# fname = namee(_fName)
	# mname = namee(_mName)
	# uname = namee(_uName)
	# sname = namee(_sName)
	# dob = dob(dob)

	files={"name":_yName,"fname":_fName,"mname":_mName,"mob":mob,"univrstyname":_uName,"subjctname":_sName}
	file = open(str(_yName) +'.txt','w')
	file.write(str(files))
	file.close()
	print("Done......>>>>>>>>")

	entry = input("Press Y or Yes for continue: ").lower()
	if (entry == 'y' or entry == 'yes'):
		continue
	else:
		exit()
