import subprocess
hosts = ['192.168.100.1', '192.168.100.101', '192.168.100.201']
for host in hosts:
    print('====================')
    result = subprocess.run(['ping', host, '-c', '2', '-W', '1000'], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    if result.returncode == 0:
        print('OK')
    else:
        print('NG')
