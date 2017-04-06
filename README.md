# Benchmarking PostgreSQL Server by using PGBENCH Utility #

In this repository, we show every thing about `PostgreSQL` server and how to install it and it's clients. We show also how to benchmark the server with many tools and specially by using the `pgbench` utility. We provide a python script which run the benechmark for 100 times from a remote client or locally. 


## Prerequisites ##
To use our tool, you need to install the following :

- PostgreSQL Server
- Make a database for the test
- Install pgbench utility 


### Install PostgreSQL Server ###

You can proceed to install the PostgreSQL by the following commands:
		
		$ sudo apt-get install postgresql postgresql-contrib

**NOTE:** 

There are many details for the installation, and to configure the server to follow look at [postgresql](https://github.com/AbdallahCoptan/PostGreSQL-Bench/blob/master/postgreSQL-Server.md).

### Create A database for the test ###

You can create the appropriate database by simply calling this command:

		$ sudo -u postgres createdb -O [dbOwner] [dbName]

Then you can connect to this database by the follwoing command: 

		$ sudo -u postgres psql [dbName]

for example connect to dbName = ali :

		$ sudo -u postgres psql ali
		psql (9.3.16)
		Type "help" for help.

		ali=# 

for giving password for a user (owner) by the following:

		$ sudo -u postgres psql
		psql (9.3.16)
		Type "help" for help.

		postgres=# \password bro
		Enter new password: 
		Enter it again: 
		postgres=# \q



### Install pgbench utility ###

By default, once you installed the PostgreSQL server, you have the pgbench utility installed already and you can test your server but locally. If you want to test (*benchmark*) the server remotly (*this is the desired benchmarking for the PostgreSQL database server*) from a postgresql client.   

You can install the **pgbench** utility on the client machine by the following command: 


		$ sudo apt-get install postgresql-contrib 

After installing the utitity, you can now check all the options in the tool by asking for the help, wherever in the **postgres#** terminal (you can now in the client login to it by `$ sudo -i -u postgres`) or in the sudo terminal by:

		$ pgbench -? [--help]

**NOTE:** 

There are many details for the installation, and to use the pgbench to follow look at [pgbench](https://github.com/AbdallahCoptan/PostGreSQL-Bench/blob/master/Pgbench.md).


## Getting Started ##

1. Clone the repository:

With git installed, clone this repository, and cd into this folder:
		
		$ git clone https://github.com/AbdallahCoptan/PostGreSQL-Bench
		$ cd PostGreSQL-Bench


2. Using the pgbench and our python script:

With python installed, verify that the server is running and everything is fine, just call the script by `python` command:

		$ python PostGreSQL.py


**Notes:**

1. Do not forget to configure the postgreSQL server ip and port, and also change them in the python script.
2. The script itself will initialize the test in the database `ali`, if you want to change the name, do not forget to change it in the script.
3. For the other parameters of initialization like `-s`,`-F` you shoud change them in the script and also the rest of the parameters. 
4. Do not forget to read more about benchmarking in the presenetation and the links in the repository.
