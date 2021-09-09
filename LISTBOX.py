        
    def widgets(self):  # 
               
#______________I N S T A N C I A S   M A P E A D O S  por  D E F E C T O :

        self.frm_A1 = Create_Frame (self, bg='#11161d', width=60, height=65)  # Color: Azul        --- Frame Contenedor del logo y la rueda            
        self.frm_B1 = Frame (self, bg='#31343a', width=756, height=65)        # Color: Plomo       --- Frame Contenedor del Contenedor de los Botones
        self.frm_b1 = Create_Frame (self.frm_B1, bg = '#11161d',)             # Color: Azul        --- Frame Contenedor de los Botones

        #______Posicionamiento:

        self.frm_A1 .grid (column= 0, row= 0, padx=(0,0), pady=(0,0))         # Instancia
        self.frm_B1 .grid (column= 1, row= 0, padx=0, pady=0, sticky='n')     # Frame 
        self.frm_b1 .grid (padx = (10,10), pady = (6,6))                      # Instancia

        #______Metodos de Instancias:

        self.frm_A1 .img_ash()
        self.frm_A1 .img_gear() 
        self.frm_b1 .img_moviles()

        #______Propagación:

        self.frm_A1 .grid_propagate (False)
        self.frm_B1 .grid_propagate (False)

#______________C O N F I G U R A C I O N  V I S U A L :

        #______C O N T E N E D O R : INTERFACE DE CONFIGURACION:  (NO POSICIONADO)
        self.frm_B2 = Frame (self, bg='#31343a', width=756, height=65)  # Color: Plomo
        self.frm_B2 .grid_propagate (False)

        #______W I D G E T :   L A B E L 
        label_option1 = Label (self.frm_B2, text= 'Activar Aimbot :' , font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option2 = Label (self.frm_B2, text= 'Activar aimbot :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option3 = Label (self.frm_B2, text= 'Activar ddd ', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option4 = Label (self.frm_B2, text= 'Activar Modo On :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option5 = Label (self.frm_B2, text= 'Activar Modo Lista :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option6 = Label (self.frm_B2, text= 'Activar Modo Guía :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option7 = Label (self.frm_B2, text= 'Recordar Configuracion :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)

        #______Posicionamiento Label :
        label_option1 .grid (column=0, row=0, padx= (30,10), pady=(10,0), sticky=W)
        label_option2 .grid (column=0, row=1, padx= (30,10), pady=(0,0), sticky=W)
        label_option3 .grid (column=2, row=0, padx= (30,10), pady=(10,0), sticky=W)
        label_option4 .grid (column=2, row=1, padx= (30,10), pady=(0,0), sticky=W)
        label_option5 .grid (column=4, row=0, padx= (30,10), pady=(10,0), sticky=W)
        label_option6 .grid (column=4, row=1, padx= (30,10), pady=(0,0), sticky=W)   
        label_option7 .grid (column=6, row=0, padx= (30,10), pady=(10,0), sticky=W)

        #______W I D G E T :   C H E C K B U T T O N
        self.checkbutton1 = Checkbutton_class (self.frm_B2,  bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.checkbutton2 = Checkbutton_class (self.frm_B2,  bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.checkbutton3 = Checkbutton_class (self.frm_B2,  bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.checkbutton4 = Checkbutton_class (self.frm_B2,  bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.checkbutton5 = Checkbutton_class (self.frm_B2,  bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0, command=self.cheeck_5)
        self.checkbutton6 = Checkbutton_class (self.frm_B2,  bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.checkbutton7 = Checkbutton_class (self.frm_B2,  bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
    
        #______Posicionamiento Checkbutton :
        self.checkbutton1 .grid (column=1, row=0, pady=(10,0))
        self.checkbutton2 .grid (column=1, row=1, pady=(0,0))
        self.checkbutton3 .grid (column=3, row=0, pady=(10,0))
        self.checkbutton4 .grid (column=3, row=1, pady=(0,0))
        self.checkbutton5 .grid (column=5, row=0, pady=(10,0))
        self.checkbutton6 .grid (column=5, row=1, pady=(0,0))
        self.checkbutton7 .grid (column=7, row=0, pady=(10,0))

     
#_____________SELF.CHECKBUTTON 5 :  MODO LISTA

        #_____C O N T E N E D O R E S:  (NO POSICIONADOS)
        self.frm_B3 = Frame (self, bg='#31343a', width=174, height=65)  # Color: Plomo
        self.frm_B3 .grid_propagate(False)

        self.frm_C1 = Frame (self, bg='green2', width=60, height=65)
        self.frm_C1 .grid_propagate(False)

########self.label_mini
        
        self.spinbox_variable = StringVar()
        self.spinbox_variable .trace_add ('write', lambda *arg: self.spinbox_variable.set (self.spinbox_variable.get() .capitalize()))  # SE ACTIVA SI INTRODUCE TEXTO: CAMBIA POR MAYUSCULA
        label_title = Label (self.frm_B3, text='Seleccione  Mobil :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)

        self.spinbox_values = ['Frog', 'Fox', 'Boomer', 'Ice', 'J.d', 'Grub', 'Lightning', 'Aduka', 'Knight', 'Kalsiddon', 'Mage', 'Randomizer', 'Jolteon', 'Turtle', 'Armor','A.sate', 'Raon', 'Trico', 'Nak', 'Bigfoot', 'Dragon 1', 'Dragon 2']
        self.spinbox = Spinbox (self.frm_B3, width=13, values= self.spinbox_values, textvariable=self.spinbox_variable, wrap= True)    

        self.spinbox .bind ('<Return>', self.bind_spinbox)  # SE ACTIVA SI SPINBOX TIENE FOCO, Y SE PRESIONA LA TECLA ENTER: ABRE LAS VENTANAS
        
        #self.spinbox .icursor(END)
        #______Posicionamientos:
        label_title .grid (column= 0, row=0, padx=10, pady=(10,5), sticky= W)

        self.spinbox .grid (column= 0, row=1, padx=10, pady=(0,6), sticky= W)
     
    def mini(self):
           

    def gear_stacking(self):   # SE ACTIVA CON LA RUEDA DE CONFIGURACIONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

        if  self.gear == True:         # PREDETERMINADO: TRUE
            self.frm_B1 .grid_remove()  # B1: BOTONES          
            self.frm_B3 .grid_remove()  # B3: LISTBOX    ###??? necesita if?
            self.frm_C1 .grid_remove()  # C1: MINIATURA

            self.frm_B2 .focus_set()    # NECESARIO 
            self.frm_B2 .grid (column= 1, row= 0, padx=0, pady=0, sticky= N)               
            self.gear = False      
    
        else:
            self.frm_B2 .grid_remove()
            if self.checkbutton5.variable.get() == True:   
                self.frm_B3 .grid (column= 1, row= 0, padx=0, pady=0, sticky= NW)
                self.frm_C1 .grid (column= 1, row= 0, padx=0, pady=0, sticky= NE)
                self.spinbox .focus_set()   # AKI TRABAJAR
                #self.spinbox .icursor(END)
            else:
                self.frm_B1 .grid ()
                self.frm_B3 .grid_remove()
                self.frm_C1 .grid_remove()
                
            self.gear = True            

    def cheeck_5 (self):   # SE ACTIVA MARCANDO LA CASILLA : SELF.CHEECKBUTTON 5  # ESTE METODO ESTA SIN USOOOOOOOOOOOOOOOOOO
        self.checkbutton5.value()

    def bind_spinbox (self, event):  # SE ACTIVA CUANDO SPINBOX TIENE FOCO Y SE PRESIONA LA TECLA ENTER: ABRE LAS VENTANAS
        
        left = [Frog_left_off, Fox_left_off, Boomer_left_off, Ice_left_off, Jd_left_off, Grub_left_off, Lightning_left_off, Aduka_left_off, Knight_left_off, Kalsiddon_left_off, Mage_left_off, Randomizer_left_off, Jolteon_left_off, Turtle_left_off, Armor_left_off, Asate_left_off, Raon_left_off, Trico_left_off, Nak_left_off, Bigfoot_left_off, Dragon1_left_off, Dragon2_left_off,]
        right = [Frog_right, Fox_right, Boomer_right, Ice_right, Jd_right, Grub_right, Lightning_right, Aduka_right, Knight_right, Kalsiddon_right, Mage_right, Randomizer_right, Jolteon_right, Turtle_right, Armor_right, Asate_right, Raon_right, Trico_right, Nak_right, Bigfoot_right, Dragon1_right, Dragon2_right]
        stuf = [Frog_stuf, Fox_stuf, Boomer_stuf, Ice_stuf, Jd_stuf, Grub_stuf, Lightning_stuf, Aduka_stuf, Knight_stuf, Kalsiddon_stuf, Mage_stuf, Randomizer_stuf, Jolteon_stuf, Turtle_stuf, Armor_stuf, Asate_stuf, Raon_stuf, Trico_stuf, Nak_stuf, Bigfoot_stuf, Dragon1_stuf, Dragon2_stuf]
####### lista de img : self.Miniaturas de 0 a 21
        for index, i in enumerate(self.spinbox_values):
            if self.spinbox.get() == i:
                self.windows_123(left[index], right[index], stuf[index])  
                

    def configure_height (self):  # Metodo DESABILITADO
              
        if self.frm_A1 .winfo_reqheight() == 65:
            self.frm_A1 .config (width=60, height=165)   
        else:
            self.frm_A1 .config (width=60, height=65)


    
    """ def aa(self, event):
        print('s')
        self.toplevel_LEFT.iconify()
        self.toplevel_RIGHT.iconify()
        self.toplevel_STUF.iconify()

    def bb(self, event):

        self.toplevel_LEFT.deiconify()
        self.toplevel_RIGHT.deiconify()
        self.toplevel_STUF.deiconify() """


    def remove_frame (self):  # Metodo LOGO
        

        try:
            # TRUE: VISIBLE   /   FALSE: NO VISIBLE
            if self.toplevel_LEFT.winfo_ismapped() == False and self.toplevel_RIGHT.winfo_ismapped() == False and self.toplevel_STUF.winfo_ismapped() == False:
                self.toplevel_LEFT.deiconify()   # OCULTAR MODO MINIATURA
                self.toplevel_RIGHT.deiconify()
                self.toplevel_STUF.deiconify()
            else:
                self.toplevel_LEFT.iconify()
                self.toplevel_RIGHT.iconify()
                self.toplevel_STUF.iconify()

        except Exception as err:
            print('error: 1')
        

        """try:
            if self.toplevel_RIGHT.winfo_ismapped():
                self.toplevel_RIGHT.iconify()
            else:
                self.toplevel_RIGHT.deiconify()
        except Exception as err: 
            print('error: 2')
        

        try:
            if self.toplevel_STUF.winfo_ismapped():
                self.toplevel_STUF.iconify()
            else:
                self.toplevel_STUF.deiconify()
        except Exception as err:
            print('error: 3')"""
