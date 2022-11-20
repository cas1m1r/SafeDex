import xml.etree.ElementTree as ET
import ctypes
import os

if __name__ == '__main__':
	data = ET.parse('wdac.xml')
	root = data.getroot()
	N = len(root)
	bad_drivers = []
	# File Rule List is in root[4]
	for rule in root[4].getchildren():
		rules = list(rule.items())
		driver_name = rules[1][1].split(' ')[0].split('\\')[0]
		driver_file = rules[2][1].split(' ')[0].split('\\')[0]
		if driver_name.find('.sys') > 0:
			bad_drivers.append(driver_name)
	# remove any duplicate entries
	bad_drivers = list(set(bad_drivers))
	# Now check which drivers are on system
	os.system('driverquery > drvs')
	drivers_present = open('drvs','r').read().split('\n')
	os.remove('drvs')
	for driver in drivers_present:
		name = f"{driver.split(' ')[0]}.sys"
		# print(f'{name} is malicious:\t{name in bad_drivers}')
		if name in bad_drivers:
			msg = u"[X] VULNERABLE DRIVER " +name+u" IS PRESENT"
			title = u"*** !!!!!!!!!!!!!!!!! SECURITY ALERT !!!!!!!!!!!!!!!!!!!!!!! ***"
			ctypes.windll.user32.MessageBoxW(None, msg, title, 0)
