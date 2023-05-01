# robotFramework
This is to execute automated testing using robot framework
To start using robot framework, verify if system has installed the following packages:
Type:

pip list 

as shown below:

![image](https://user-images.githubusercontent.com/12807393/235483581-0794039d-6435-47ed-a7af-14e36e629385.png)

In case packages below are not installed please type the commands below:

# to verify pip it's installed type:

pip --version
C:\Users\riotb>pip --version
pip 23.0.1 from C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\lib\site-packages\pip (python 3.10)

# to install robot Robot Framework
pip install robotframework

# to verify is properly installed:

C:\Users\riotb>robot --version

Robot Framework 6.0.2 (Python 3.10.11 on win32)
# to install  robotframework-databaselibrary:

pip install robotframework-databaselibrary

# to install  pymssql:

pip install pymssql

# Installing SQL server developer edition:

go to:

https://www.microsoft.com/en-us/sql-server/sql-server-downloads

Once installed, follow the wizzard

Important configurations:

look for SQL server configuration manager:

![image](https://user-images.githubusercontent.com/12807393/235489389-dde946ce-8e2f-4518-b3a0-c090e377a0da.png)

Look for the pipes are enabled:

![image](https://user-images.githubusercontent.com/12807393/235489997-e4a93751-07d0-444d-97d2-a9c31dc45d52.png)

TCP is enabled


![image](https://user-images.githubusercontent.com/12807393/235490278-5ca815f3-e63a-4dfb-8a93-33cdb9408236.png)

# Getting the Port and Host Name:

to get the host name:

Select Host_name()

![image](https://user-images.githubusercontent.com/12807393/235496425-500c328f-63f3-4051-bbd2-287dc02185ab.png)


to get the port:

USE MASTER
GO
xp_readerrorlog 0, 1, N'Server is listening on'
GO









