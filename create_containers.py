import docker

# Create a Docker client
client = docker.from_env()

# Specify the image you want to use
image_name = "nginx:latest"

# Create the container
container = client.containers.run(image_name, detach=True)

# Print container ID
print("Container ID:", container.id)
