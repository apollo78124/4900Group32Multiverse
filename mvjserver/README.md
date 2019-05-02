# Multiverse MMO server deployment scripts

The dokku deployment is built base on the server installation [instructions](http://wiki.apps.magnetar.net/index.php?title=Installing_the_Servers_on_Linux) on Multiverse Platform Wiki. Checkout the [wiki](http://mvwiki.magnetar.net) for more information on the game.

## Create database tables using mysql docker container.
The project utilizes the official mysql repos at https://hub.docker.com/r/mysql/mysql-server/  
Here is some quick tips to set up the tabls using the exsiting table creation scripts [install.sql](install.sql) and [master.sql](master.sql).

Run a mysql 5.7.9 database container named 'mysqld' in the background, map data directory, set password.  
```docker run --restart always --name mysqld -p 3306:3306 -v $(pwd)/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret  -d mysql/mysql-server:5.7.9```  
Port mapping '-p' option could be omitted, if mysql database is just used in the same network not crossing the machine boundary. This might be useful if you already have an sql instance running in the host machine.  

Access the mysql cli client in the container.  
```docker run -v $(pwd):/my --link mysqld --rm -it mysql/mysql-server sh -c 'exec mysql -h"$MYSQLD_PORT_3306_TCP_ADDR" -uroot -p"$MYSQLD_ENV_MYSQL_ROOT_PASSWORD"'```

Execute the sql script in current directory named install.sql  
```docker run -v $(pwd):/my --link mysqld --rm -it mysql sh -c 'exec mysql -h"$MYSQLD_PORT_3306_TCP_ADDR" -u root -p"$MYSQLD_ENV_MYSQL_ROOT_PASSWORD" < /my/install.sql'```

## Run directly from docker without dokku
If one wants to run the container directly from docker. Build the container with   
```docker builkd -t . [container name]```   
then run the container with the following options to address port mapping.  

*#Specify link to mysql database container*  
--link mysqld  
*#Specify TCP and UDP ports required for server-client communications.*  
-p 943:943 -p 4505:4505 -p 9005:4505 -p 4510:4510 -p 5040:4510  
-p 4520:4520 -p 5050:4520 -p 5040:4510/udp -p 5050:4520/udp -p 9010:9010/udp  

Enter  
```  
docker run -d --link mysql -p 943:943 -p 4505:4505 -p 9005:4505 -p 4510:4510 -p 5040:4510
-p 4520:4520 -p 5050:4520 -p 5040:4510/udp -p 5050:4520/udp -p 9010:9010/udp
```  

## Disable zero-Downtime check of DOKKU
Since multiverse server is a worker process uses many non-standard ports. Dokku build would onny work by skipping the 'Zero-Downtime' check.

http://dokku.viewdocs.io/dokku~v0.6.5/deployment/zero-downtime-deploys/  
https://github.com/dokku/dokku/issues/2871

PolicyFile.xml and PolicyServer.exe were made for working with Silverlight.

## Start script
'start.sh' starts the server. It first runs SED to search and replace several properties in multiverse config file , then launch the master server and multiverse world server. Upon server successfully lanuched, you should see console output 'DONE INITIALIZING, you can log in now'

## Login Web Interface.  
The legacy C# .NET client uses web page login form to capture user credential. The HTML files could be found at *server/website/login* folder. These files are not required for webgl client. To maintain backward compatibility, we just host these files on a separated directory served by nginx via http://mvlogin.magnetar.net/login/login.jsp. The url is specified as *login_url* parameter for the .net client  

```--login_url http://mvlogin.magnetar.net/login/login.jsp```

## Script for local test and debug.
The following scripts are made for testing and debugging "docker build -t" on the server, and not utilized in the dokku deployment.  
build.sh  
clean.sh  
mvbash.sh  
mvexec.sh  

ports.sh and rmports.sh are scripts made for testing abd debugging several port redirectings when the docker build is executing without dokku involved.

## Game Client  
Find out more about legacy client at [CLIENT.md](CLIENT.md)