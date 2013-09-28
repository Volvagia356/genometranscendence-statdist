import statdist
import Tkinter
import tkMessageBox
import tkSimpleDialog

attributes=["STR","DEX","AGI","STA","FOR","COM","INT","WIS","PER","CHA","WIL","PSY",]
default_points=600

stats=statdist.StatDist(attributes,default_points)

class Application(Tkinter.Frame):
    def __init__(self,master=None):
        Tkinter.Frame.__init__(self,master)
        master.title("Genome Transcendence Stat Distributor")
        master.resizable(0,0)
        self['padx']=10
        self['pady']=10
        self.pack()
        self.create_widgets()
        self.update_values()

    def create_widgets(self):
        self.frames=[]
        self.total_label=Tkinter.Label(self)
        self.total_label.pack({'side':'top'})
        self.change_total=Tkinter.Button(self)
        self.change_total['text']="Change"
        self.change_total['command']=change_total
        self.change_total.pack({'side':'top'})
        for attr in stats.attributes:
            #Generate LabelFrame
            frame=AttributeFrame(self,attr)
            self.frames.append(frame)
    
    def update_values(self):
        for frame in self.frames:
            frame.update_value()
        self.total_label['text']="Points Remaining: {}/{}".format(stats.points,stats.total_points)
        

class AttributeFrame(Tkinter.LabelFrame):
    def __init__(self,master,attr):
        #Init self
        Tkinter.LabelFrame.__init__(self,master)
        self['text']=attr
        self.pack({'side':'top'})
        ##Generate -10 button
        self.sub_ten=AdjustButton(self,attr,"-10")
        #Generate -1 button
        self.sub_one=AdjustButton(self,attr,"-1")
        #Generate value
        self.value=Tkinter.Label(self)
        self.value['text']="0"
        self.value['width']=4
        self.value.pack({'side':'left'})
        #Generate +1 button
        self.add_one=AdjustButton(self,attr,"+1")
        #Generate +10 button
        self.add_ten=AdjustButton(self,attr,"+10")
    
    def update_value(self):
        self.value['text']=str(stats.attributes[self['text']])

class AdjustButton(Tkinter.Button):
    def __init__(self,master,attr,amount):
        Tkinter.Button.__init__(self,master)
        self['text']=amount
        self['command']=get_adj_point_func(attr,int(amount))
        self.pack({'side':'left'})

def change_total():
    global stats,attributes,app
    new_total=tkSimpleDialog.askinteger("Change Total","Enter a new total:")
    if new_total==None: return False
    if new_total<0: new_total=0
    stats=statdist.StatDist(attributes,new_total)
    app.update_values()

def get_adj_point_func(attr,amount):
    def adj_point_func():
        try:
            stats.adj_point(attr,amount)
        except (statdist.StatPointError):
            tkMessageBox.showerror("Error","Not enough points")
        app.update_values()
    return adj_point_func

root=Tkinter.Tk()
app=Application(master=root)
app.mainloop()