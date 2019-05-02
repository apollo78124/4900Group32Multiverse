#EC2  setup is using master/master.properties for master server, and bin/multiverse.properties for world server
# following route command routes the original .net client ( 5040 ) port to new silverlight 4505 port for master server etc....
# Master server TCP
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 9005 -j REDIRECT --to-port 4505
# World management server
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 5040 -j REDIRECT --to-port 4510
# Proxy plugin for client communication
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 5050 -j REDIRECT --to-port 4520
# Voice port
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 5051 -j REDIRECT --to-port 4521
# RDP ( reliable udp ) re-direction for .net client ( server can serve both .net and Silverlight ) 
sudo iptables -t nat -A PREROUTING -i eth0 -p udp --dport 5040 -j REDIRECT --to-port 4510
sudo iptables -t nat -A PREROUTING -i eth0 -p udp --dport 5050 -j REDIRECT --to-port 4520

