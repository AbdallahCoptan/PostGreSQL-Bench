# Installing **PostGreSQL** Data Base Server #

**PostGreSQL: The world's most advanced open source databse**

**PostgreSQL** is a powerful, open source object-relational database system. It has more than 15 years of active development and a proven architecture that has earned it a strong reputation for reliability, data integrity, and correctness. It runs on all major operating systems, including Linux, UNIX (AIX, BSD, HP-UX, SGI IRIX, macOS, Solaris, Tru64), and Windows. It is fully ACID compliant, has full support for foreign keys, joins, views, triggers, and stored procedures (in multiple languages). It includes most SQL:2008 data types, including INTEGER, NUMERIC, BOOLEAN, CHAR, VARCHAR, DATE, INTERVAL, and TIMESTAMP. It also supports storage of binary large objects, including pictures, sounds, or video. It has native programming interfaces for C/C++, Java, .Net, Perl, Python, Ruby, Tcl, ODBC, among others, read the [documentations and manuals](https://www.postgresql.org/docs/manuals/) of the different releases of [PostgreSQL](https://www.postgresql.org/)

An enterprise class database, PostgreSQL boasts sophisticated features such as Multi-Version Concurrency Control (MVCC), point in time recovery, tablespaces, asynchronous replication, nested transactions (savepoints), online/hot backups, a sophisticated query planner/optimizer, and write ahead logging for fault tolerance. It supports international character sets, multibyte character encodings, Unicode, and it is locale-aware for sorting, case-sensitivity, and formatting. It is highly scalable both in the sheer quantity of data it can manage and in the number of concurrent users it can accommodate. There are active PostgreSQL systems in production environments that manage in excess of 4 terabytes of data. Some general PostgreSQL limits are included in the table below. 

Here are some important numbers about PostgreSQL:

|   Limit                  |     Value                           |
| --------------------     | ----------------------------------- |
|Maximum Database Size     | Unlimited                           |
|Maximum Table Size        | 32 TB                               |
|Maximum Row Size          | 1.6 TB                              |
|Maximum Field Size        | 1 GB                                |
|Maximum Rows per Table    | Unlimited                           |
|Maximum Columns per Table | 250 - 1600 depending on column types|
|Maximum Indexes per Table |Unlimited                            |

For more features about this data base read the [PostgreSQL](https://www.postgresql.org/about/) Featureful and Standards Compliant.


## Installing PostgreSQL Server ##

Befor installing postgresql you need to make update and upgrade, as following:

		$ sudo apt-get update
		$ sudo apt-get upgrade


After updating the system, it's time to install postgresql from the Internet by through the command line.

### INSTALLING PostgreSQL in ubuntu command line ###
You can proceed to install the PostgreSQL by the following commands:

		$ sudo apt-get install postgresql postgresql-contrib

 
### WORKING with PostgreSQL Server ###
By default, PostgreSQL-server is started after installation. You can check using the service command :

		$ sudo service postgresql status
		9.3/main (port 5432): online
		
You can also check using the netstat command whether PostgreSQL-server is already listening on a port or not.

		$ sudo netstat -naptu | grep LISTEN
		tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      1123/mysqld     
		tcp        0      0 0.0.0.0:6379            0.0.0.0:*               LISTEN      1209/redis-server 0
		tcp        0      0 0.0.0.0:11211           0.0.0.0:*               LISTEN      1197/memcached  
		tcp        0      0 0.0.0.0:52715           0.0.0.0:*               LISTEN      721/rpc.statd   
		tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN      619/rpcbind     
		tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1793/sshd       
		tcp        0      0 127.0.0.1:5432          0.0.0.0:*               LISTEN      5472/postgres   

From output above we learned that PostgreSQL server is already listening on port **5432** and bind to **localhost or 127.0.0.1**.

#### Start Dealing with PostgreSQL Server  
By default, Postgres uses a concept called "roles" to aid in authentication and authorization. These are, in some ways, similar to regular Unix-style accounts, but Postgres does not distinguish between users and groups and instead prefers the more flexible term "role".

Upon installation Postgres is set up to use "ident" authentication, meaning that it associates Postgres roles with a matching Unix/Linux system account. If a Postgres role exists, it can be signed in by logging into the associated Linux system account.

The installation procedure created a user account called **postgres** that is associated with the default Postgres role. In order to use Postgres, we'll need to log into that account. You can do that by typing:

		$ sudo -i -u postgres


You will be given a shell prompt for the postgres user. Then you can get the PostgreSQL server prompt immediately by typing: 

		$ psql 


or(do the two steps in one in the main **ubuntu prompt**) by: 

		$ sudo -u postgres psql postgres
		psql (9.3.16)
		Type "help" for help.

		postgres=# 

you can quit by **\q** and **\list** to see all the databases you have:
		
		postgres=# \list
					    			List of databases
		   Name    |  Owner   | Encoding  | Collate | Ctype |   Access privileges   
		-----------+----------+-----------+---------+-------+-----------------------
		 abdo      | postgres | SQL_ASCII | C       | C     | 
		 ali       | abdo     | SQL_ASCII | C       | C     | 
		 amarokdb  | postgres | SQL_ASCII | C       | C     | 
		 mydb      | postgres | SQL_ASCII | C       | C     | 
		 postgres  | postgres | SQL_ASCII | C       | C     | 
		 template0 | postgres | SQL_ASCII | C       | C     | =c/postgres + postgres=CTc/postgres
		 template1 | postgres | SQL_ASCII | C       | C     | =c/postgres + postgres=CTc/postgres
		(7 rows)

 


#### Popup problem after installation 

After installing PostgreSQL server and you try to check if it works or not by issuing the following command:

		$ sudo -u postgres psql postgres
		psql: could not connect to server: No such file or directory
		Is the server running locally and accepting
		connections on Unix domain socket "/var/run/postgresql/.s.PGSQL.5432"?


That is mean that the postgresql db need a **cluster** this can be done by the following command:

		$ sudo pg_craetecluster 9.3 main --start
		Creating new cluster 9.3/main ...
		  config /etc/postgresql/9.3/main
		  data   /var/lib/postgresql/9.3/main
		  locale C
		  port   5432

and then restart the  PostgreSQL server by the follwing command: 

		$ sudo service Postgresql restart
		* Restarting PostgreSQL 9.3 database server 

#### Create a New Role
From the **postgres** Linux account, you have the ability to log into the database system. However, we're also going to demonstrate how to create additional roles. The **postgres** Linux account, being associated with the Postgres administrative role, has access to some utilities to create users and databases.

We can create a new role by typing:

		$ createuser --interactive


or from the ubuntu termenal: 

		$ sudo -u postgres createuser --interactive
		Enter name of role to add: bro
		Shall the new role be a superuser? (y/n) y

**Note:** The role in the PostgreSQL db server is like the user of the database or the owner of the data base which like the super user **postgres**

#### Create a New Database
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

		 

**All commandes in a nutshell !!**
		
		$ sudo -u postgres createuser -D -A -P myuser
		$ sudo -u postgres createdb -O myuser mydb
		$ sudo -u postgres psql mydb
		
The first command line creates the user with no database creation rights (-D) with no add user rights -A) and will prompt you for entering a password (-P). The second command line create the database **'mydb with 'myuser'** as owner. The last one connect you to the database terminal **ali=#**, to verify on which database you are connected and with with which user you are connnected by the commend **/conninfo** in the database prompt: 

		$ sudo -u postgres psql ali
		psql (9.3.16)
		Type "help" for help.

		ali=# \conninfo
		You are connected to database "ali" as user "postgres" via socket in "/var/run/postgresql" at port "5432".

****For more informations about the installation of the PostGreSQL server, please check the links,**** [PostgreSQL on Ubuntu](https://help.ubuntu.com/community/PostgreSQL), also how to deal with the database such as create tables, insert and update date check the [link](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-14-04). 



### Configuring the PostGreSQL Server ###

To configure the PostGreSQL Server by updating the files in the directory: **/etc/postgresql/9.3/main/** 

In this directory you will find the following: 

File name | purpose  
----------|---------------
postgresql.conf |to configure the server generally
pg_ident.conf |to configure the user authentications
pg_hba.conf | to configure the users allow to access the server remotely 
start.conf | to configure the server starting condiguration
pg_ctl | to configure the server control options
data file | located in **/var/lib/postgresql/9.3/main/** to hold the server data 

--> PostGreSQL Server configuration is located in the **/etc/postgresql/9.3/main/postgresql.conf** file. In this tutorial we'll change one PostGreSQL configuration directive so that it will listen to all network interfaces instead of only on localhost. This is useful if you have a dedicated PostGreSQL server and you're connecting from outside clients, such as an application server. Open **/etc/postgresql/9.3/main/postgresql.conf**  in your favourite editor and alter the **listen_addresses** as below:

		$ listen_addresses = 'localhost'

Change the line above with: 

		$ listen_addresses = '*'

to listen on all network interfaces. See the docs for listen_addresses for other options. 

Then, restart PostGreSQL service by: 

		$ sudo service postgresql restart

Now check where PostGreSQL is listening ;

		$ sudo netstat -naptu | grep LISTEN
		tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      1123/mysqld     
		tcp        0      0 0.0.0.0:6379            0.0.0.0:*               LISTEN      1209/redis-server 0
		tcp        0      0 0.0.0.0:11211           0.0.0.0:*               LISTEN      1197/memcached  
		tcp        0      0 0.0.0.0:52715           0.0.0.0:*               LISTEN      721/rpc.statd   
		tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN      619/rpcbind     
		tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1793/sshd       
		tcp        0      0 0.0.0.0:5432            0.0.0.0:*               LISTEN      8311/postgres

We see above that redis is listening on all interfaces on port **5432 (0.0.0.0:5432)**.

There are a lot more configuration directive on **postgresql.conf** file. You can read the comment above each directive to see how you can customize postgresql configuration.


--> To manage users, you first have to edit **/etc/postgresql/current/main/pg_hba.conf** and modify the default configuration which is very locked down and secure. For example, if you want postgres to manage its own users (not linked with system users), you will add the following line: 

		8<-------------------------------------------
		# TYPE  DATABASE    USER        IP-ADDRESS        IP-MASK           METHOD
		 host    all         all         10.0.0.0       255.255.255.0        md5
		8<-------------------------------------------
[or]

		8<-------------------------------------------
		# TYPE  DATABASE    USER        IP-ADDRESS         METHOD
		 host    all         all        10.0.0.0/24        trust
		8<-------------------------------------------


Which means that on your local network **(10.0.0.0/24 - replace with your own local network !)**, postgres users can connect through the network to the database providing a classical couple user / password. 

#### Finally, restarting the server

You should restart the PostgreSQL service to initialize the new configuration. From a terminal prompt enter the following to restart PostgreSQL: (there are many lines could do the restart)

		$ sudo systemctl restart postgresql.service  #[or]
		$ sudo service postgresql restart  #[or]
		
Or After configuring the networking / users you may need to reload the server, here is a suggested command to do so.

		$ sudo /etc/init.d/postgresql reload

Some settings changes in postgresql.conf require a full restart, which will terminate active connections and abort uncommitted transactions: 

		$ sudo /etc/init.d/postgresql restart



### Installing PostGreSQL Client ###

If you only wish to connect to an external PostgreSQL server, do not install the main PostgreSQL package, but install the PostgreSQL client package instead. To do this, use the following command:

		$ sudo apt-get install postgresql-client

By the previous command you already installed the postgreSQL client on the client machine. Remember to update the postgreSQL server configutrations like: 

**1)** The listening address should be from outside the server or from everywhere this in the **postgresql.conf** file (see the previous section).

**2)** Manage the users and clients in the file **pg_hba.conf** by adding the addresses and netmasks and also the method of authentication. The database and users should be mentioned or let them for **all** which means this client will access all the users and databases (see the previous section).

**3)** Do not forget to **restart** the postGreSQL server after doing any changes in the previous files (onfiguration files) also, (see the previous section how to restart the server !!) 

The last thing you need before starting the connection from the client to the database server, is the passwored for the postgres user. You will need it to connect remotely !!

If you don't know it, just alter the password in the server side by the alter command. You can run the following SQL command at the psql prompt to configure the password for the user postgres (on the server itself).
 
		$ sudo -u postgres psql postgres
		psql (9.3.16)
		Type "help" for help.

		postgres=# ALTER USER postgres with encrypted password 'your_password';
		ALTER ROLE
		postgres=#
		 

You will need this password to connect from the client to the server remotly.

#### Connecting from Client to the PostGreSQL Server

To connect from the client machine to the postgresql server you can use this command (-W to force the password(this should be automatic)and small -w never ask for password):

		$ psql -h [server-ip] -U postgres -W 

If you want to connect on a spacific database or user(role), with the same command by adding the database name:

		$ psql -h [server-ip] -U dbuser -d dbname


You can check all the options of the **psql** command by issuing the help command:

		$ psql --help


For example, if the server ip is **10.10.1.200/24** and you already add this network in the **pg_hba.conf** and did all the configuration for the server. You can connet as following from the client side (you will asked to enter the password) :

		$ psql -h 10.10.1.200 -U postgres -d qui 
		Password for user postgres: 
		psql (9.3.16)
		SSL connection (cipher: DHE-RSA-AES256-GCM-SHA384, bits: 256)
		Type "help" for help.

		qui=# 

If you issue the **\list** command you can see all the databases hosted on the server !!


#### Note
For more information about the configuration, and connecting remotely to PostGreSQL server, please follow the links [PostGreSQL on Ubuntu 2](https://help.ubuntu.com/lts/serverguide/postgresql.html) and [cyberciti](https://www.cyberciti.biz/tips/postgres-allow-remote-access-tcp-connection.html).





