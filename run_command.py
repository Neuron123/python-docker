import docker

# Create a Docker client
client = docker.from_env()

# Specify the container ID or name you want to connect to
container_id_or_name = "silly_feistel"

# Connect to the specified container
container = client.containers.get(container_id_or_name)

# Run a command inside the container
command = "cat /etc/passwd"
result = container.exec_run(command)

# Print the output of the command
print("Command output:", result.output.decode())
