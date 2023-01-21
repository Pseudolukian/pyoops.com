import requests, json, time, os, subprocess, sys

api_key = str(sys.argv[1])
url = "https://api.1cloud.ru/server/"
server_id = str()

headers = {"Content-Type":"application/json", "Authorization": "Bearer " + api_key}
server_config = json.load(open("./configs/vps_config.json")) 


def create_server():
    create_server = requests.post(url, headers = headers, json = server_config)
    server_id = create_server.json()
    return server_id

if __name__ == "__main__":
    print(create_server())