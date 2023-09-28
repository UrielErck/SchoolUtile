def create_access(data):
    import subprocess
    import locale
    print(locale.getlocale())
    path = data.get('Name')
    access = ', '.join(data.get('Access'))
    if list(locale.getlocale())[0] == 'Russian_Russia':
        subprocess.call(f'icacls "{path}" /deny "Все":{access}', creationflags=0x08000000)
        print('RUS')
    else:
        subprocess.call(f'icacls "{path}" /deny "All":{access}', creationflags=0x08000000)
        print('ENG')

def remove_acces(path):
    import subprocess
    subprocess.call(f'icacls "{path}" /reset', creationflags=0x08000000)

