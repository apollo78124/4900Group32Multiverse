FROM multiverse
MAINTAINER DavidLee KevinLo

RUN apt-get update
RUN apt-get install -y maven
COPY dockerservice /root/usr/local/service/dockerservice
WORKDIR /root/usr/local/service/dockerservice
RUN mvn install:install-file -Dfile=/root/usr/local/service/dockerservice/libs/multiverse-1.0.jar -DgroupId=multiverse -DartifactId=multiverse -Dversion=1.0 -Dpackaging=jar
RUN mvn install:install-file -Dfile=/root/usr/local/service/dockerservice/libs/mars-1.0.jar -DgroupId=mars -DartifactId=mars -Dversion=1.0 -Dpackaging=jar
RUN mvn install:install-file -Dfile=/root/usr/local/service/dockerservice/libs/inject-1.0.jar -DgroupId=inject -DartifactId=inject -Dversion=1.0 -Dpackaging=jar
RUN mvn install:install-file -Dfile=/root/usr/local/service/dockerservice/libs/jython.jar -DgroupId=jython -DartifactId=jython -Dversion=1.0 -Dpackaging=jar
RUN mvn package -e
