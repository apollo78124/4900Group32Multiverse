# Look at ports.sh for comments about port mapping.
# We don't need to run iptables in ports.sh for port redirection
# and it is not necessary to EXPOSE the ports if they are not used
# for intra-containers communications ( -link )
docker run -h apps.magnetar.net -d -p 943:943 -p 4505:4505 \
              -p 9005:4505 \
              -p 4510:4510 \
              -p 5040:4510 \
              -p 4520:4520 \
              -p 5050:4520 \
              -p 5040:4510/udp \
      	      -p 5050:4520/udp \
              -p 9010:9010/udp \
 --name multiverse --link=mysqld lazydino/multiverse 

