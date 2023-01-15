import os

env_file = os.getenv('GITHUB_ENV')

print(1)
print(2)
print(env_file)

""""
with open(env_file, "a") as file: 
    file.write(f'VPS_IP={str(server_ip)}')
"""
