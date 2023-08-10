import os
import json
import re

print("(-h for help) (exit to quit)")

Config = open("config.json", "r+")
file = json.load(Config)



def include_path():
	include_userInp = input("include path: ")

	file["include_path"] = include_userInp
	print(file["include_path"])
	
	Config.seek(0)
	json.dump(file, Config)
	Config.truncate()

def lib_path():
	lib_userInp = input("lib path: ")

	file["lib_path"] = lib_userInp
	print(file["lib_path"])
	
	Config.seek(0)
	json.dump(file, Config)
	Config.truncate()

def rml():
	#REMOVE linkedlib from list
	
	delIntput = input("remove argument from list : ")
	file["linker_args"].remove(f"-l{delIntput}")

	
	Config.seek(0)
	json.dump(file, Config)
	Config.truncate()

def linker_aguments():
	print("Use -rml to remove argument from a list")
	lib_userInp = input("linker args: ")

	file["linker_args"].append((f"-l{lib_userInp}"))
	print(file["linker_args"])



def file_path():
	file_userInp = input("main file path: ")

	file["file_path"] = file_userInp
	print(file["file_path"])
	
	Config.seek(0)
	json.dump(file, Config)
	Config.truncate()

def linker():
	global cppOutputFilename
	global cppFile
	cppFile = input("cpp file do not add file extension: ")
	#file
	os.system(f'cmd /k "g++ -I"{file["include_path"]}" -c "{file["file_path"]}\\{cppFile}" " ')


	a = str(file["linker_args"])
	args = a.translate({ ord(i): None for i in "[],'"} )
	print(args)

	os.system(f'cmd /k "g++ "{file["file_path"]}\\{cppFile}.o" -o {cppFile} "-L{file["lib_path"]}" {args}"')


		
def main():
	selection = input(": ")

	if selection == "-h":
		print(" -c to compile file \n -r to run \n -s to compile and run \n -id add include directory \n -ld add lib directory \n -m linker \n -f cpp file path \n -rml to remove linked args from a list")

	elif selection == "-id":
		include_path()

	elif selection == "-ld":
		lib_path()

	elif selection == "-i":
		linker_arguments()

	elif selection == "-f":
		file_path()

	elif selection == "-c":
		#linker()
		linker()

	elif selection == "-rml":
		rml()

	elif selection == "exit":
		os.close(0)
		exit()

	else:
		print("Invalid command")


while True:
	main()
