import subprocess
import argparse

def startproject():
	parse=argparse.ArgumentParser("description=Create python project")
	parse.add_argument("projectname",help="input your project name")
	parse.add_argument('-c','--clean',action='store_true',help='clean your projectname information')

	args=parse.parse_args()

	print args
	if args.clean:
		removeproject(args.projectname)
	else:
		createproject(args.projectname)

def createproject(projectname):

	curpath = subprocess.check_output(["pwd"]).replace('\n','')

	projectpath=curpath+"/"+projectname
	setup_file=projectpath+"/"+"setup.py"
	req_file=projectpath+"/"+"requirements.txt"
	readme_file=projectpath+"/"+"README.md"

	subprocess.call(["mkdir",projectpath])
	subprocess.call(["touch",setup_file])
	subprocess.call(["touch",req_file])
	subprocess.call(["touch",readme_file])

	packetspath=projectpath+"/"+projectname
	init_file=packetspath+"/"+"_init_.py"
	main_file=packetspath+"/"+"main.py"

	subprocess.call(["mkdir",packetspath])
	subprocess.call(["touch",init_file])
	subprocess.call(["touch",main_file])

	docspath=projectpath+"/"+"docs"
	subprocess.call(["mkdir",docspath])
	testpath=packetspath+"/"+"test"
	subprocess.call(["mkdir",testpath])


def removeproject(projectname):
	print("remove project")

	action=raw_input("Are you sure to remove this project?(y/n):")
	if action=="y" or action=="Y":
		subprocess.call(["rm","-rf",projectname])
	pass


if __name__ == '__main__':
	startproject()
