import winreg as wrg

def dataconvert():
    keys = {'HKEY_CLASSES_ROOT': wrg.HKEY_CLASSES_ROOT, 'HKEY_CURRENT_USER': wrg.HKEY_CURRENT_USER,
            'HKEY_LOCAL_MACHINE': wrg.HKEY_LOCAL_MACHINE, 'HKEY_USERS': wrg.HKEY_USERS,
            'HKEY_PERFORMANCE_DATA': wrg.HKEY_PERFORMANCE_DATA, 'HKEY_CURRENT_CONFIG': wrg.HKEY_CURRENT_CONFIG}
def read(key, sub_key, name):
    PATH = wrg.OpenKey(key, sub_key)
    value = wrg.QueryValueEx(PATH, name)[0]
    return value
def add(key, sub_key, name, value, type):
    PATH = wrg.CreateKey(key, sub_key)
    wrg.SetValueEx(__key=PATH, __value_name=name, __type=type, __value=value)
# print(read(wrg.HKEY_LOCAL_MACHINE, 'SOFTWARE\Policies\Microsoft\Windows\Personalization', 'NoLockScreen'))
