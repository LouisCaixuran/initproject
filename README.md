# initproject
initial a python project


## install:
  $ python setup.py install 
  
## how to get help:
 '''Shell 
 $ initpro -h
  
usage: initpro [-h] [-c] projectname

Create python project

positional arguments:
  projectname  input your project name

optional arguments:
  -h, --help   show this help message and exit
  -c, --clean  clean your projectname information
  '''

 ## how to initial a new project called "abc":
 '''Shell
 $ initpro abc
 $ tree abc

abc
├── README.md
├── abc
│   ├── _init_.py
│   ├── main.py
│   └── test
├── docs
├── requirements.txt
└── setup.py

3 directories, 5 files

'''
  
