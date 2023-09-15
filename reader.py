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
