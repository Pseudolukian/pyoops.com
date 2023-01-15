import requests, json, time, os, subprocess, sys

api_key = str(sys.argv[1])
url = "https://api.1cloud.ru/server/"
server_id = str()

headers = {"Content-Type":"application/json", "Authorization": "Bearer " + api_key}
server_config = json.load(open("./configs/vps_config.json")) 


def create_server():
    create_server = requests.post(url, headers = headers, json = server_config)
    server_id = create_server.json()["ID"]
    print("Server", server_id, "start to create.")
    time.sleep(10)
    check_server_status = requests.get(url + str(server_id), headers = headers)
    check_server_status.json()

    while check_server_status.json()['State'] == "New":
        time.sleep(45)
        check_server_status = requests.get(url + str(server_id), headers = headers)
        check_server_status.json()
        print("Server", server_id, "creating...")
    
    server_ip = str(check_server_status.json()["PrimaryNetworkIp"])
    subprocess.Popen(f'echo "VPS_IP"={server_ip} >> $GITHUB_ENV', shell=True)
    result = "Server" + str(server_id) + "is created successful. " + "IP:" + str(server_ip)
    return result


if __name__ == "__main__":
    print(create_server())

    