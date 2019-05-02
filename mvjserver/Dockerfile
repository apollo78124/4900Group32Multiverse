FROM yan047/jdk6:1
MAINTAINER Reggie Chen <reggie@magnetargames.com>

RUN apt-get -y update
RUN apt-get -y install unzip
RUN apt-get -y install libmysql-java

WORKDIR /root
# Download multiverse server source
RUN wget http://sourceforge.net/projects/multiverse3d/files/server_20120322.zip/download
RUN mv download server_20120322.zip
RUN unzip server_20120322.zip && mv multiverse /usr
# Silverlight Polict Server
COPY PolicyFile.xml /usr/multiverse/bin/
COPY PolicyServer.exe /usr/multiverse/bin/
# Start and master scripts.
ADD start.sh /etc/my_init.d/start.sh
ADD master_server.py /usr/multiverse/bin/master_server.py
# Update sampleworld ( new vagetation...)
COPY sampleworld-main.mwc /usr/multiverse/config/sampleworld/sampleworld-main.mwc
COPY sampleworld.mvw /usr/multiverse/config/sampleworld/sampleworld.mvw
COPY sampleworld.worldassets /usr/multiverse/config/sampleworld/sampleworld.worldassets
#COPY Procfile ./
CMD ["/sbin/my_init"]

