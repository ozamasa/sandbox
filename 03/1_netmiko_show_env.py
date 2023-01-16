from netmiko import ConnectHandler                              # ... 1
import sys                                                      # ... 2
from getpass import getpass                                     # ... 3


def func():
    device = {                                                  # ... 4
        "device_type": "yamaha",  # デバイスタイプ
        "ip": sys.argv[1],        # 接続先
        "username": sys.argv[2],  # ユーザ名
        "password": getpass(),    # パスワード
    }

    with ConnectHandler(**device) as connection:                # ... 5
        connection.send_command("console character en.ascii")   # ... 6
        connection.send_command("console lines infinity")
        connection.send_command("console columns 200")
        print(connection.send_command('show environment'))      # ... 7


if __name__ == "__main__":                                      # ... 8
    func()
