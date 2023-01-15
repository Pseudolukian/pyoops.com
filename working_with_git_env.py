import os

env_file = os.getenv('GITHUB_ENV')


print(env_file)

""""
with open(env_file, "a") as file: 
    file.write(f'VPS_IP={str(server_ip)}')
""""