from netmiko import ConnectHandler
from netmiko import SSHDetect                                   # ... 1
import sys
from getpass import getpass


def func():
    device = {
        "device_type": "autodetect",  # デバイスタイプ          # ... 2
        "ip": sys.argv[1],        # 接続先
        "username": sys.argv[2],  # ユーザ名
        "password": getpass(),    # パスワード
    }

    detect = SSHDetect(**device)                                # ... 3
    device_type = detect.autodetect()
    print("device_type: " + device_type)
    device['device_type'] = device_type                         # ... 4

    with ConnectHandler(**device) as connection:                # ... 5
        connection.send_command("console character en.ascii")
        connection.send_command("console lines infinity")
        connection.send_command("console columns 200")
        print(connection.send_command('show environment'))


if __name__ == "__main__":
    func()
