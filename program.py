import sys
arg = sys.argv
print(arg)
if len(arg) >= 2:
    if arg[1] == '--BackUpRegedit':
        import backup
        backup.dobackup()
        sys.exit()
    if arg[1] == '--AddNewElement':
        import backup
        data = ' '.join(arg[2:]).replace(chr(92), '/')
        print(data)
        backup.addAccess(data)
        sys.exit()


def save_reg():
    import reader as rd
    import RegEdit as re
    regdata = rd.read_dump().get("RegEdit")
    for i in regdata:
        key = re.dataconvert(textkey=i.get("key"))
        sub_key = i.get("sub_key")
        name = i.get("name")
        if i.get("state") == 1:
            value = i.get("on_value")
        else:
            value = i.get("off_value")
        rtype = re.dataconvert(texttype=i.get("type"))
        re.add(key=key, sub_key=sub_key, value=value, name=name, rtype=rtype)

try:
    import reader as rd
    if rd.read_RegFoldersJson() == []:
        rd.read_RegFoldersJson()
except Exception:
    rd.write_RegFoldersJson({'Data': []})

data = {'RegFolder': rd.read_RegFoldersJson()}
import GUI
GUI.main()

try:
    import icaclsEdit as ie
    for i in data.get('RegFolder'):
        if not i in rd.read_RegFoldersJson():
            ie.remove_acces(i)
    for i in rd.read_RegFoldersJson(alldata=1):
        ie.create_access(i)
except PermissionError:
    print('Not Enough Permissions')
try:
    save_reg()
except PermissionError:
    print('Not Enough Permissions')
sys.exit()
