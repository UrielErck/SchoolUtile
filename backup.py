import pyuac


def dobackup():
    import subprocess
    import datetime
    import os
    from plyer import notification
    import reader as rd
    from pathlib import Path
    rez = 0
    try:
        os.makedirs(f'{Path.home()}\\backup')
    except Exception:
        print('Folder exist')
    for i in ['HKLM', 'HKCU', 'HKCR', 'HKU', 'HKCC']:
        command = f'reg export {i} {Path.home()}\\backup\\{i}-{datetime.datetime.now().strftime("%Y-%m-%d")}.reg /y'
        print(command)
        temp = subprocess.call(command, creationflags=0x08000000)
        if temp == 1:
            rez = 1

    notif = ['Regedit backup successful', 'An error has occurred while backup regedit']
    notification.notify(
        title='Admin Utile',
        message=notif[rez],
        app_icon=rd.resource_path('icon.ico'),
        timeout=10,
    )
    # import winreg as wrg
    # import datetime
    # keys = {'HKEY_CLASSES_ROOT': wrg.HKEY_CLASSES_ROOT, 'HKEY_CURRENT_USER': wrg.HKEY_CURRENT_USER,
    #         'HKEY_LOCAL_MACHINE': wrg.HKEY_LOCAL_MACHINE, 'HKEY_USERS': wrg.HKEY_USERS,
    #         'HKEY_PERFORMANCE_DATA': wrg.HKEY_PERFORMANCE_DATA, 'HKEY_CURRENT_CONFIG': wrg.HKEY_CURRENT_CONFIG}
    # for i in keys:
    #     wrg.SaveKey(keys.get(i), f'{i} - {datetime.datetime.now().strftime("%Y-%m-%d %H-%M-S")}.reg')

def autorun(state):
    import os
    if state in ['1', 1]:
        state = True
    else:
        state = False
    set_autostart_registry(app_name='SchoolUtile', key_data=f'{os.getcwd()}\\SchoolUtile.exe --BackUpRegedit', autostart=state)

def set_autostart_registry(app_name, key_data=None, autostart: bool = True) -> bool:
    import winreg
    """
    Create/update/delete Windows autostart registry key

    ! Windows ONLY
    ! If the function fails, OSError is raised.

    :param app_name:    A string containing the name of the application name
    :param key_data:    A string that specifies the application path.
    :param autostart:   True - create/update autostart key / False - delete autostart key
    :return:            True - Success / False - Error, app name dont exist
    """

    with winreg.OpenKey(
            key=winreg.HKEY_CURRENT_USER,
            sub_key=r'Software\Microsoft\Windows\CurrentVersion\Run',
            reserved=0,
            access=winreg.KEY_ALL_ACCESS,
    ) as key:
        try:
            if autostart:
                winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, key_data)
            else:
                winreg.DeleteValue(key, app_name)
        except OSError:
            return False
    return True

def addAccess(path):
    import subprocess
    import os
    if not pyuac.isUserAdmin():
        cmdcommand = f'powershell -Command "Start-Process -FilePath "{os.getcwd()}\\SchoolUtile.exe" -ArgumentList "--AddNewElement", \'{path}\' -Verb RunAs"'
        print(cmdcommand)
        subprocess.call(cmdcommand, creationflags=0x08000000)
        return 2
    import reader as rd
    import icaclsEdit as iE
    if path in rd.read_RegFoldersJson():
        return 1
    data = rd.read_RegFoldersJson(alldata=1)
    command = {'Name': path, 'Access': rd.read_dump().get("DefaultAccessType"), 'User': str(rd.read_dump().get('User'))}
    data.append(command)
    rd.write_RegFoldersJson({'Data': data})
    iE.create_access(command)
    print(f'Command: {command}')
    return 0
