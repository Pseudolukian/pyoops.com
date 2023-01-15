import os

env_file = os.getenv('GITHUB_ENV')
server_ip = "123.213.341.21"
print(1)
print(2)
print(env_file)


with open(env_file, "a") as file: 
    file.write(f'VPS_IP={str(server_ip)}')

print(1)
print(2)
print(env_file)


