from setuptools import setup, find_packages

setup(
	name="initproject",
	version="0.1",
	author="purkol",
	author_email="louiscaixuran@163.com",
	description="This is a tool to help initial a new python project",
	url="https://github.com/LouisCaixuran/initproject.git",
	packages=find_packages(),
	license="Aparch",
	platforms="Independant",

	entry_points={
		'console_scripts':[
			'initproject = initproject.initproject:startproject',
			]
	}
)