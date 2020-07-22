#!/usr/bin/env python3

import subprocess
from image_names import image_names

print("Building...")

# build_command = 'docker build --build-arg "network_config_arg=network_host_0_02.sh" -t host_0_02 -f Dockerfile_host_0_02 .'
# subprocess.run(build_command, shell=True)
# subprocess.run(["docker", "build", "--build-arg", "network_config_arg=network_host_0_02.sh", "-t", "host_0_02", "-f", "Dockerfile_host_0_02", "."])

# Create a new image for each host, passing in the necessary
# network configuration for each different host. It seems like
# it should not be necessary to create an entire new image for each host:
# this just doesn't scale. But, this works for now.
for name in image_names:
    build_command = 'docker build --build-arg "network_config_arg=network_' + name + '.sh" -t ' + name + ' .'
    subprocess.run(build_command, shell=True)

#docker run -dit --name host_100_02 --network net1 --privileged host_100_02
# start -i interactive -t with terminal but -d detached. This way, the container will be running,
# but not at the command prompt - that is, control will return to the command prompt, but
# you can still attached to the process later and get a command prompt.
for name in image_names:
    run_command = 'docker run -dit --name ' + name + ' --network net1 --privileged ' + name
    subprocess.run(run_command, shell=True)

