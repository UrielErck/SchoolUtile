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

import GUI
GUI.main()
try:
    save_reg()
except PermissionError:
    print('Not Enough Permissions')
