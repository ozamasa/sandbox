from netmiko import ConnectHandler
import datetime                                                 # ... 1
import sys
from getpass import getpass
import pandas as pd                                             # ... 2

def func():
    device = {
        "device_type": "yamaha",  # デバイスタイプ
        "ip": sys.argv[1],        # 接続先
        "username": sys.argv[2],  # ユーザ名
        "password": getpass(),    # パスワード
    }

    with ConnectHandler(**device) as connection:
        connection.send_command("console character en.ascii")
        connection.send_command("console lines infinity")
        connection.send_command("console columns 200")
        output = connection.send_command("show status dhcp")    # ... 3

        keys = ["Leased address",
                "(type) Client ID",
                "Remaining lease"]                              # ... 4
        dhcp = {keys[0]: [], keys[1]: [], keys[2]: []}          # ... 5

        for line in output.splitlines():                        # ... 6
            key, value = line.strip().split(':')                # ... 7
            key = key.strip()                                   # ... 8
            value = value.strip()
            if key in dhcp:
                dhcp[key].append(value)                         # ... 9

        df = pd.DataFrame(dhcp)                                 # ... 10
        now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        df.to_csv("dhcp_" + now + ".csv")                       # ... 11

if __name__ == "__main__":
    func()
