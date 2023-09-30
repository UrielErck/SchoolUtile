def create_access(data):
    import subprocess
    import locale
    print(locale.getlocale())
    path = data.get('Name')
    access = str(data.get('Access'))
    remove_acces(path=path)
    if list(locale.getlocale())[0] == 'Russian_Russia':
        subprocess.call(f'icacls "{path}" /deny "Все":{access} /inheritancelevel:d /setintegritylevel h', creationflags=0x08000000)
        print('RUS')
    else:
        subprocess.call(f'icacls "{path}" /deny "everyone":{access} /inheritancelevel:e /setintegritylevel h', creationflags=0x08000000)
        print('ENG')

def remove_acces(path):
    import subprocess
    subprocess.call(f'icacls "{path}" /reset', creationflags=0x08000000)

