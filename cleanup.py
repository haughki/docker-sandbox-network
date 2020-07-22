#!/usr/bin/env python3

import subprocess
from image_names import image_names

print("Cleaning up...")

# docker stop host_0_02
# docker rm host_0_02
# docker rmi host_0_02
# kill each container, delete each container, and delete each image
for name in image_names:
    subprocess.run('docker kill ' + name, shell=True)
    subprocess.run('docker rm ' + name, shell=True)
    subprocess.run('docker rmi ' + name, shell=True)

