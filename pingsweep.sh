for i in `seq 1 255`; do ping -c 1 10.11.1.$i | tr \\n ' ' | awk '/1 received/ {print $2}' ; done 

