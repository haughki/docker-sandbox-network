# Build an image based on Linux Alpine. Pass a network configuration shell script as an argument to the script,
# then convert this argument into an environment variable so that we can 
# run it later as the ENTRYPOINT.

FROM alpine

ARG network_config_arg
ARG home="/home/networker"
ENV network_config="${home}/${network_config_arg}"

RUN cd /; mkdir ${home}
COPY --chown=root:root ${network_config_arg} ${home}
RUN chmod +x ${network_config}

# Run the network configuration script when the container starts, and then replace the script
# process with a Bourne shell so that the container keeps running, and there's a shell to connect to.
# Note that, we have to do this once the container is up and running -- it doesn't work to try and execute
# the network configuration using RUN commands in the Dockerfile. This is because these kinds of network
# changes require elevated privileges that are specific to Docker containers -- not a general Linux thing
# but specific to docker. This is why when we run the containers, we have to pass the --privileged flag.
# Once we do that, we can do the network configuration at runtime.
ENTRYPOINT ${network_config}; /bin/sh