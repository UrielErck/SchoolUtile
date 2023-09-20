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
    file = open('config.SUCF', 'r')
    data = json.load(file)
    file.close()
    return data


def read_RegFolder():
    import winreg as wrg
    try:
        PATH = wrg.OpenKey(
            wrg.HKEY_LOCAL_MACHINE,
            'SOFTWARE\\SchoolUtile'
        )
        value = wrg.QueryValueEx(PATH, 'FoldersData')[0]
        return value
    except FileNotFoundError:
        print(f'Regedit key does not exist')


def write_RegFolder(value: list = []):
    if not type(value) == list:
        print('Can`t write not list to FoldersData')
    if value == []:
        print('Clear Regedit')
    else:
        print(f'Write to FoldersData: {value}')
    import winreg as wrg
    PATH = wrg.OpenKey(
        wrg.HKEY_LOCAL_MACHINE,
        'SOFTWARE\\SchoolUtile'
    )
    wrg.SetValueEx(PATH, 'FoldersData', 0, wrg.REG_MULTI_SZ, value)
# {
#     "RegEdit": [
#         {'display_name': 'test1',
#             "state": 0,
#             'on_value': 1,
#             'off_value': 0,
#             'key': 'HKEY_LOCAL_MACHINE',
#             'sub_key': 'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System',
#             'name': 'NoDispAppearancePage',
#             'type': 'REG_DWORD',
#         }
#     ]
# }
