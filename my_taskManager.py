import os
import time
import sys

class my_taskManager:

	def __init__(self):
		pass


	def getPID(self,process_name):
		self.processList_file = "process_list.txt"
		cmd = "tasklist" 
		processList_file_obj = os.popen(cmd)

		required_pid_list = []
		start = 0
		lines = processList_file_obj.readlines()
		
		for line in lines:
			if line.find("============") > -1:
				start = 1
				continue

			if start == 1:
				process_array = line.split()
				process_name_inList = process_array[0]
				process_id = process_array[1]
				if(process_name in process_name_inList.lower()):
					required_pid_list.append(process_id)

		return required_pid_list


	def killProcess(self,process_name):
		pid_list = self.getPID(process_name)
		final_cmd = "taskkill"
		for pid in pid_list:
			final_cmd += " /PID " + pid

		print(final_cmd)
		os.system(final_cmd)


def main():
	tm_obj = my_taskManager()
	
	# Getting PID for chrome
	pid_list = tm_obj.getPID("chrome")
	text = "\n".join(pid_list)
	print(text)

	# Killing Firefox
	# tm_obj.killProcess("firefox")


if __name__ == "__main__":
	main()
