#!/bin/bash

#echo "Waiting for mysql"
#until mysql -h"$MYSQLD_PORT_3306_TCP_ADDR" -uroot -p"$MYSQLD_ENV_MYSQL_ROOT_PASSWORD" &> /dev/null
#do
#  printf "."
#  sleep 1
#done
#while ! mysqladmin ping -h"$MYSQLD_PORT_3306_TCP_ADDR" --silent; do
#    printf "."
#    sleep 1
#done
#echo -e "\nmysql ready"

dbhost_mv=multiverse.db_hostname
dbpass_mv=multiverse.db_password
jdbc_mv=multiverse.jdbcJarPath
mastertcp=4505
masterrdp=9010
worldmgr=4510
proxyport=4520
# apps.magnetar.net
proxyserver=159\.203\.21\.90
# Transform multiverse properties files with sed
# Use master.properties in  /usr/multiverse/master, outpur result to /usr/multiverse/bin
sed -r -e "s/(^$dbhost_mv=).*/\1$MYSQLD_PORT_3306_TCP_ADDR/g" \
-e "s/(^$dbpass_mv=).*/\1$MYSQLD_ENV_MYSQL_ROOT_PASSWORD/g" \
-e "s/(^$jdbc_mv=).*/\1\/usr\/share\/java\/mysql\.jar/g" \
-e "s/(^multiverse.master_tcp_port=).*/\1$mastertcp/g" \
 < /usr/multiverse/master/master.properties > /usr/multiverse/bin/master.properties
# Correct /bin/sh to /bin/bash in master.sh
sed -e "s/bin\/sh/bin\/bash/" < /usr/multiverse/master/master.sh > /usr/multiverse/bin/master.sh 
# rename the multiverse.propereties, treat it as sed input file
mv /usr/multiverse/bin/multiverse.properties /usr/multiverse/bin/multiverse.properties.org 
sed -r -e "s/(^$dbhost_mv=).*/\1$MYSQLD_PORT_3306_TCP_ADDR/g" \
-e "s/(^$dbpass_mv=).*/\1$MYSQLD_ENV_MYSQL_ROOT_PASSWORD/g" \
-e "s/(^$jdbc_mv=).*/\1\/usr\/share\/java\/mysql\.jar/g" \
-e "s/(^multiverse.worldmgrport=).*/\1$worldmgr/g" \
-e "s/(^multiverse.proxyserver=).*/\1$proxyserver/g" \
-e "s/(^multiverse.proxyport=).*/\1$proxyport/g" \
 < /usr/multiverse/bin/multiverse.properties.org > /usr/multiverse/bin/multiverse.properties
#Correct /bin/sh to /bin/bash in multiverse.sh
#rename the file for input.
mv /usr/multiverse/bin/multiverse.sh /usr/multiverse/bin/multiverse.sh.org
sed -e "s/bin\/sh/bin\/bash/" < /usr/multiverse/bin/multiverse.sh.org > /usr/multiverse/bin/multiverse.sh 
#cp ../master/master_server.py . 
cd /usr/multiverse/bin
#cp ../master/master_server.py . 
chmod +x multiverse.sh master.sh
# Generate master server key...
#./master.sh test
# Start servers...
# mono PolicyServer.exe &
./master.sh -v start &
./multiverse.sh -w sampleworld -v start




