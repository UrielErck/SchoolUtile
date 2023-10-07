def create_access(data):
    import subprocess
    import locale
    print(locale.getlocale())
    print(data)
    path = data.get('Name')
    access = data.get('Access')
    user = data.get('User')
    print(f'Start remove')
    remove_acces(path=path)
    print('Remove Successful')
    print(f'Path: {path} \nAccess: {access} \nUser: {user}')
    subprocess.call(f'icacls "{path}" /deny "{user}":{access}', creationflags=0x08000000)
    print('Element Add Successful')

def remove_acces(path):
    import subprocess
    import threading
    import time
    thread = threading.Thread(target=subprocess.call, args=(f'icacls "{path}" /reset /t /c /q',))
    thread.start()
    timer = 0
    while thread.is_alive():
        time.sleep(1)
        timer += 1
        if timer >= 3:
            return 1



