def main():
    import reader as rd
    import customtkinter as ctk
    from PIL import Image
    import RegEdit
    import webbrowser
    linkgit = 'https://github.com/UrielErck/SchoolUtile/tree/main'
    standartcolor = [('#FFFFFF', '#333333'), ('#336b97', '#154972')]
    app = ctk.CTk(fg_color=standartcolor[0])
    app.resizable(width=False, height=False)
    app.title('Admin tool')
    app.iconbitmap(rd.resource_path('icon.ico'))

    class MainPage:
        text = {'Title': 'User`s Manual',
                'Text': [
                    'To open menu press ≡ button in up',
                    'left side',
                    '',
                    'The menu have 3 options: ',
                    '',
                    'Hello page - This page, that show you',
                    'help info, about this program.',
                    '',
                    'RegEdit - This page allow you to quick edit',
                    'Windows Register by configuration file. To',
                    'add new element press + and save, than edit',
                    'save file "config.SUCF" with text editor',
                    'using JSon format. In page you can on/off',
                    'prewrited configs or delete it bu press x',
                    'The backup option is export regedit to files',
                    'in userfolder/backup. If this folder does not',
                    'exist or something  will go wrong you will have',
                    'error message.',
                    '',
                    'Folder Control - This page allow you to deny',
                    'delete folder/files. To add new element press',
                    'folder icon and select file/folder than press',
                    'check mark icon. Than save all by pressing',
                    'diskette button.',
                    '',
                    'Open Configuration File - This button allow you',
                    'to quick open configuration file in default text',
                    'editor.',
                    '',
                    'If file "config.SUCF" was not found you will',
                    'have error message. You can create configuration',
                    'by pressing + button in RegEdit page, than save',
                    'changes and file will be created.',
                    'This app is completely open-sours, but this app',
                    'allow to use only if i say so. So please if you',
                    'need link to Github dm me by email and ask about',
                    'this.',
                    '',
                    'This app is sign and if you use app with out sign',
                    'this mean that this app not created by me and can',
                    'be danger. I am not responsible for the malfunction',
                    'of your personal computer, because this program',
                    'interacts directly with the system settings.',
                    'This app is request admin privileges to communicate',
                    'with Windows Registry.',
                    '',
                    'My email: qugifurldfk@gmail.com',
                         ]}
        visible = False
        root = ctk.CTkFrame(master=app, fg_color=standartcolor[0])

        def __init__(self):
            super().__init__()
            self.root.grid(column=1, row=0)
            textframe = ctk.CTkScrollableFrame(master=self.root, fg_color='transparent', width=350)
            textframe.grid(column=1, row=0, ipadx=10, ipady=10, columnspan=2)
            Title = ctk.CTkLabel(master=textframe, font=('Calibre', 20), text=self.text.get('Title'),
                                 fg_color=standartcolor[1], corner_radius=5, text_color='white')
            Title.grid(row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky='WE')

            githubphoto = ctk.CTkImage(light_image=Image.open(rd.resource_path('github_white.png')),
                                       dark_image=Image.open(rd.resource_path('github_white.png')), size=(23, 23))
            Githudbtn = ctk.CTkButton(master=textframe, image=githubphoto, text='', width=25, height=30,
                                     fg_color=standartcolor[1], corner_radius=5, hover_color=standartcolor[1][::-1],
                                      command=lambda: webbrowser.open(linkgit))
            Githudbtn.grid(row=0, column=2, padx=5, pady=5, ipadx=5, ipady=5, sticky='E')

            Text = ctk.CTkLabel(master=textframe, font=('Calibre', 15), text="\n".join(self.text.get('Text')),
                                 fg_color=standartcolor[1], corner_radius=5, justify='left', text_color='white')
            Text.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5, sticky='WE', columnspan=3)


    class RegEditFrame:
        visible = False
        root = ctk.CTkFrame(master=app, fg_color=standartcolor[0])
        dataEnt = []
        Elements = rd.read_dump()
        ischanged = 0
        ElFrame = ctk.CTkScrollableFrame(master=root, fg_color=standartcolor[0], width=300)

        def add_el(self):
            print(f'Add el Name: NEW')
            temp = self.Elements.get('RegEdit')
            temp.append({
            'display_name': 'NEW',
            "state": 0,
            'on_value': 1,
            'off_value': 0,
            'key': 'HKEY_LOCAL_MACHINE',
            'sub_key': 'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System',
            'name': 'NoDispAppearancePage',
            'type': 'REG_DWORD',
            })
            self.Elements.update({'RegEdit': temp})
            self.dataEnt = []
            self.__init__()

        def remove_el(self, index):
            print(f'del el Id:{index} Name: {self.dataEnt[index].get("name").cget("text")}')
            self.dataEnt[index].get("itemframe").destroy()
            self.dataEnt.pop(index)
            tmplst = self.Elements.get('RegEdit')
            tmplst.pop(index)
            self.Elements.update({'RegEdit': tmplst})
            rd.create_dump(self.Elements)
            return 0

        def save_changes(self):
            print(f'Save changes arrived')
            if not self.visible:
                pass
            self.ischanged = 1
            for i in range(len(self.dataEnt)):
                state = self.dataEnt[i].get('stateswitch').get()
                self.Elements.get('RegEdit')[i].update({'state': state})
                rd.create_dump(self.Elements)

        def __init__(self):
            super().__init__()
            self.ElFrame.destroy()
            self.root.grid(row=0, column=1)
            self.dataEnt = []
            app.bind('<Return>', lambda event: self.save_changes())
            self.ElFrame = ctk.CTkScrollableFrame(master=self.root, fg_color=standartcolor[0], width=300)
            self.ElFrame.grid(row=0, column=0, sticky='E', columnspan=3)

            buttonframe = ctk.CTkFrame(master=self.root, fg_color=standartcolor[0])
            buttonframe.grid(column=0, row=1, sticky='SW', pady=10, padx=8)

            savebtn = ctk.CTkButton(master=buttonframe, text='💾', width=30, font=('Calibre', 18), height=30,
                                    fg_color=standartcolor[1], corner_radius=5, hover_color=standartcolor[1][::-1],
                                    command=self.save_changes)
            savebtn.grid(column=0, padx=10, row=0)

            addbtn = ctk.CTkButton(master=buttonframe, text='+', width=32, font=('Calibre', 18), height=30,
                                   fg_color=standartcolor[1], corner_radius=5, hover_color=standartcolor[1][::-1],
                                   command=self.add_el)
            addbtn.grid(column=1, padx=10, row=0)

            index = 0
            for i in self.Elements.get('RegEdit'):
                print(f'Element {index}: {i}')
                index += 1
                itemframe = ctk.CTkFrame(master=self.ElFrame, fg_color=standartcolor[1], corner_radius=5)
                self.dataEnt.append({
                    "itemframe": itemframe,
                    'name': ctk.CTkLabel(itemframe, text=i.get('display_name'), width=260, text_color='white'),
                    'stateswitch': ctk.CTkSwitch(itemframe, text=None),
                    'delbtn': ctk.CTkButton(itemframe, text='×', width=22, height=22, fg_color='red'
                                            , hover_color='dark red',
                                            command=lambda ind=index: self.remove_el(ind-1)),
                    'index': index-1,
                })
                self.dataEnt[index-1].get('name').grid(row=0, column=0, sticky='W', padx=10, columnspan=2, pady=5)
                if self.Elements.get('RegEdit')[index-1].get('state') in [1, '1', True, 'True']:
                    self.dataEnt[index-1].get('stateswitch').select()
                elif self.Elements.get('RegEdit')[index-1].get('state') in [0, '0', False, 'False']:
                    self.dataEnt[index-1].get('stateswitch').deselect()
                self.dataEnt[index - 1].get('stateswitch').grid(row=1, column=0, padx=10, pady=5, sticky='WS')
                self.dataEnt[index - 1].get('delbtn').grid(row=1, padx=10, sticky='ES', column=1, pady=5)
                itemframe.grid(column=1, row=index - 1, padx=10, pady=10, sticky='WE')
                itemframe.grid_columnconfigure(1, weight=1)


    class Access:
        root = ctk.CTkFrame(master=app, fg_color=standartcolor[0])
        visible = False
        FoldersData = rd.read_RegFoldersJson(alldata=1)
        ElData = []

        def __init__(self):
            self.ElData = []
            self.root.grid(row=0, column=1)
            index = -1
            self.Ellist = ctk.CTkScrollableFrame(self.root, fg_color=standartcolor[0], width=300)
            self.Ellist.grid(row=0, column=0, sticky='E', columnspan=3)
            selectbtn = ctk.CTkButton(self.root, text='📂', width=30, font=('Calibre', 18), height=30,
                                      fg_color=standartcolor[1], corner_radius=5, hover_color=standartcolor[1][::-1],
                                            command=self.GUI_addel)
            selectbtn.grid(row=1, column=0, sticky='S', pady=10, padx=10)

            selectbtn = ctk.CTkButton(self.root, text='💾', width=30, font=('Calibre', 18), height=30,
                                      fg_color=standartcolor[1],
                                      corner_radius=5, hover_color=standartcolor[1][::-1],
                                      command=lambda data=self.FoldersData: rd.write_RegFoldersJson({'Data': data}))
            selectbtn.grid(row=1, column=0, sticky='SW', pady=10, padx=10)
            for i in self.FoldersData:
                index += 1
                frame = ctk.CTkFrame(master=self.Ellist, fg_color=standartcolor[1], corner_radius=5)
                self.ElData.append({
                    'Frame': frame,
                    'Name': ctk.CTkLabel(frame, text=f"{str(i.get('Name').split('/')[-1])}", width=210, text_color='white'),
                    'DelBtn': ctk.CTkButton(frame, text='×', height=22, width=22, fg_color='red',
                                            hover_color='dark red',
                                            command=lambda ind=index: self.delel(index=ind)),
                    'Path': i.get('Name'),
                    'Access': i.get('Access'),
                    'Index': index,
                    'infobtn': ctk.CTkButton(frame, text='i', height=22, width=22, fg_color='green',
                                            hover_color='dark green',
                                            command=lambda ind=index: self.info(index=ind)),
                    'User': i.get('User')
                })
                frame, name, delbtn, path, access, index, infobtn, user = self.ElData[index].values()
                frame.grid(row=index, padx=10, pady=10, sticky='WE')
                frame.grid_columnconfigure(1, weight=1)
                name.grid(row=0, column=0, padx=5)
                infobtn.grid(row=0, column=1, padx=3, sticky='E')
                delbtn.grid(row=0, column=2, padx=3, sticky='E')


        def delel(self, index: int):
            print(f'del el Id:{index} Name: {self.ElData[index].get("Name").cget("text")}')
            self.ElData[index].get('Frame').grid_forget()
            self.ElData[index].get('Frame').destroy()
            self.ElData.pop(index)
            self.FoldersData.pop(index)
            Access()

        def selel(self, lable, type: int = 0):
            if type == 0:
                filename = tuple([ctk.filedialog.askdirectory()])
                filename: tuple
            elif type == 1:
                filename = ctk.filedialog.askopenfilenames(filetypes=(('Links', '*.lnk'), ('All files', '*.*')))
                filename: tuple
            else:
                filename = ''
                filename: str
            if filename == '':
                print(f'Folder not selected')
                return ''
            print(filename)
            lable.configure(text='\n'.join(filename))
            return filename

        def addel(self, frame, filename: str or tuple = ''):
            print(filename)
            if filename in ['', None] or type(filename) == int:
                print('Wrong filename value')
                return [frame, 1]

            filename = filename.split('\n')
            for i in filename:
                self.FoldersData.append({'Name': i, 'Access': rd.read_dump().get("DefaultAccessType"), 'User': rd.read_dump().get('User')})
            print(f'filePATH: {filename}')
            self.__init__()
            return [frame, 0]

        def GUI_addel(self):
            path = ''

            newlayer = ctk.CTkToplevel(app, fg_color=standartcolor[0])
            newlayer.resizable(width=False, height=False)
            newlayer.title('Add Element')
            newlayer.attributes('-topmost', 'true')
            newlayer.grid()

            lablepath = ctk.CTkLabel(newlayer, text=path, font=('Calibri', 15), fg_color=standartcolor[1],
                                     corner_radius=5, width=280, text_color='white')
            lablepath.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

            # Select Frame
            selframe = ctk.CTkFrame(newlayer, fg_color=standartcolor[0])
            selframe.grid(row=1, column=0, columnspan=2, sticky='W')

            selfoldbtn = ctk.CTkButton(selframe, text='Select Folder', width=40,
                                       command=lambda lable=lablepath: self.selel(lable=lable, type=0))
            selfoldbtn.grid(row=1, column=0, padx=5, pady=5, sticky='W')

            selfilebtn = ctk.CTkButton(selframe, text='Select File', width=40,
                                       command=lambda lable=lablepath: self.selel(lable=lable, type=1))
            selfilebtn.grid(row=1, column=1, padx=5, pady=5, sticky='E')

            # Ask frame
            askframe = ctk.CTkFrame(newlayer, fg_color=standartcolor[0])
            askframe.grid(row=1, column=1, columnspan=2, sticky='E')

            yesbtn = ctk.CTkButton(askframe, text='✔', width=25, fg_color='green', hover_color='dark green',
                command=lambda lable=lablepath: self.addel(frame=newlayer, filename=lable.cget('text'))[0].destroy())
            yesbtn.grid(row=1, column=0, padx=5, pady=5)

            nobtn = ctk.CTkButton(askframe, text='❌', width=25, fg_color='red', hover_color='dark red',
                                command=lambda frame=newlayer: frame.destroy())
            nobtn.grid(row=1, column=1, sticky='E', padx=5, pady=5)

        def info(self, index: int = 0):
            def savechanges(idk):
                self.FoldersData[index].update({'Access': accstypeentr.get()})
                self.FoldersData[index].update({'User': accstypeuserent.get()})

            newlayer = ctk.CTkToplevel(app, fg_color=standartcolor[0])
            newlayer.resizable(width=False, height=False)
            newlayer.title('Element Info')
            newlayer.attributes('-topmost', 'true')
            newlayer.grid()
            text = [
                f'Name: {str(self.ElData[index].get("Path").split("/")[-1])}',
                # f'Access type: {", ".join(self.ElData[index].get("Access"))}',
                    ]
            ctk.CTkButton(newlayer, fg_color=standartcolor[1], corner_radius=5, height=35,
                          text=f' Full Path: {self.ElData[index].get("Path")}', hover_color=standartcolor[1][::-1],
                          command=lambda: webbrowser.open("/".join(self.ElData[index].get("Path").split("/")[:-1])), anchor='w')\
                .grid(row=0, column=0, padx=10, pady=10, sticky='WEN', columnspan=3)
            rowindex = 1
            for i in text:
                frame = ctk.CTkFrame(newlayer, fg_color=standartcolor[1], corner_radius=5)
                frame.grid(row=rowindex, column=0, padx=10, pady=10, sticky='WEN', columnspan=3)
                lable = ctk.CTkLabel(frame, text=i, font=('Calibri', 15), text_color='white')
                lable.grid(padx=5, pady=3)
                rowindex +=1

            accstypeframe = ctk.CTkFrame(fg_color=standartcolor[1], height=35, master=newlayer)
            print(self.ElData[index].get('Access'))
            newlayer.bind('<Return>', savechanges)
            accstypeframe.grid(row=rowindex, column=0,  padx=10, pady=10, sticky='WEN', columnspan=3)

            accstypename = ctk.CTkLabel(text='Access type: ', master=accstypeframe, fg_color=standartcolor[1], corner_radius=5, text_color='white')
            accstypename.grid(row=0, column=0, ipadx=5)

            accstypeentr = ctk.CTkEntry(placeholder_text='Example: D,W', master=accstypeframe)
            try:
                accstypeentr.insert(index=0, string=str(self.ElData[index].get('Access')))
            finally:
                pass
            accstypeentr.grid(row=0, column=1, padx=5, pady=3, columnspan=2)

            accstypeinfo = ctk.CTkButton(master=accstypeframe, text='i', fg_color='green', hover_color='dark green',
                                         height=25, width=25,
                                         command=lambda: webbrowser.open('https://learn.microsoft.com/ru-ru/windows-server/administration/windows-commands/icacls'))
            accstypeinfo.grid(row=0, column=3, padx=5, pady=3)

            accstypeuser = ctk.CTkFrame(master=accstypeframe, fg_color=standartcolor[1], height=35)
            accstypeuser.grid(row=0, column=4, padx=5, pady=3)

            accstypeuserlable = ctk.CTkLabel(master=accstypeuser, text='User Name', text_color='white')
            accstypeuserlable.grid(row=0, column=0, padx=5, pady=3)

            accstypeuserent = ctk.CTkEntry(master=accstypeuser, placeholder_text='Example: User1')
            accstypeuserent.insert(0, str(self.ElData[index].get('User')))
            accstypeuserent.grid(row=0, column=1, padx=5, pady=3)


    class Settings:
        visible = False
        root = ctk.CTkFrame(master=app, corner_radius=5, fg_color='transparent')

        def __init__(self):
            self.root.grid(row=0, column=1)
            Elframe = ctk.CTkScrollableFrame(master=self.root, corner_radius=5, fg_color='transparent', width=350)
            Elframe.grid(row=0, column=0, padx=10, pady=10, columnspan=3, sticky='WE')

            class backup_El:
                frame = ctk.CTkFrame(master=Elframe, corner_radius=5, fg_color=standartcolor[1])
                frame.grid(column=0, row=0, sticky='W')
                backupswitch = ctk.CTkSwitch(master=frame, text='Auto Back-Up', width=32, font=('Calibre', 12),
                                             height=30, text_color='white')
                backupswitch.configure(command=lambda: self.backup(state=backup_El.backupswitch.get()))
                if rd.read_dump().get("backup_state") in ['1', 1]:
                    backupswitch.select()
                backupswitch.grid(sticky='NSWE', padx=10, pady=5)

            class Deafult_Access:
                AccessFrame = ctk.CTkFrame(master=Elframe, corner_radius=5, fg_color=standartcolor[1])
                AccessFrame.grid(pady=10, column=0, row=1, sticky='W')
                AccessLable = ctk.CTkLabel(master=AccessFrame, text='Default Access Type: ', fg_color='transparent', text_color='white')
                AccessLable.grid(row=0, column=0, padx=10, pady=5, sticky='NSWE')
                AccessEntry = ctk.CTkEntry(master=AccessFrame, placeholder_text='Example: D,W')
                if rd.read_dump().get('DefaultAccessType') != None:
                    AccessEntry.insert(index=0, string=str(rd.read_dump().get('DefaultAccessType')))
                AccessEntry.grid(row=0, column=1, padx=5, pady=5, sticky='NSWE')
                data = rd.read_dump()
                command = lambda: Deafult_Access.data.update({'DefaultAccessType': str(Deafult_Access.AccessEntry.get())})
                AccessSaveButton = ctk.CTkButton(master=AccessFrame, text='💾', hover_color='dark green', fg_color='green', width=30, height=30, font=('Calibre', 20),
                                                 command=lambda: rd.create_dump([Deafult_Access.command(), Deafult_Access.data][1]))
                AccessSaveButton.grid(row=0, column=2, padx=5, pady=5, sticky='NSWE')

            class ContextMenuAddon:
                frame = ctk.CTkFrame(master=Elframe, corner_radius=5, fg_color=standartcolor[1])
                frame.grid(row=2, sticky='W')
                switch = ctk.CTkSwitch(master=frame, text='Context Menu Addon', onvalue=0, offvalue=1, text_color='white')
                switch.configure(command=lambda: RegEdit.InstallContextMenuAddon(delete=ContextMenuAddon.switch.get()))
                if RegEdit.InstallContextMenuAddon(check=1):
                    switch.select()
                switch.grid(sticky='NSWE', padx=10, pady=5)

            class ExecUser:
                def savechanges(self):
                    temp = rd.read_dump()
                    temp.update({'User': ExecUser.Userent.get()})
                    rd.create_dump(temp)

                frame = ctk.CTkFrame(master=Elframe, corner_radius=5, fg_color=standartcolor[1])
                frame.grid(row=3, sticky='W', pady=14)

                Userlabl = ctk.CTkLabel(master=frame, text='User Name', text_color='white')
                Userlabl.grid(row=0, column=0, padx=5, pady=3)

                Userent = ctk.CTkEntry(master=frame, placeholder_text='Example: User1')
                Userent.insert(0, str(rd.read_dump().get('User')))
                Userent.grid(row=0, column=1, padx=5, pady=3)

                SaveButton = ctk.CTkButton(master=frame, text='💾', hover_color='dark green',
                                                 fg_color='green', width=30, height=30, font=('Calibre', 20),
                                                 command=lambda: ExecUser.savechanges(ExecUser))
                SaveButton.grid(row=0, column=2, padx=5, pady=5, sticky='NSWE')

        def backup(self, state):
            data = rd.read_dump()
            data: dict
            data.update({'backup_state': state})
            rd.create_dump(data)
            import backup
            backup.autorun(state)

    class Menu:
        btncolor = standartcolor[1]
        frame = None
        buttonslist = []
        mainframe = None
        items = {'Hello page': MainPage, 'RegEdit': RegEditFrame, 'Folder Control': Access, 'Settings': Settings}
        ismenuvisible = False
        btnitemsframe = None

        def __init__(self):
            super().__init__()
            self.frame = ctk.CTkFrame(master=self.mainframe, corner_radius=5, fg_color=standartcolor[1])
            self.frame.grid(row=0, column=0, sticky='NS', pady=8, padx=8)
            menubtn = ctk.CTkButton(master=self.frame, text='≡', font=('Arial', 27), command=self.openmenu, width=30,
                                    corner_radius=5, fg_color=standartcolor[1], hover_color=standartcolor[1][::-1])
            menubtn.grid(row=0, column=0, pady=5, padx=5)

            self.opconffile = ctk.CTkButton(master=self.frame, text='Open Configuration File', corner_radius=5,
                                            width=30, fg_color=standartcolor[1], hover_color=standartcolor[1][::-1],
                                            command=lambda : webbrowser.open('config.SUCF'), font=('Arial', 12))
            self.addmenuitems()




        def addmenuitems(self):
            self.btnitemsframe = ctk.CTkFrame(master=self.frame, fg_color=standartcolor[1])
            row = 0
            i = 0
            for i in self.items.keys():
                row += 1
                self.buttonslist.append(
                    [ctk.CTkButton(master=self.btnitemsframe, text=i, fg_color=standartcolor[1],
                                   hover_color=standartcolor[1][::-1], corner_radius=5, font=('Arial', 12)), i,
                     lambda i=i: setvisible(self.items.get(i))])
                self.buttonslist[row - 1][0].configure(command=self.buttonslist[row - 1][2],
                                                       bg_color=self.buttonslist[row - 1][0].cget('fg_color'))
                self.buttonslist[row-1][0].grid(row=row, column=0, padx=5, pady=5)
            return self.btnitemsframe

        def openmenu(self):
            if self.ismenuvisible:
                self.ismenuvisible = False
                self.btnitemsframe.grid_forget()
                self.opconffile.grid_forget()

            else:
                self.ismenuvisible = True
                self.btnitemsframe.grid(row=1, column=0)
                self.opconffile.grid(column=0, sticky='S', pady=10)



    def setvisible(frame):
        for i in Menu.items.values():
            try:
                if i.visible:
                    print(f'Forget {i}')
                    i.visible = False
                    i.root.grid_forget()
            except AttributeError:
                pass
        if not frame:
            return 1
        if frame.visible:
            frame.visible = False
            frame.root.grid_forget()
        else:
            frame.visible = True
            frame()

    Menu.mainframe = app
    Menu()
    setvisible(MainPage)
    app.mainloop()