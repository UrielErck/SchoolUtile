import winreg as wrg


def dataconvert(textkey: str = False,
                texttype: str = False):
    if textkey:
        keys = {'HKEY_CLASSES_ROOT': wrg.HKEY_CLASSES_ROOT, 'HKEY_CURRENT_USER': wrg.HKEY_CURRENT_USER,
                'HKEY_LOCAL_MACHINE': wrg.HKEY_LOCAL_MACHINE, 'HKEY_USERS': wrg.HKEY_USERS,
                'HKEY_PERFORMANCE_DATA': wrg.HKEY_PERFORMANCE_DATA, 'HKEY_CURRENT_CONFIG': wrg.HKEY_CURRENT_CONFIG}
        return keys.get(textkey)

    if texttype:
        types = {'REG_BINARY': wrg.REG_BINARY,
                'REG_DWORD': wrg.REG_DWORD,
                'REG_DWORD_LITTLE_ENDIAN': wrg.REG_DWORD_LITTLE_ENDIAN,
                'REG_DWORD_BIG_ENDIAN': wrg.REG_DWORD_BIG_ENDIAN,
                'REG_EXPAND_SZ': wrg.REG_EXPAND_SZ,
                'REG_LINK': wrg.REG_LINK,
                'REG_MULTI_SZ': wrg.REG_MULTI_SZ,
                'REG_NONE': wrg.REG_NONE,
                'REG_QWORD': wrg.REG_QWORD,
                'REG_QWORD_LITTLE_ENDIAN': wrg.REG_QWORD_LITTLE_ENDIAN,
                'REG_RESOURCE_LIST': wrg.REG_RESOURCE_LIST,
                'REG_FULL_RESOURCE_DESCRIPTOR': wrg.REG_FULL_RESOURCE_DESCRIPTOR,
                'REG_RESOURCE_REQUIREMENTS_LIST': wrg.REG_RESOURCE_REQUIREMENTS_LIST,
                'REG_SZ': wrg.REG_SZ,
                }
        return types.get(texttype)

def read(key, sub_key, name):
    PATH = wrg.OpenKey(key, sub_key)
    value = wrg.QueryValueEx(PATH, name)[0]
    return value


def add(key, sub_key, name, value, rtype):
    print(value)
    PATH = wrg.CreateKey(key, sub_key)
    wrg.SetValueEx(PATH, name, 0, rtype, value)

def InstallContextMenuAddon(
        delete: int = 0,
        check: int = 0
):
    if check == 1:
        try:
            PATH = wrg.OpenKey(wrg.HKEY_CLASSES_ROOT, 'Directory\shell\SchoolUtileAddon')
            return True
        except Exception:
            return False
    if delete == 1:
        # Delete for folders
        wrg.DeleteKeyEx(wrg.HKEY_CLASSES_ROOT, 'Directory\shell\SchoolUtileAddon\command')
        wrg.DeleteKeyEx(wrg.HKEY_CLASSES_ROOT, 'Directory\shell\SchoolUtileAddon')
        # Delete for files
        wrg.DeleteKeyEx(wrg.HKEY_CLASSES_ROOT, '*\shell\SchoolUtileAddon\command')
        wrg.DeleteKeyEx(wrg.HKEY_CLASSES_ROOT, '*\shell\SchoolUtileAddon')
        return None
    import os
    # Add for folders
    PATH = wrg.CreateKey(wrg.HKEY_CLASSES_ROOT, 'Directory\shell\SchoolUtileAddon')
    wrg.SetValueEx(PATH, '', 0, wrg.REG_SZ, 'Set Access To This File')
    PATH = wrg.CreateKey(wrg.HKEY_CLASSES_ROOT, 'Directory\shell\SchoolUtileAddon\command')
    wrg.SetValueEx(PATH, '', 0, wrg.REG_SZ, f'{os.getcwd()}\\SchoolUtile.exe --AddNewElement %1')
    # Add for files
    PATH = wrg.CreateKey(wrg.HKEY_CLASSES_ROOT, '*\shell\SchoolUtileAddon')
    wrg.SetValueEx(PATH, '', 0, wrg.REG_SZ, 'Set Access To This File')
    PATH = wrg.CreateKey(wrg.HKEY_CLASSES_ROOT, '*\shell\SchoolUtileAddon\command')
    wrg.SetValueEx(PATH, '', 0, wrg.REG_SZ, f'{os.getcwd()}\\SchoolUtile.exe --AddNewElement %V')
# print(read(wrg.HKEY_LOCAL_MACHINE, 'SOFTWARE\Policies\Microsoft\Windows\Personalization', 'NoLockScreen'))
