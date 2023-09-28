def create_dump(data):
    if type(data) != dict:
        raise 'Data not dict'
    import json
    file = open('config.SUCF', 'w')
    json.dump(data, file, sort_keys=True, indent=4)
    file.close()
    return 0


def read_dump():
    import json
    try:
        file = open('config.SUCF', 'r')
        data = json.load(file)
        file.close()
    except FileNotFoundError:
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, u"Please create configuration file config.SUCF\n and paste {'RegEdit': []} by json format", u"Configuration File Not Found", 0)
        return {'RegEdit': []}
    return data


def read_RegFoldersJson(alldata: int = 0):
    import winreg as wrg
    import json
    # try:
    PATH = wrg.OpenKey(
        wrg.HKEY_LOCAL_MACHINE,
        'SOFTWARE\\SchoolUtile'
    )
    value = json.loads(str(wrg.QueryValueEx(PATH, 'FoldersData')[0]))
    value: dict
    value = value.get('Data')
    value: list
    if value == None:
        value = []
    if alldata == 0 and value != None:
        for i in range(len(value)):
            value[i] = value[i].get('Name')
    return value
    # except Exception:
    #     print(f'Json Read Error')
    #     return []

def write_RegFoldersJson(data: dict = {'Data': [{'Name': 'NotSelected', 'Access': ['NotSelected']}]}):
    import winreg as wrg
    import json
    PATH = wrg.CreateKey(
        wrg.HKEY_LOCAL_MACHINE,
        'SOFTWARE\\SchoolUtile'
    )
    wrg.SetValueEx(PATH, 'FoldersData', 0, wrg.REG_EXPAND_SZ, json.dumps(data))


def read_RegFolder():
    import winreg as wrg
    try:
        PATH = wrg.OpenKey(
            wrg.HKEY_LOCAL_MACHINE,
            'SOFTWARE\\SchoolUtile'
        )
        value = wrg.QueryValueEx(PATH, 'FoldersData')[0]

        return value
    except OSError:
        print(f'Regedit key does not exist')
        return []


def write_RegFolder(value: list = []):
    if not type(value) == list:
        print('Can`t write not list to FoldersData')
    if value == []:
        print('Clear Regedit')
    else:
        print(f'Write to FoldersData: {value}')
    import winreg as wrg
    # try:
    PATH = wrg.CreateKey(
        wrg.HKEY_LOCAL_MACHINE,
        'SOFTWARE\\SchoolUtile'
    )
    wrg.SetValueEx(PATH, 'FoldersData', 0, wrg.REG_MULTI_SZ, value)

def resource_path(relative_path):
    import os
    import sys
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

    # except PermissionError:
    #     print('No enough permissions')
    #     return 1


# {
#     "RegEdit": [
#         {
#             "display_name": "NEW",
#             "key": "HKEY_LOCAL_MACHINE",
#             "name": "NoDispAppearancePage",
#             "off_value": 0,
#             "on_value": 1,
#             "state": 0,
#             "sub_key": "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
#             "type": "REG_DWORD"
#         }
#     ],
#     "backup_state": 1
# }
