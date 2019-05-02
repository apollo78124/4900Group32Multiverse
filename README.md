# 4900Group32Multiverse

###Deploy Local Dockerized MySQL Server###
#1. Install Docker
#2. Create the docker container named mysqld on CMD
#	Run this command inside /mvjserver/
#	'''docker run --restart always --name mysqld -p 3308:3308 -v $(pwd)/data/var/lib/mysql -e MYSQL_ROOT_PASSWORD=toor  -d mysql/mysql-server:5.7.9'''
#	MySQL credentials: 
#		username: root
#		password: toor
#		port: 3308 (changed because 3306 is too general)
#3. Check container name and id 
#	'''docker ps'''
#4. Run shell inside the docker container
#	docker exec -it <container name> /bin/bash
#	'''docker exec -it mysqld /bin/bash'''
#5. Run mysql inside the docker container
#	'''mysql -u root -p'''
#6. Run the initial SQL queries stored inside the /mvjserver/install.sql and /mvjserver/master.sql
	
