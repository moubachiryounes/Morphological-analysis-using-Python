# -*- coding: utf-8 -*-
"""
Spyder Editor

Created on Thu Oct 10 2013

@author: younes

This is a temporary script file.
"""

"morphlogical analyses on Product Design Specification "
#=============main modules imported=================

import tkinter 
import tkinter.filedialog  as filedialog 
import tkinter.ttk as ttk
import Pmw
import pickle
 
#=============   used variable for incrimentation   ========

Data=[]  #list of instances
Data1=[] #list of Entries
Data1S=[] #list of Scores
CollectDualitiesInTk=[] 
CollectDualities=[]
Data3=[] #list of Label in analysing process
Data_0_1=[] # triangle matrice of ones and zero coresspending to dualities
Data_Bron_Kerbosch=[]
count=0
#===========Add Class Main criterion + parametre Object  =========================

class AddMainClass :
    
    def __init__(self,parent,Nmain,Npara=2):
        self.parent=parent
        self.Nmain=Nmain
        self.Npara=Npara
        self.button=ttk.Button(parent,text='Add Specifications',command=self.AddParameter)
        E1=self.entry=ttk.Entry(parent,foreground="red",width=25)
        self.button.grid(row=0,column=Nmain)
        self.entry.grid(row=1,column=Nmain)
        self.a=len(Data1)
        Data1.append([E1])
        Data1S.append([E1])

    def AddParameter(self):
        E2=tkinter.Frame(self.parent)
        E3=tkinter.Entry(E2,width=20)
        E4=tkinter.Entry(E2,width= 5)
        E2.grid(row=self.Npara,column=self.Nmain)
        E3.pack(side="left")
        E4.pack(side="left")
        Data1[self.a].append(E3)
        Data1S[self.a].append(E4)
        self.Npara+=1
        
#============Duality Cheker Frame element (in the Toplevel1)========================
        

class dualityChecker(tkinter.Frame) :
    def __init__(self, master,text1,text2):
        tkinter.Frame.__init__(self, master)
        self.text1=text1
        self.text2=text2
        self.var = tkinter.IntVar()
        self.firstParameter= tkinter.Label(self,text=self.text1, width=60,height=3,relief="groove",wraplength=400)
        self.firstParameter.pack()
        self.SecondParameter= tkinter.Label(self,text=self.text2,width=60,height=3,relief="groove",wraplength=400)
        self.SecondParameter.pack()
        self.checkbutton = tkinter.Checkbutton(self, text="check incompatibility",variable=self.var)#,command=self.cb)
        self.checkbutton.pack()


#============Data Treatment Classt (in the Toplevel2)========================


class DataTreatmentClass():
    def __init__(self, master,text3,Nmain1,Npara1,position=-1):
       self.text3=text3 
       self.position=position
       self.Nmain1=Nmain1
       self.Npara1=Npara1
       self.label=tkinter.Label(master,text=text3,width=15,height=3,relief="raised",wraplength=150 )#SUNKEN, RAISED, GROOVE, and RIDGE
       self.label.bind("<Button-1>", self.checker)
       self.label.grid(row=self.Npara1,column=self.Nmain1)
       
    def checker (self,event) :
 
        h=0
        e=0
        
#=======>#  if the label is red or head main of parameters  do noting 
     
        if Data3[self.Nmain1][self.Npara1].label.cget("bg")=="red": 
            pass
        elif   self.Npara1==0: 
            for u in range(len(Data3)):
                    for j in range (len(Data3[u])) :                                   
                        Data3[u][j].label.config(bg="SystemButtonFace")
                        
#=======># if it is blue turn it to red and check only the blue one's   
        elif Data3[self.Nmain1][self.Npara1].label.cget("bg")=="blue": 

        # check the first side of the triangle matrice Data_0_1
            for u in range(len(Data3)): 
                if u<self.Nmain1:
                    h=h+(len(Data3[u])-1)
                    for k in range (len (Data3[u])-1) :
                        if Data3[u][k+1].label.cget("bg")=="blue" and Data_0_1[u][k][self.position-h]==1 :
                            Data3[u][k+1].label.config(bg="SystemButtonFace")
              
                elif u==self.Nmain1 :
                    for g in range (len (Data3[u])-1) : 
                       if g+1==self.Npara1:  # return the cliked one to red
                           Data3[u][g+1].label.config(bg="red")  
                
                else : # check the second side of the  triangle matrice Data_0_1
                    
                    for j in range (len(Data3[u])-1) :
                         if Data3[u][j+1].label.cget("bg")=="blue" and Data_0_1[self.Nmain1][self.Npara1-1][e+j]==1 :    # if it is blue turn it to red and check only the blue one's
                            Data3[u][j+1].label.config(bg="SystemButtonFace")
                         else:
                            pass

                    e=e+(len(Data3[u])-1)
                    
#=======>#  if cliqing in a new label with system color       
        else :  
               # turn all label to system color  
                for u in range(len(Data3)):
                    for j in range (len(Data3[u])) :                                   
                        Data3[u][j].label.config(bg="SystemButtonFace")

                   # Check the first side of the matrice (left Nmain1)
                
                for u in range(len(Data3)):                    
                    if u<self.Nmain1:
                        h=h+(len(Data3[u])-1)
                        for k in range (len (Data3[u])-1) :
                            if Data_0_1[u][k][self.position-h]==0 :
                                Data3[u][k+1].label.config(bg="blue")
                            else:
                                pass        
                      # Check the Nmain1 of the matrice (left Nmain1)
                    elif u==self.Nmain1 :
                        for g in range (len (Data3[u])-1) :
                            if g+1==self.Npara1 :
                                Data3[u][g+1].label.config(bg="red") #turn the cliquedone to red 
                            else :    #the others to blue
                                Data3[u][g+1].label.config(bg="blue")
                    else :                       
                        for j in range (len(Data3[u])-1) :                            
                            if Data_0_1[self.Nmain1][self.Npara1-1][e+j]==0  :                                
                                Data3[u][j+1].label.config(bg="blue")
                            else:
                                pass       
                        e=e+(len(Data3[u])-1)        

#============= function for used Botton  ================

    #============Add Main Parameters=======================


def AddMain ():
    #Matrice that hold the instances of addMainClass
    Data.append(AddMainClass(parent=interiorMainScrolledFrame ,Nmain=len(Data)))

    #=============Data Exhibition Function============  
	
def showValue ():
    
    ms=tkinter.Toplevel( root )
    for p in range(len(Data1)):        
        tkinter.Label(ms  , text= p+1 ).grid(row=p,column=0)                        # number of the parameter                                                                               # the parameter
        for i in range (len (Data1[p])) :
            tkinter.Label(ms  , text=str(Data1[p][i].get()) ,width=20,height=4,relief="raised",wraplength=150 ).grid(row=p,column=i+2)
	
    #===============clear work=====================

def clear():
    
    global Data1S,MainScrolledFrame, Data, Data1,Data_0_1, interiorMainScrolledFrame,CollectDualitiesInTk,CollectDualities
    MainScrolledFrame.destroy()

    Data=[]
    Data1=[]
    Data1S=[]
    CollectDualitiesInTk=[] 
    CollectDualities=[]
    Data_0_1=[]

    MainScrolledFrame =  Pmw.ScrolledFrame()
    MainScrolledFrame._clipper.config(width=500, height = 500)
    MainScrolledFrame.interior().configure(height=300, width=300,)
    interiorMainScrolledFrame=MainScrolledFrame.interior()

    MainScrolledFrame.pack(fill="both" ,expand=1)

    #===============AnnalyseData================

def AnnalyseData() :
    
    global CollectDualitiesInTk,m,CollectDualities,DataMain,DataScore
    DataScore=[]
    DataMain=[]
    m=0
    CollectDualitiesInTk=[]   

            #===============NextDuality================
    
    def NextDuality():
        
        global m        
        CollectDualitiesInTk[m].pack_forget()
        if m==len(CollectDualitiesInTk)-1:
            m=-len(CollectDualitiesInTk)
        else:
            m+=1
        CollectDualitiesInTk[m].pack(side="top")
        
            #===============PreviousDuality================
        
    def PreviousDuality():
        
        global m        
        CollectDualitiesInTk[m].pack_forget()
        if m==-len(CollectDualitiesInTk):
            m=len(CollectDualitiesInTk)-1
        else:
            m-=1
        CollectDualitiesInTk[m].pack(side="top")
        
                   #===============SaveDuality================
        
    def SaveDuality():
        
        global CollectDualities
        CollectDualities=[]
        for i in range(len (CollectDualitiesInTk)):
            CollectDualities.append([CollectDualitiesInTk[i].text1,CollectDualitiesInTk[i].text2,CollectDualitiesInTk[i].var.get()])
                
                #===============TreatmentOfDuality================

    def TreatmentOfDuality():
        
        global CollectDualities ,Data3 ,Data_0_1

        TreatmentOfDualitywindow=tkinter.Toplevel()
        analyseScrolledFrame =  Pmw.ScrolledFrame(TreatmentOfDualitywindow)
        analyseScrolledFrame._clipper.config(width=500, height = 500)
        analyseScrolledFrame.interior().configure(height=300, width=300,)
        interioranalyseScrolledFrame=analyseScrolledFrame.interior()
        analyseScrolledFrame.pack(fill="both" ,expand=1)
        Data3=[]
        Data_0_1=[]#matrice of 0 and 1 (compatible or not)
        c=0
        for i in range (len(DataMain)-1): 
            Data_0_1.append([])
            for p in range(1,len(DataMain[i])):
                Data_0_1[i].append([])                
                for k in range(i+1,len(DataMain)):
                    for l in range(1,len(DataMain[k])):
                        Data_0_1[i][p-1].append(CollectDualities[c][2])
                        c+=1

            #instantiation of element and storing them in Data3 
        compteur=0
        for s in range(len(DataMain)):
            Data3.append([DataTreatmentClass(interioranalyseScrolledFrame,DataMain[s][0]  ,Nmain1=s,Npara1=0)] )
            for d in range (1,len (DataMain[s])) :
                Data3[s].append(DataTreatmentClass(interioranalyseScrolledFrame,DataMain[s][d]  ,Nmain1=s,Npara1=d,position=compteur) )
                compteur+=1

                #=============== All Combinations ================    
            
    def AllCombinations():
        
            global DataMain,CollectDualities,Data_Bron_Kerbosch,count
            AllCombinationswindow=tkinter.Toplevel()
            AllCombinationsScrolledFrame =  Pmw.ScrolledFrame(AllCombinationswindow)
            AllCombinationsScrolledFrame._clipper.config(width=500, height = 500)
            AllCombinationsScrolledFrame.interior().configure(height=300, width=300,)
            interiorAllCombinationsFrame=AllCombinationsScrolledFrame.interior()
            AllCombinationsScrolledFrame.pack(fill="both" ,expand=1)
            
            Data_0_1=[]#matrice of 0 and 1 (compatible or not)
            c=0
            for i in range (len(DataMain)-1): 
                Data_0_1.append([])
                for p in range(1,len(DataMain[i])):
                    Data_0_1[i].append([])                
                    for k in range(i+1,len(DataMain)):
                        for l in range(1,len(DataMain[k])):
                            Data_0_1[i][p-1].append(CollectDualities[c][2])
                            c+=1
            ListdesParametres=[]
            Data_Bron_Kerbosch=[]
            comptku=0
            comptsu=0
            #============Creat Data Bron Kerbosch Matrice from DataMain and Data_0_1==========
            
            for nu in range(len(DataMain)):
                l=0
                for ku in range(len(DataMain[nu])-1):
                    ListdesParametres.append([DataMain[nu][ku+1],DataScore[nu][ku+1]] )
                    Data_Bron_Kerbosch.append([])
                    k=0
                    
                    for pu in range(len(DataMain)):
                        if nu==pu :
                            for su in range(len(DataMain[pu])-1):
                                if comptsu==comptku :
                                    Data_Bron_Kerbosch[comptku].append(0)
                                    comptsu=comptsu+1
                                else :
                                    Data_Bron_Kerbosch[comptku].append(1)
                                    comptsu=comptsu+1
                            
                        elif nu < pu :
                            
                            
                            for su in range(len(DataMain[pu])-1):
                                Data_Bron_Kerbosch[comptku].append(1-Data_0_1[nu][l][k])
                                comptsu=comptsu+1
                                k=k+1
                            
                        else :
                            for su in range(len(DataMain[pu])-1):
                                Data_Bron_Kerbosch[comptku].append(Data_Bron_Kerbosch[comptsu][comptku])
                                comptsu=comptsu+1

                    comptku=comptku+1
                    l=l+1
                    comptsu=0

            def N(vertex):
                return[i for i, n_v in enumerate(Data_Bron_Kerbosch[vertex]) if n_v]
            c=[]
            H=[]
            count=0
		
            def Bron_Kerbosch(r,p,x):
        
                
                if len(p) == 0 and len(x)==0 :
                    c.append(r)
                for vertex in p[:] :
                    r_new = r[:]
                    r_new.append(vertex)
                    p_new = [val for val in p if val in N(vertex)]
                    x_new = [val for val in x if val in N(vertex)]

                    Bron_Kerbosch(r_new,p_new,x_new)
                    p.remove(vertex)
                    x.append(vertex)
                                           			
            			
            Bron_Kerbosch ([],[i for i in range(len(ListdesParametres))],[])
	
            for k in range(len (c)) :
                H.append([])
                compteur=0
                for j in  range(1,len (c[k])+1):

                    compteur=compteur+float(ListdesParametres[c[k][j-1]][1])
                    H[k].append(ListdesParametres[c[k][j-1]][0])
                H[k].insert(0,compteur)
            H=sorted(H, key=lambda x: x[0])
            H.reverse()
            print("H= ",H)
            for p in range(len(H)):        
                tkinter.Label(interiorAllCombinationsFrame  , text= p+1 ).grid(row=p,column=0)                        # number of the parameter      the parameter
                for i in range (len (H[p])) :
                    tkinter.Label(interiorAllCombinationsFrame  , text=str(H[p][i]) ,width=18,height=3,relief="raised",wraplength=150 ).grid(row=p,column=i+2)
            
#            print ("Data: ",Data)  #list of instances
#            print ("Data1: ",Data1)  #list of Entries
#            print ("DataMain: ",DataMain)  #list of Entries
#            print ("CollectDualitiesInTk : ",CollectDualitiesInTk )
#            print ("CollectDualities: ",CollectDualities )
#            print ("Data3: ",Data3) #list of Label in analysing process
#            print ("Data_0_1: ",Data_0_1) # triangle matrice of ones and zero coresspending to dualities
#            print ("Data_Bron_Kerbosch: ",Data_Bron_Kerbosch) 
        
            
       
            #===============Main Function Program ================
                        
    DataAnalysingWindow=tkinter.Toplevel(root)
    for i in range (len(Data1)-1): #create the frame containing parameters in label and checkcutton
            
            if Data1[i][0].get()=="" :
                pass
            else : 
                for p in range(1,len(Data1[i])):
                     if Data1[i][p].get()=="" :
                            pass
                     else : 
                            for k in range(i+1,len(Data1)):                               
                                for l in range(1,len(Data1[k])):
                                     if Data1[k][l].get()=="":
                                         pass
                                     else : 
                                         CollectDualitiesInTk.append(dualityChecker(DataAnalysingWindow,Data1[i][0].get()+":\t"+Data1[i][p].get(),Data1[k][0].get()+":\t"+Data1[k][l].get()))       
    
    for i in range (len(Data1)): 
            
            if Data1[i][0].get()==""  :
                pass
            else : 
                
                DataMain.append([Data1[i][0].get()])
                DataScore.append([Data1[i][0].get()])
                for p in range(1,len(Data1[i])):
                     if Data1[i][p].get()=="" :
                            pass
                     else : 
                         DataMain[i].append(Data1[i][p].get())
                         if Data1S[i][p].get()=="" :
                             DataScore[i].append(0)
                         else :
                             DataScore[i].append(Data1S[i][p].get())

#    print ("DataMain :",DataMain)
#    print ("DataScore :",DataScore)
    frame2 = ttk.Frame(DataAnalysingWindow )	
    frame1 = ttk.Frame(frame2)		   
    PreviousButton=ttk.Button(frame1,text="Previous",command=PreviousDuality)
    PreviousButton.pack( side = "left")   
    SaveButton=ttk.Button(frame1,text="SaveWork",command=SaveDuality)
    SaveButton.pack( side = "left" ) 
    NextButton=ttk.Button(frame1,text="Next",command=NextDuality)
    NextButton.pack(side="left")
    frame1.pack()
       
    TreatmentOfData=ttk.Button(frame2,text="Treatement Of Data",command=TreatmentOfDuality)
    TreatmentOfData.pack(side="left")
    AllPossibleCombinations=ttk.Button(frame2,text="All Combinations",command=AllCombinations)
    AllPossibleCombinations.pack(side="left")
    frame2.pack(side = "bottom")
    CollectDualitiesInTk[m].pack(side="top")
    
##========   Add Scores   =========================    
#
#def AddScore () :
#    








#========used file function for file menu============================

    #========Save Work====================================================
	
def  SaveWork():
    q=[[],[]]   #put the data
    a=filedialog.asksaveasfilename()# file location    -initialdir, -mustexist, -parent, or -title)defaultextension, filetypes, initialdir, initialfile, multiple, message, parent, title
    for p in range(len(Data1)):
        q[0].append([])
        for i in range (len (Data1[p])) :
            q[0][p].append(str(Data1[p][i].get() )) 
    for p in range(len(Data1)):
        q[1].append([])
        for i in range (len (Data1[p])) :
            q[1][p].append(str(Data1S[p][i].get() )) 
    print(q)
    with open(a,'wb+')as f:
        pickle.dump(q, f, pickle.HIGHEST_PROTOCOL)
    f.close()

    
    #=========Open File=============================================
    
def OpenFile():
    global fileLocation, Data   
	
    fileLocation=filedialog.askopenfilename() 
	
    with open(fileLocation,'rb') as f:  # The protocol version used is detected automatically, so we do not have to specify it.  
          LoadedData = pickle.load(f)
    f.close()
   
    for p in range(len(LoadedData[0])):       
        Data.append(AddMainClass(parent=interiorMainScrolledFrame ,Nmain=len(Data)) )
        Data1[p][0].insert("end",LoadedData[0][p][0])
 
        for i in range (1 ,len (LoadedData[0][p])) :
            Data[p].AddParameter()
            Data1[p][i].insert("end",LoadedData[0][p][i])
            Data1S[p][i].insert("end",LoadedData[1][p][i])
			
     #def About():

#=============Main Program=========================

       #====Main Window ===============================

root = tkinter.Tk()
root.geometry("900x450+50+50")
root.title(" DS analyser ")

      #====  Buttons  ====================================
FrameMaster=tkinter.Frame(root)
AddNewMainB =ttk.Button(FrameMaster,text="Add cluster",command=AddMain)
AddNewMainB.pack(side='left',padx=15) 

Clear=ttk.Button(FrameMaster,text="clear All",command=clear)
Clear.pack(side='left',padx=5) 

showValueB=ttk.Button(FrameMaster,text='show data',command=showValue)  
showValueB.pack(side='left',padx=5) 

AnnalyseDataB=ttk.Button(FrameMaster,text='Data Analysis',command=AnnalyseData)  
AnnalyseDataB.pack(side='left',padx=5) 


FrameMaster.pack(pady=15)

      #========= Main Frame of work =======================

MainScrolledFrame =  Pmw.ScrolledFrame()
MainScrolledFrame._clipper.config(width=500, height = 500)
MainScrolledFrame.interior().configure(height=300, width=300,)
interiorMainScrolledFrame=MainScrolledFrame.interior()
MainScrolledFrame.pack(fill='both',  expand=1,pady=5)

    #======================  Head Bar  =================

menu = tkinter.Menu(root)
root.config(menu=menu)
filemenu = tkinter.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save",command=SaveWork)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.destroy)
helpmenu = tkinter.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...",)# command=About)

root.mainloop()
