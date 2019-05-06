@echo off
:: This batch file starts the Multiverse Master sever processes on Windows
:: You must have installed Java, a database, JDBC driver, and the Multiverse servers
:: Copyright 2012 The Multiverse Software Foundation

:: Set DEFAULT_MV_PROPERTYFILE if you want to use a different defult property file
if defined DEFAULT_MV_PROPERTYFILE (
   echo DEFAULT_MV_PROPERTYFILE is %DEFAULT_MV_PROPERTYFILE%
) else (
   echo DEFAULT_MV_PROPERTYFILE is not defined using master.properties
   set DEFAULT_MV_PROPERTYFILE=master.properties
)

:: Set to true to enable JMX management and monitoring
if not defined ENABLE_MGMT set ENABLE_MGMT=false

:: Check that script is being run from mv_home\bin
if not defined MV_HOME (
  echo MV_HOME is not defined, using relative paths
  if exist .\start-master.bat (
    set MV_HOME=..
  ) else (
    echo Batch script must be run from MV_HOME\master directory!
  )
) 

set MV_COMMON=%MV_HOME%\config\common

echo MV_HOME is %MV_HOME%
echo ENABLE_MGMT is %ENABLE_MGMT%

:: Change to "server" to use the server Java VM
set JVM_TYPE=client
set JVM_HEAP_FLAGS=-Xms32m -Xmx256m

set PROPFILE=%1
if %1x==x (
  set PROPFILE=%DEFAULT_MV_PROPERTYFILE%
)
echo Using properties file %PROPFILE%

if not defined MV_JAR (
  set MV_JAR=%MV_HOME%\dist\lib\multiverse.jar
)
if not defined MARS_JAR (
  set MARS_JAR=%MV_HOME%\dist\lib\mars.jar
)
if not defined INJECTED_JAR (
  set INJECTED_JAR=%MV_HOME%\dist\lib\injected.jar
)

set JYTHON=%MV_HOME%\other\jython.jar
set RHINO=%MV_HOME%\other\rhino1_5R5\js.jar
set GETOPT=%MV_HOME%\other\java-getopt-1.0.11.jar
set LOG4J=%MV_HOME%\other\log4j-1.2.14.jar
set BCEL=%MV_HOME%\other\bcel-5.2.jar

:: Get path to JDBC JAR file from property file, unless set in env. var.
if not defined JDBC (
  java -cp %MV_JAR% -Dmultiverse.propertyfile=%PROPFILE% -Dwin_env_var=JDBC multiverse.scripts.PropertyGetter multiverse.jdbcJarPath > tmp.bat
  : call tmp.bat
  : del tmp.bat
)
echo JDBC is %JDBC%

set MV_CLASSPATH=%INJECTED_JAR%;%MV_JAR%;%MARS_JAR%;%EXT_JAR%;%RHINO%;%GETOPT%;%JYTHON%;%JDBC%;%LOG4J%;%BCEL%

set CMDLINE_PROPS=
if defined MV_HOSTNAME (
  set CMDLINE_PROPS=-Pmultiverse.hostname=%MV_HOSTNAME%
)

set JAVA_FLAGS=-%JVM_TYPE% %JVM_HEAP_FLAGS% -cp "%MV_CLASSPATH%" -Dmultiverse.propertyfile=%PROPFILE%
set MV_LOGS=%MV_HOME%\logs\master
set JAVA_FLAGS=%JAVA_FLAGS% -Dmultiverse.logs=%MV_LOGS%

if not exist %MV_LOGS% (
  mkdir %MV_LOGS%
)

if not defined DELETE_LOGS_ON_STARTUP (
  java -cp %MV_JAR% -Dmultiverse.propertyfile=%PROPFILE% -Dwin_env_var=DELETE_LOGS_ON_STARTUP multiverse.scripts.PropertyGetter multiverse.delete_logs_on_startup > tmp.bat
  call tmp.bat
  del tmp.bat
)

if %DELETE_LOGS_ON_STARTUP%==true (
  echo Deleting existing log files
  del %MV_LOGS%\*.out*
)

if not exist run (
  echo Creating run directory
  mkdir run
)

del .\run\*.* /Q

if %ENABLE_MGMT%==true (
  echo Enabling JMX mgmt and monitoring
  set JAVA_FLAGS=-Dcom.sun.management.jmxremote %JAVA_FLAGS%
) 

set MV_BIN=%MV_HOME%\master

echo MV_HOME is %MV_HOME%
echo Using log directory %MV_LOGS%
echo Using common directory %MV_COMMON%
echo Using bin directory %MV_BIN%
echo Java Flags are: %JAVA_FLAGS%

echo *** Starting master server ***

START /B java %JAVA_FLAGS% ^
	-Dmultiverse.loggername=master ^
        multiverse.server.engine.MasterServer ^
	%CMDLINE_PROPS% ^
        %MV_BIN%\master_server.py 

rem echo $! > %MV_RUN%\master.pid
     
echo Wait for finished initializing msg... 
