def create_access(path):
    import subprocess
    import locale
    print(locale.getlocale())
    if list(locale.getlocale())[0] == 'Russian_Russia':
        subprocess.call(f'icacls "{path}" /deny "Все":D', creationflags=0x08000000)
        print('RUS')
    else:
        subprocess.call(f'icacls "{path}" /deny "All":D', creationflags=0x08000000)
        print('ENG')

def remove_acces(path):
    import subprocess
    subprocess.call(f'icacls "{path}" /reset', creationflags=0x08000000)

