# This Dockerfile is used to create a Jenkins SSH agent with Python 

# We start from the Jenkins SSH agent image.
FROM jenkins/ssh-agent:6.9.0 as ssh-agent

# The RUN command executes a series of commands in the new layer of the image and commits the results.
# The following commands are executed:

# 1. Update the package list.
# 2. Install necessary dependencies including Python, python3-venv and several Python-related packages.
RUN apt-get update && apt-get install -y --no-install-recommends \
    binutils ca-certificates curl git python3 python3-venv python3-pip python3-setuptools python3-wheel python3-dev wget \
    && rm -rf /var/lib/apt/lists/*

# Create an alias for python3 as python.
RUN ln -s /usr/bin/python3 /usr/bin/python

# Create a Python virtual environment in /opt/venv.
RUN python3 -m venv /opt/venv

# Activate the virtual environment by adding its bin directory to the PATH.
# This ensures that the virtual environment is activated for all subsequent RUN commands in the Dockerfile.
ENV PATH="/opt/venv/bin:$PATH"

# Install required Python packages in the virtual environment.
RUN pip install pytest

# Add the PATH environment variable to /etc/environment so that it is available to all users and processes.
RUN echo "PATH=${PATH}" >> /etc/environment

#install docker-ce on this agent in order to build and push image from jenkins
RUN install -m 0755 -d /etc/apt/keyrings &&\
	curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc &&\
	chmod a+r /etc/apt/keyrings/docker.asc &&\
	echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null &&\
  apt-get update &&\
  apt-get install -y --no-install-recommends acl docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

#gives jenkins user permissions to access /var/run/docker.sock
#via setfacl --modify user:jenkins:rw /var/run/docker.sock
#in init_docker_access.sh
COPY init_docker_access.sh init_docker_access.sh

# override entrypoint of inherited jenkins/ssh-agent:6.9.0 
# my_entrypoint.sh = call init_docker_access.sh and call setup-sshd
COPY my_entrypoint.sh my_entrypoint.sh
ENTRYPOINT ["sh" ,"my_entrypoint.sh"]

# Set the ownership of the Jenkins agent home directory to the Jenkins user.
# This ensures that the Jenkins user has the necessary permissions to access its home directory.
RUN chown -R jenkins:jenkins "${JENKINS_AGENT_HOME}"
