## 0x0F. Python - Object-relational mapping
- This module utilizes MySQLdb to connect to a MySQL database and execute SQL queries
- Module SQLAlchemy will be used: An Object Relational Mapper (ORM)
---
	**Procedure to Install MySQLdb module version 2.0.x**
## Install MySQL 8.0 on Ubuntu 20.0.4 LTS
- $ sudo apt update
- $ sudo apt install mysql-server
- ...
- $ mysql --version
- mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
---
## Install MySQL module version 2.0.x
- $ sudo apt-get install python3-dev
- $ sudo apt-get install libmysqlclient-dev
- $ sudo apt-get install zlib1g-dev
- $ sudo pip3 install mysqlclient
- ...
- $ python3
- >>> import MySQLdb
- >>> MySQLdb.version_info 
- (2, 0, 3, 'final', 0)
---
## Install SQLAlchemy module version 1.4.x
- $ sudo pip3 install SQLAlchemy
- ...
- $ python3
- >>> import sqlalchemy
- >>> sqlalchemy.__version__ 
- '1.4.22'
