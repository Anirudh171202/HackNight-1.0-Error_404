

from tkinter import  *


import pandas as pd

from sklearn import tree
from sklearn.ensemble import AdaBoostClassifier
dp = 'C:/Users/Anirudh/Desktop/mental-health-in-tech-survey/trainms.csv'
dataframe = pd.read_csv(dp)
l = []
m = []
newdf = pd.DataFrame(columns = ['Age','family_history', 'work_interfere', 'phys_health_consequence', 'mental_health_consequence', 'anonymity', 'wellness_program', 'leave', 'care_options','benefits', 'seek_help', 'treatment'])
newdf['Age'] = dataframe['Age']
for i in ['family_history', 'work_interfere', 'phys_health_consequence', 'mental_health_consequence', 'anonymity','wellness_program', 'leave', 'care_options','benefits', 'seek_help', 'treatment']:
   l = list(pd.unique(dataframe[i]))
   for j in range(1000):
       m.append(l.index(dataframe[i][j]))
   newdf[i] = m
   m = []
   l = []
xtrset = newdf[['Age', 'family_history', 'work_interfere', 'phys_health_consequence', 'mental_health_consequence', 'anonymity','wellness_program', 'leave', 'care_options','benefits', 'seek_help']]
ytrset = newdf['treatment']
print(newdf)
adb = AdaBoostClassifier(n_estimators=200, base_estimator = tree.DecisionTreeClassifier(max_depth = 3),learning_rate = 0.01, random_state=0)
adb.fit(xtrset, ytrset)


df2 = pd.DataFrame(columns = ['Age','family_history', 'work_interfere', 'phys_health_consequence', 'mental_health_consequence', 'anonymity', 'wellness_program', 'leave', 'care_options','benefits', 'seek_help'])

def save_info():
        
        fh1 = input_fh1.get()
        fh2 = int(input_fh2.get())
        g_g = g_inp.get()
        g11 = g_inp1.get()
        g22 = g_inp2.get()
        g33 = g_inp3.get()
        g44 = g_inp4.get()
        g55 = g_inp5.get()
        g66 = g_inp6.get()
        g77 = g_inp7.get()
        g88 = g_inp8.get()
        g99 = g_inp9.get()
        g00 = g_inp0.get()
        
##	file  = open ("user.txt", "a+")
##	file.write(("name : " + str(name_info)))
##	file.write(("age : " + age_info))
##	file.close()
        
        df2['Age'] = [fh2]
        df2['family_history'] = [list(pd.unique(dataframe['family_history'])).index(g11)]
        df2['work_interfere'] = [list(pd.unique(dataframe['work_interfere'])).index(g22)]
        df2['phys_health_consequence'] = [list(pd.unique(dataframe['phys_health_consequence'])).index(g33)]
        df2['mental_health_consequence'] =[list(pd.unique(dataframe['mental_health_consequence'])).index(g44)]
        df2['anonymity'] =[list(pd.unique(dataframe['anonymity'])).index(g55)]
        df2['wellness_program']=[list(pd.unique(dataframe['wellness_program'])).index(g66)]
        df2['leave']=[list(pd.unique(dataframe['leave'])).index(g77)]
        df2['care_options']=[list(pd.unique(dataframe['care_options'])).index(g88)]
        df2['benefits']=[list(pd.unique(dataframe['benefits'])).index(g99)]
        df2['seek_help']=[list(pd.unique(dataframe['seek_help'])).index(g00)]
        xtest = df2[['Age','family_history', 'work_interfere', 'phys_health_consequence', 'mental_health_consequence', 'anonymity', 'wellness_program', 'leave', 'care_options','benefits', 'seek_help']]
        ypredict = adb.predict(xtest)
        if ypredict[0] == 1:
            print("No")
            # top = Tk()
            
            
            heading = Label(text = "no", bg =  "green", fg = "black" , width = "500", height= "3")
            heading.pack()
        else:
            
            heading = Label(text = "yes", bg =  "red", fg = "black" , width = "500", height= "3")
            heading.pack()
    
        

screen = Tk()
screen.geometry("1500x1500")
screen.title("Med.io form")
heading = Label(text = "Med.io form", bg =  "grey", fg = "black" , width = "500", height= "3")
heading.pack()

####name_text = Label(text = "Enter your  name *")
####input_text = StringVar()
####name_entry = Entry(textvariable = input_text, width = "30")
####name_entry.place(x = 15, y = 70)
####
##_text = Label(text = "")
##input_ = StringVar()
##_text = Entry(textvariable = input_, width = "30")
##_text.place(x = , y = )
####
####age_text = Label(text = "Age* ")
####age_text.place(x = 15, y = 210)
fh_text1 = Label(text = "Name")
input_fh1 = StringVar()
fh_text1 = Entry(textvariable = input_fh1, width = "30")
fh_text1.place(x = 15, y = 70)
        



fh_text2 = Label(text = "Age")
input_fh2 = StringVar()
fh_text2 = Entry(textvariable = input_fh2, width = "30")
fh_text2.place(x = 350, y = 70)



g = ['Female', 'Male', 'Other'] 
g_inp = StringVar(screen)
g_inp.set(g[0]) # default value
w = OptionMenu(screen, g_inp , *g)
v = Label(w, text = "gender")
v.pack()
w.pack()
w.place(x = 15, y = 120)


g1 = ['No', 'Yes'] 
g_inp1 = StringVar(screen)
g_inp1.set(g1[0]) # default value
w = OptionMenu(screen, g_inp1 , *g1)
w.pack()
w.place(x = 15, y = 170)
#df2['family_history'].append( list(pd.unique(dataframe['family_history'])).index(.get()))



g2 = ['Often', 'Rarely', 'Never', 'Sometimes', 'nan'] 
g_inp2 = StringVar(screen)
g_inp2.set(g2[0]) # default value
w = OptionMenu(screen, g_inp2 , *g2)
w.pack()
w.place(x = 15, y = 220)




g3 = ['No', 'Yes', 'Maybe'] 
g_inp3 = StringVar(screen)
g_inp3.set(g3[0]) # default value
w = OptionMenu(screen, g_inp3 , *g3)
w.pack()
w.place(x = 15, y = 270)
##df2['phys_health_cons']= [pd.unique(dataframe['phys_health_cons']).index(g_text.get())]

g4 = ['No', 'Yes', 'Maybe'] 
g_inp4 = StringVar(screen)
g_inp4.set(g4[0]) # default value
w = OptionMenu(screen, g_inp4 , *g4)
w.pack()
w.place(x = 15, y = 320)
##df2['mental_health_cons']= [pd.unique(dataframe['mental_health_cons']).index(g_text.get())]






g5 = ['No', 'Yes', "Don't know"] 
g_inp5 = StringVar(screen)
g_inp5.set(g5[0]) # default value
w = OptionMenu(screen, g_inp5 , *g5)
w.pack()
w.place(x = 15, y = 370)
##df2['anonymity']= [pd.unique(dataframe['anonymity']).index(g_text.get())]

g6 = ['No', 'Yes', "Don't know"] 
g_inp6 = StringVar(screen)
g_inp6.set(g6[0]) # default value
w = OptionMenu(screen, g_inp6 , *g6)
w.pack()
w.place(x = 15, y = 420)
##df2['wellness_program']= [pd.unique(dataframe['wellness_program']).index(g_text.get())]

g7 = ['Somewhat easy', "Don't know", "Somewhat difficult", "Very difficult", "Very easy"] 
g_inp7 = StringVar(screen)
g_inp7.set(g7[0]) # default value
w = OptionMenu(screen, g_inp7 , *g7)
w.pack()
w.place(x = 15, y = 470)
##df2['leave']= [pd.unique(dataframe['leave']).index(g_text.get())]

g8 = ['No', 'Yes', "Not sure"] 
g_inp8 = StringVar(screen)
g_inp8.set(g8[0]) # default value
w = OptionMenu(screen, g_inp8 , *g8)
w.pack()
w.place(x = 15, y = 520 )
##df2['care_options']= [pd.unique(dataframe['care_options']).index(g_text.get())]

g9 = ['No', 'Yes', "Don't know"] 
g_inp9 = StringVar(screen)
g_inp9.set(g9[0]) # default value
w = OptionMenu(screen, g_inp9 , *g9)
w.pack()
w.place(x = 15, y = 570)
##df2['seek_h']= [pd.unique(dataframe['seek_help']).index(g_text.get())]

g0 = ['No', 'Yes', "Don't know"] 
g_inp0 = StringVar(screen)
g_inp0.set(g0[0]) # default value
w = OptionMenu(screen, g_inp0 , *g0)
w.pack()
w.place(x = 15, y = 620)




        
##l = ['No', 'Yes']
##tkvar.set('No') # set the default option
##
##popupMenu = OptionMenu(screen, tkvar, *l)
##popupMenu.drop()
##Label(mainframe, text="Choose a dish").grid(row = 1, column = 1)
##popupMenu.grid(row = 2, column =1)



# on change dropdown value
#def change_dropdown(*args):
 #   print( tkvar.get() )

##l = [] 
## = StringVar(screen)
##.set(l[0]) # default value
##
##w = OptionMenu(screen, , *l)
##w.pack()

##l = ['a','b','c'] 
##tet= StringVar(screen)
##tet.set(l[0]) # default value
##
##w = OptionMenu(screen,tet , *l)
##w.pack()



register=Button(screen, text="Register"  ,width = "30", height = "2", command = save_info, bg = "grey")
register.place (x =  15, y = 800)



