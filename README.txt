[Requirements]
-python
-flask module for python
-flask_mysqldb for python
-MySql server (community edition)

[Instructions]
1.Install python 3.74 (64bit) along with pip
2.add python to windows/Linux/Mac path(environment variables)
3.install flask module with the following command: "pip install flask" in the command prompt
4.install flask_mysqldb with the following command: "pip install flask_mysqldb" in the command prompt
5.Download and install MySql server community edition from the link "https://dev.mysql.com/downloads/windows/installer/8.0.html"
	-install in deafault directory
	-choose the root user password as "password"
6.Add the path for MySql in the environment variables (windows/Linux/Mac)
7.Create a database named udaan in MySql and use it
8.Create the following tables in MySql
	-assets(assetID varchar(10),description varchar(100))
	-tasks(taskId varchar(10),assetId varchar(10),freq int(50))
	-admin(name varchar(100),password varchar(100))
	-workers(workerId varchar(10),name varchar(50),skillset(100))
	-allocatetask(assetId varchar(10),taskId varchar(10),workerId varchar(10),toa datetime,ttbpb datetime)
	**to create tables for above use "Create table" command along with any of the above commands
9.Run the main_server.py
10.Now the server is ready to accepts requests for all the API's mentioned in the question

https://github.com/dibyenshu/udaan
check the above repository readme for further info