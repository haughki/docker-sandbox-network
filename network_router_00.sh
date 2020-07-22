#!/bin/sh

ifconfig eth0:0 198.162.0.1
ifconfig eth0:1 198.162.100.1

# The following line runs the passed command line args.
# In this case, it will run /bin/sh. This has the effect of keeping the container running. Without this line,
# if this script just exited, the container would exit as well. This is how CMD and ENTRYPOINT work: once
# the commands/scripts they run exit, the container exits as well.
exec "$@"