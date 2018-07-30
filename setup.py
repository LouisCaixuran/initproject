from setuptools import setup, find_packages

setup(
	name="initpro",
	version="0.2.2",
	author="purkol",
	author_email="louiscaixuran@163.com",
	description="This is a tool to help initial a new python project",
	url="https://github.com/LouisCaixuran/initproject.git",
	packages=find_packages(),
	license="Aparch",
	platforms="Independant",
	
	package_data={
		'initpro':['data/*.*'],
	},

	entry_points={
		'console_scripts':[
			'initpro = initpro.initpro:startproject',
			]

	}
)