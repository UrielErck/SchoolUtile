def create_access(data):
    import subprocess
    import locale
    print(locale.getlocale())
    path = data.get('Name')
    access = f"({','.join(data.get('Access'))})"
    remove_acces(path=path)
    command = f'icacls "{path}"'
    if list(locale.getlocale())[0] == 'Russian_Russia':
        subprocess.call(f'{command} /grant "Все":F', creationflags=0x08000000)
        subprocess.call(f'{command} /deny "Все":{access}', creationflags=0x08000000)
        print('RUS')
    else:
        subprocess.call(f'icacls "{path}" /grant "All":F', creationflags=0x08000000)
        subprocess.call(f'icacls "{path}" /deny "All":{access}', creationflags=0x08000000)
        print('ENG')

def remove_acces(path):
    import subprocess
    subprocess.call(f'icacls "{path}" /reset', creationflags=0x08000000)

