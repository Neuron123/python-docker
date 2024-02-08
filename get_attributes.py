import docker

# Create a Docker client
client = docker.from_env()

# Specify the container ID or name
container_id_or_name = "silly_feistel"

# Get the container object
container = client.containers.get(container_id_or_name)

# Get the image used to build the container
image_id = container.attrs['Image']

# Retrieve the image object
image = client.images.get(image_id)

# Print image details
print("Image ID:", image.id)
print("Image tags:", image.tags)
