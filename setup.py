import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='MDroidPythonConfig',  
     version='0.1',
     scripts=['mdroidconfig'] ,
     author="Quinn Casey",
     author_email="quinn@quinncasey.com",
     description="Reads from MDroid configuration file, used across several Python scripts in the MDroid suite.",
     url="https://github.com/MrDoctorKovacic/MDroid-PythonConfig",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )