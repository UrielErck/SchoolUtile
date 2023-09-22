def main():
    import reader as rd
    import customtkinter as ctk
    standartcolor = ('#FFFFFF', '#333333')
    app = ctk.CTk(fg_color=standartcolor)
    app.resizable(width=False, height=False)
    app.title('Test')

    class RegEditFrame:
        visible = False
        root = ctk.CTkFrame(master=app, fg_color=standartcolor)
        dataEnt = []
        Elements = rd.read_dump()
        ischanged = 0

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
            self.Elements.get('RegEdit').pop(index)
            self.Elements.update({'RegEdit': self.Elements.get('RegEdit')})
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
            self.root.grid(row=0, column=1)
            self.dataEnt = []
            app.bind('<Return>', lambda event: self.save_changes())
            ElFrame = ctk.CTkScrollableFrame(master=self.root, fg_color=standartcolor)
            ElFrame.grid(row=0, column=0, sticky='E')
            savebtn = ctk.CTkButton(master=self.root, text='Save', width=20, fg_color='green', hover_color='dark green',
                                    command=self.save_changes)
            savebtn.grid(column=0, row=1, padx=10, pady=3, sticky='WS')

            addbtn = ctk.CTkButton(master=self.root, text='+', width=20, fg_color='green', hover_color='dark green',
                                    command=self.add_el)
            addbtn.grid(column=0, row=1, padx=10, pady=3, sticky='ES')

            index = 0
            for i in self.Elements.get('RegEdit'):
                print(f'Element {index}: {i}')
                tempcolor = '#154972'
                if app['bg'] == '#FFFFFF':
                    tempcolor = '#3192de'
                index += 1
                itemframe = ctk.CTkFrame(master=ElFrame, fg_color=tempcolor, corner_radius=5)
                self.dataEnt.append({
                    "itemframe": itemframe,
                    'name': ctk.CTkLabel(itemframe, text=i.get('display_name')),
                    'stateswitch': ctk.CTkSwitch(itemframe, text=None),
                    'delbtn': ctk.CTkButton(itemframe, text='×', width=30, font=('Calibre', 20), height=30, fg_color='red',
                                    corner_radius=0, hover_color='dark red',
                                            command=lambda ind=index: self.remove_el(ind-1)),
                    'index': index-1,
                })
                self.dataEnt[index-1].get('name').grid(row=0, column=0, columnspan=2, padx=5)
                if self.Elements.get('RegEdit')[index-1].get('state') in [1, '1', True, 'True']:
                    self.dataEnt[index-1].get('stateswitch').select()
                elif self.Elements.get('RegEdit')[index-1].get('state') in [0, '0', False, 'False']:
                    self.dataEnt[index-1].get('stateswitch').deselect()
                self.dataEnt[index - 1].get('stateswitch').grid(row=0, column=2)
                self.dataEnt[index - 1].get('delbtn').grid(row=0, column=3)
                itemframe.grid(column=1, row=index - 1, padx=10, pady=10)


    class Access:
        root = ctk.CTkFrame(master=app, fg_color=standartcolor)
        visible = False
        FoldersData = [i for i in rd.read_RegFolder()]
        ElData = []

        def __init__(self):
            self.ElData = []
            self.root.grid(row=0, column=1)
            index = -1
            Ellist = ctk.CTkScrollableFrame(self.root, fg_color=standartcolor)
            Ellist.grid(row=0, column=0, sticky='E')
            selectbtn = ctk.CTkButton(self.root, text='📂', width=30, font=('Calibre', 18), height=30, bg_color='transparent',
                                    corner_radius=0, hover_color='#2682cb',
                                            command=self.addel)
            selectbtn.grid(row=0, column=2, sticky='SE')
            for i in self.FoldersData:
                index += 1
                frame = ctk.CTkFrame(master=Ellist, fg_color='#154972', corner_radius=5)
                self.ElData.append({
                    'Frame': frame,
                    'Name': ctk.CTkLabel(frame, text=str(i.split("/")[-1])),
                    'DelBtn': ctk.CTkButton(frame, text='×', width=30, font=('Calibre', 20), height=30, fg_color='red',
                                    corner_radius=0, hover_color='dark red',
                                            command=lambda ind=index: self.delel(index=ind)),
                    'Path': ctk.CTkLabel(frame, text=i),
                    'Index': index,
                })
                frame, name, delbtn, path, index = self.ElData[index].values()
                frame.grid(row=index, column=0, padx=10, pady=10)
                name.grid(row=0, column=0, columnspan=2, padx=5)
                delbtn.grid(row=0, column=3, sticky='E')
                path.grid(row=1, column=0, columnspan=2, padx=5)


        def delel(self, index: int):
            print(f'del el Id:{index} Name: {self.ElData[index].get("Name").cget("text")}')
            self.ElData[index].get('Frame').grid_forget()
            self.ElData[index].get('Frame').destroy()
            self.ElData.pop(index)
            self.FoldersData.pop(index)
            Access()

        def addel(self):
            filename = ctk.filedialog.askdirectory()
            self.FoldersData.append(filename)
            print(f'filePATH: {filename}')
            self.__init__()

    class Menu:
        btncolor = ''
        frame = None
        buttonslist = []
        mainframe = None
        items = {'Hello page': None, 'RegEdit': RegEditFrame, 'Folder Control': Access}
        ismenuvisible = False
        btnitemsframe = None

        def __init__(self):
            super().__init__()
            self.frame = ctk.CTkFrame(master=self.mainframe)
            self.frame.grid(row=0, column=0, sticky='NS')
            menubtn = ctk.CTkButton(master=self.frame, text='≡', font=('Arial', 27), command=self.openmenu,
                                    width=30)
            menubtn.configure(bg_color=menubtn.cget('fg_color'))
            self.btncolor = menubtn.cget('bg_color')
            self.frame.configure(fg_color=self.btncolor)
            menubtn.grid(row=0, column=0, sticky='N')
            self.addmenuitems()


        def addmenuitems(self):
            self.btnitemsframe = ctk.CTkFrame(master=self.frame, fg_color=self.btncolor)
            row = 0
            i = 0
            for i in self.items.keys():
                row += 1
                self.buttonslist.append(
                    [ctk.CTkButton(master=self.btnitemsframe, text=i), i,
                     lambda i=i: setvisible(self.items.get(i))])
                self.buttonslist[row - 1][0].configure(command=self.buttonslist[row - 1][2],
                                                       bg_color=self.buttonslist[row - 1][0].cget('fg_color'),)
                self.buttonslist[row-1][0].grid(row=row, column=0)
            return self.btnitemsframe

        def openmenu(self):
            if self.ismenuvisible:
                self.ismenuvisible = False
                self.btnitemsframe.grid_forget()
            else:
                self.ismenuvisible = True
                self.btnitemsframe.grid(row=1, column=0)


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
    setvisible(RegEditFrame)
    app.mainloop()