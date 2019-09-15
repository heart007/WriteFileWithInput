import datetime
import numpy as np
while True:
	def name(_str):
		while True:
			_name = input("Enter " + _str + " Name : ")
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
	_yName = name("Your").capitalize()
	_fName = name("Father").capitalize()
	_mName = name("Mother").capitalize()
	def dateofbirth():
		while True:
			_dob = input("Enter Your Date Of Birth. e.g(dd/mm/yyyy) : ")
			if (len(_dob) > 10 or _dob == ""):
				print("Enter Correct Date of Birth...!!!")
				continue
			else:
				if ('/' in _dob):	
					aa = '/'
					_dob2 = _dob.split(aa)
					if (len(_dob2[0]) == 2 and len(_dob2[1]) == 2 and len(_dob2[2]) == 4):
						try:
							dd_num=int(_dob2[0])
							dd_num1=int(_dob2[1])
							dd_num2=int(_dob2[2])
						except Exception as e:
							print("Enter Numeric Date of Birth...!!!")
							continue
					else:
						print("Enter Correct Date of Birth...!!!")
						continue
				elif('.' in _dob):
					aa = '.'
					_dob2 = _dob.split(aa)
					if (len(_dob2[0]) == 2 and len(_dob2[1]) == 2 and len(_dob2[2]) == 4):
						try:
							dd_num=int(_dob2[0])
							dd_num1=int(_dob2[1])
							dd_num2=int(_dob2[2])
						except Exception as e:
							print("Enter Numeric Date of Birth...!!!")
							continue
					else:
						print("Enter Correct Date of Birth...!!!")
						continue
				else:
					aa = '-'
					_dob2 = _dob.split(aa)
					if (len(_dob2[0]) == 2 and len(_dob2[1]) == 2 and len(_dob2[2]) == 4):
						try:
							dd_num=int(_dob2[0])
							dd_num1=int(_dob2[1])
							dd_num2=int(_dob2[2])
						except Exception as e:
							print("Enter Numeric Date of Birth...!!!")
							continue
					else:
						print("Enter Correct Date of Birth...!!!")
						continue
				return _dob
	dob=dateofbirth()
	def mob():
		while True:
			try:
				mob = int(input("Enter Your Mobile Number, i.g.(01xxxxxxxxx) : +880"))
				if (len(str(mob)) > 10 or len(str(mob)) < 10):
					print("Input Correct Mobile Number...!!!")
					continue
				else:
					return mob
			except Exception as e:
				print("Input Correct Mobile Number...!!!")
				continue
	mob = mob()
	_uName = name("University").capitalize()
	_sName = name("Subject").capitalize()
	files = {"name": _yName, "fname": _fName, "mname": _mName, "mob": mob, "dob": dob, "univrstyname": _uName, "subjctname": _sName}
	file = open(str(_yName) + '.txt', 'w')
	file.write(str(files))
	file.close()
	print("Done...............>>>>>>>>>>>>>>>")
	entry = input("Press Y or Yes for continue:(y/n) ").lower()
	if (entry == 'y' or entry == 'yes'):
		continue
	else:
		exit()