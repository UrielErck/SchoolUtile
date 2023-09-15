def main():
    import reader as rd
    import customtkinter as ctk
    standartcolor = ('#FFFFFF', '#333333')
    app = ctk.CTk(fg_color=standartcolor)
    app.resizable(width=False, height=False)
    app.title('Test')

    class Menu:
        btncolor = ''
        frame = None
        buttonslist = []
        mainframe = None
        items = {'Hello page': None, 'RegEdit': None}
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
                def tempcommand():
                    self.openel(self.items.get(str(i)))
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

    class RegEditFrame:
        visible = False
        root = ctk.CTkFrame(master=app, fg_color=standartcolor)
        dataEnt = []
        Elements = rd.read_dump()
        ischanged = 0

        def remove_el(self, index):
            print('triggerred')
            self.dataEnt[index].get("itemframe").destroy()
            self.dataEnt.pop(index)
            self.Elements.get('RegEdit').pop(index)
            self.Elements.update({'RegEdit': self.Elements.get('RegEdit')})
            rd.create_dump(self.Elements)
            return 0

        def save_changes(self):
            print(self.visible)
            if not self.visible:
                return 1
            self.ischanged = 1
            for i in range(len(self.dataEnt)):
                state = self.dataEnt[i].get('stateswitch').get()
                self.Elements.get('RegEdit')[i].update({'state': state})
                rd.create_dump(self.Elements)
            return 0

        def __init__(self):
            super().__init__()
            self.root.grid(row=0, column=1)
            app.bind('<Return>', lambda event: self.save_changes())
            ElFrame = ctk.CTkFrame(self.root, fg_color=standartcolor)
            index = 0
            savebtn = ctk.CTkButton(self.root, text='Save', width=20, fg_color='green', hover_color='dark green',
                                    command=self.save_changes)
            savebtn.grid(column=0, row=1, padx=10, pady=3, sticky='WS')

            for i in self.Elements.get('RegEdit'):
                index += 1
                itemframe = ctk.CTkFrame(ElFrame, fg_color='#154972', corner_radius=5)
                itemframe.grid(column=1, row=index-1, padx=10, pady=10)
                self.dataEnt.append({
                    "itemframe": itemframe,
                    'name': ctk.CTkLabel(itemframe, text=i.get('display_name')),
                    'stateswitch': ctk.CTkSwitch(itemframe, text=''),
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
            ElFrame.grid(row=0, column=0, padx=1, pady=1)




    def setvisible(frame):
        for i in Menu.items.values():
            print(i)
            try:
                if i.visible:
                    i.visible = False
                    i.root.grid_forget()
            except AttributeError:
                pass
        if not frame:
            return 1
        if not frame.visible:
            frame.visible = True
            frame()
        else:
            frame.visible = False
            frame.root.grid_forget()

    Menu.mainframe = app
    Menu()
    setvisible(RegEditFrame)
    app.mainloop()
if __name__ == '__main__':
    main()