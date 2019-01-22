import MySQLdb
from PIL import Image
import requests
from io import BytesIO

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import AsyncImage
from kivy.loader import Loader
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class SQLsearcherApp(App):
#Application Layout
    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        self.lbl1 = Label(text="Please fill in the query below: ", height = 40)
        layout.add_widget(self.lbl1)
       
        #Select:
        Sinputs = GridLayout(cols = 4,row_force_default= True, row_default_height = 40)
        layout.add_widget(Sinputs)
        self.lbl2 = Label(text="Select: ")
        Sinputs.add_widget(self.lbl2)
        self.txt1 = TextInput(text='', multiline=False)
        Sinputs.add_widget(self.txt1)

        #From:
        Finputs = GridLayout(cols = 4,row_force_default= True, row_default_height = 40)
        layout.add_widget(Finputs)
        self.lbl3 = Label(text="From: ")
        Finputs.add_widget(self.lbl3)
        self.txt2 = TextInput(text='', multiline=False)
        Finputs.add_widget(self.txt2)

        #Where:
        Winputs = GridLayout(cols = 2, row_force_default = True, row_default_height = 40)
        layout.add_widget(Winputs)
        self.lbl4 = Label(text= "Where: ")
        Winputs.add_widget(self.lbl4)
        self.txt3 = TextInput(text='', multiline=False)
        Winputs.add_widget(self.txt3)

        #Execute
        btn1 = Button(text="Execute")
        btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)

        #Results
        self.Result = Label(text = "Results: ")
        layout.add_widget(self.Result)

        self.aimg = AsyncImage(source = "" )
        layout.add_widget(self.aimg)
        
        return layout

#OnButtonClick - Execute
    def buttonClicked(self,btn):
        query = "Select " + self.txt1.text + " From " + self.txt2.text + " Where " + self.txt3.text
        self.Result.text = "Results: " + self.QueryFinder(query)
        if self.UrlFinder(self.txt2.text,self.txt3.text) == 'None':
            self.aimg.source = ""
        else:
            self.aimg.source = self.UrlFinder(self.txt2.text,self.txt3.text) 


#MySQL connection
    def QueryFinder(self,query):
        #Database information removed for GitHub upload
        db = MySQLdb.connect(host = "Nothing", user = "to", passwd = "see", db = "here")
        cur = db.cursor()
        statement = str(query)
        try:
            cur.execute(statement)
        except TypeError:
            error = "There's been an error in the SQL syntax"
            return error

        #Extra code to count number of attributes to be returned
        temp = statement.split(",")
        retNum = len(temp)
        print(retNum)

        info = ""
        
        for row in cur.fetchall():
            print(str(row))
            info= info + str(row) + " "
        return info

#Find URL
    def UrlFinder(self, tables, where):
        db = MySQLdb.connect(host = "these", user = "values", passwd = "are", db = "placeholders")
        cur = db.cursor()
        statement = "Select ImageURL From "+str(tables)+" Where " +str(where)
        try:
            cur.execute(statement)
        except TypeError:
            error = "There's been an error in the SQL syntax"
            return error
        for row in cur.fetchall():
            print(str(row[0]))
            url= str(row[0])
        return url

        
#Run
if __name__ == "__main__":
    SQLsearcherApp().run()
