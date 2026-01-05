import docker

client = docker.from_env()
container = client.containers.run("busybox", "sleep 3600", detach=True)
print(f"Container {container.id} is running")
exec_result = container.exec_run("hostname")
print("Hostname:", exec_result.output.decode().strip())
container.stop()
print("stop")
