from tkinter import *

r1 = [0,0,0,0,0,0,0,0,0]
r2 = [0,0,0,0,0,0,0,0,0]
r3 = [0,0,0]
r4 = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0,0]]
b = [0,0,0,0,0,0,0,0,0,0]

# Maybe add a helper function that puts them in the right order
# Or start the lists off in the correct way
# And convert them all into INTS!

#Instead of just adding them to the list, give them a spot based on their name

def fetch(entry1, number, r1=r1):
    r1[number] = entry1.get()
    print("r1")
    print(r1)
    
def fetch2(entry1, number, r2=r2):
    r2[number] = entry1.get()
    print("r2")
    print(r2)

def fetch3(entry1, number, r3=r3):
    r3[number] = entry1.get()
    print("r3")
    print(r3)

def scorelist(r1=r1, r2=r2,r3=r3,r4=r4):
    for i in range (0, 9, 1):
        for j in range(0, 2, 1):
            if j == 0:
                r4[i][j] = int(r1[i])
            else:
                r4[i][j] = int(r2[i])
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            if j==0:
                r4[9][0] = int(r3[j])
            elif j==1:
                r4[9][1] = int(r3[j])
            else: 
                r4[9][2] = int(r3[j])
    print(r4)
            
    

Label(text = "Welcome to Bowling!").grid(row = 0, column = 1)
Label(text = "Type in Your Scores Below").grid(row = 0, column = 2)

List = ["Frame 1", "Frame 2", "Frame 3", "Frame 4", "Frame 5", "Frame 6", "Frame 7", "Frame 8", "Frame 9", "Frame 10"] 
Label(text = "Roll 1").grid(row = 1, column = 1)
Label(text = "Roll 2").grid(row = 1, column = 2)
Label(text = "Roll 3").grid(row = 1, column = 3)

for i in range(0, 10, 1):
    Label(text = List[i]).grid(row = i+ 2, column = 0)
    

#Absolutely have to use dictionaries- bind a function to an instance, where the functions input
# is the instance itself? 
# Am I going about this the wrong way?


a11 = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"]
a1 = {"B1":0, "B2":0, "B3":0, "B4":0, "B5":0, "B6":0, "B7":0, "B8":0, "B9":0}

a22 = ["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9"]
a2 = {"b1":0, "b2":0, "b3":0, "b4":0, "b5":0, "b6":0, "b7":0, "b8":0, "b9":0}

a33 = ["b1", "b2", "b3"]
a3 = {"b1":0, "b2":0, "b3":0}
 
for i in range(0,9,1):
    a1[a11[i]] = Entry(relief = SUNKEN, width = 25)
    a1[a11[i]].grid(row = i+2, column = 1)
    a1[a11[i]].insert(0, "0")
    a1[a11[i]].focus()
    
    # a1[a11[i]].bind('<Return>', lambda event: fetch(a1[a11[i]]) )
    # Why is this problematic in the for loop?
    
    a2[a22[i]] = Entry( relief = SUNKEN, width = 25)
    a2[a22[i]].grid(row = i+2, column = 2)
    a2[a22[i]].insert(0, "0")
    a2[a22[i]].focus()
    # a2[a22[i]].bind('<Return>', lambda event: fetch(a2[a22[i]]) )
    
a1[a11[0]].bind('<Return>', lambda event: fetch(a1[a11[0]], 0))
a1[a11[1]].bind('<Return>', lambda event: fetch(a1[a11[1]], 1))
a1[a11[2]].bind('<Return>', lambda event: fetch(a1[a11[2]], 2))
a1[a11[3]].bind('<Return>', lambda event: fetch(a1[a11[3]], 3))
a1[a11[4]].bind('<Return>', lambda event: fetch(a1[a11[4]], 4))
a1[a11[5]].bind('<Return>', lambda event: fetch(a1[a11[5]], 5))
a1[a11[6]].bind('<Return>', lambda event: fetch(a1[a11[6]], 6))
a1[a11[7]].bind('<Return>', lambda event: fetch(a1[a11[7]], 7))
a1[a11[8]].bind('<Return>', lambda event: fetch(a1[a11[8]], 8))

a2[a22[0]].bind('<Return>', lambda event: fetch2(a2[a22[0]], 0))
a2[a22[1]].bind('<Return>', lambda event: fetch2(a2[a22[1]], 1))
a2[a22[2]].bind('<Return>', lambda event: fetch2(a2[a22[2]], 2))
a2[a22[3]].bind('<Return>', lambda event: fetch2(a2[a22[3]], 3))
a2[a22[4]].bind('<Return>', lambda event: fetch2(a2[a22[4]], 4))
a2[a22[5]].bind('<Return>', lambda event: fetch2(a2[a22[5]], 5))
a2[a22[6]].bind('<Return>', lambda event: fetch2(a2[a22[6]], 6))
a2[a22[7]].bind('<Return>', lambda event: fetch2(a2[a22[7]], 7))
a2[a22[8]].bind('<Return>', lambda event: fetch2(a2[a22[8]], 8))

# 10th Frame:

ten1 = Entry(relief= SUNKEN, width = 25)
ten1.grid(row = 11, column = 1)
ten1.insert(0, "0")
ten1.focus()
ten1.bind('<Return>', (lambda event: fetch3(ten1, 0)))

ten2 = Entry(relief= SUNKEN, width = 25)
ten2.grid(row = 11, column = 2)
ten2.insert(0, "0")
ten2.focus()
ten2.bind('<Return>', (lambda event: fetch3(ten2, 1)))

ten3 = Entry(relief= SUNKEN, width = 25)
ten3.grid(row = 11, column = 3)
ten3.insert(0, "0")
ten3.focus()
ten3.bind('<Return>', (lambda event: fetch3(ten3, 2)))

tenlist = [ten1, ten2, ten3]


Label(text = "Total Score ").grid(row = 12, column = 0)


'''
def Algorithm(r4=r4):
    b = [0,0,0,0,0,0,0,0,0,0]
    for i in range(0, 10, 1):
        if i==9:
            b[i] = sum(r4[i])
        else:
            # Strike
            if r4[i][0] == 10:
                if r4[i+1][0] == 10:
                    if r4[i+2][0] == 10:
                        b[i] = 30
                    else:
                        b[i] = r4[i][0] + r4[i+1][0] + r4[i+2][0]
                else:
                    b[i] = r4[i][0] + r4[i+1][0] + r4[i+1][1]
            # spare    
            elif r4[i][0] + r4[i][1] == 10:
                b[i] = r4[i][0] + r4[i][1] + r4[i+1][0]
               
            # Nothing
            else:
                b[i] = r4[i][0] + r4[i][1]
    return(sum(b))
     '''
            

def Algorithm(r4=r4, b=b):
        
        for i in range(0, 10, 1):
            if i==9:
                b[i] = sum(r4[i])
            elif i==8:
                #Strike
                if r4[i][0] == 10:
                    if r4[i+1][0] == 10:
                        if r4[i+1][1] == 10:
                            b[i] = 30
                        else:
                            b[i] = r4[i][0] + r4[i+1][0] + r4[i+1][1]
                    else:
                        b[i] = r4[i][0] + r4[i+1][0] + r4[i+1][1]
                # spare    
                elif r4[i][0] + r4[i][1] == 10:
                    b[i] = r4[i][0] + r4[i][1] + r4[i+1][0]
                   
                # Nothing
                else:
                    b[i] = r4[i][0] + r4[i][1]
            elif i == 7: 
                if r4[i][0] == 10:
                    if r4[i+1][0] == 10:
                        if r4[i+2][0] == 10:
                            b[i] = 30
                        else:
                            b[i] = r4[i][0] + r4[i+1][0] + r4[i+2][0]
                    else:
                        b[i] = r4[i][0] + r4[i+1][0] + r4[i+1][1]
                # spare    
                elif r4[i][0] + r4[i][1] == 10:
                    b[i] = r4[i][0] + r4[i][1] + r4[i+1][0]
                   
                # Nothing
                else:
                    b[i] = r4[i][0] + r4[i][1]
            else:
                # Strike
                if r4[i][0] == 10:
                    if r4[i+1][0] == 10:
                        if r4[i+2][0] == 10:
                            b[i] = 30
                        else:
                            b[i] = r4[i][0] + r4[i+1][0] + r4[i+2][0]
                    else:
                        b[i] = r4[i][0] + r4[i+1][0] + r4[i+1][1]
                # spare    
                elif r4[i][0] + r4[i][1] == 10:
                    b[i] = r4[i][0] + r4[i][1] + r4[i+1][0]
                   
                # Nothing
                else:
                    b[i] = r4[i][0] + r4[i][1]
            
    
        print("Before the algorithm call")
        x = sum(b)
        print("after the algorithm call")
        
        Label(text = str(x)).grid(row = 12, column = 2) 
        # This needs to be updated
        

    
Score1 = Button(text = "Score it!", command = Algorithm)
Score1.grid(row = 12, column = 4)

Update = Button(text= "Update Score", command= scorelist)
Update.grid(row = 2, column = 4)
#This also needs to be updated



def LoadScore(r4=r4, a1=a1, a11=a11, a2=a2, a22=a22, tenlist=tenlist):
    for i in range(0,9,1):
        r4[i][0] = fetch(a1[a11[i]], i)
    for j in range(0,9,1): 
        r4[i][1] = fetch2(a2[a22[j]], j)
    
    
    r4[9][0] = fetch3(tenlist[0], 0)
    r4[9][1] = fetch3(tenlist[1], 1)
    r4[9][2] = fetch3(tenlist[2], 2)
    
Update1 = Button(text="Load your score", command= LoadScore)
Update1.grid(row = 3, column = 4)


def restart(r4=r4, a1=a1, a11=a11, a2=a2, a22=a22, tenlist=tenlist):
    for i in range(0, 9, 1):
        a1[a11[i]].delete('0', END)
        a1[a11[i]].insert(END, '0')
    for j in range(0,9, 1):
        a2[a22[j]].delete('0', END)
        a2[a22[j]].insert(END, '0')
    tenlist[0].delete('0', END)
    tenlist[0].insert(END, '0')
    tenlist[1].delete('0', END)
    tenlist[1].insert(END, '0')
    tenlist[2].delete('0', END)
    tenlist[2].insert(END, '0')
    
restart1 = Button(text="Restart the game", command = restart)
restart1.grid(row = 4, column = 4)
    
mainloop()


'''
Needing to hit enter? Multiple inputs?
Scoring it
The Get Method Gives you Strings
The 10th Frame has three rolls when you score it
Ask Int and Ask Str for Entry
If People Put more than one value, the list just gets bigger, rather than adjusting
(So Use Dictionaries)
Why didn't the naming work the first time around?
'''

# Maybe also store a list with all the names in the dictionary, in order 
'''
class Entry:
    def __init__(self, frame, roll, reference): 
        self.frame = frame
        self.roll = roll
        self.reference = reference

for i in range(0,10,1):
    a1["Roll" + str(i)] = Entry(relief= SUNKEN, width=25)
    a1["Roll].grid(row = i+2, column = 1)
    a1[i].insert(0, "")
    a1[i].focus()
    
Roll12 = 0
Roll21 = 0
Roll22 = 0
Roll31 = 0
Roll32 = 0
Roll41 = 0
Roll42 = 0
Roll51 = 0
Roll52 = 0
Roll61 = 0
Roll62 = 0
Roll71 = 0
Roll72 = 0
Roll81 = 0
Roll82 = 0
Roll91 = 0
Roll92 = 0
Roll101 = 0
Roll102 = 0
Roll103 = 0
'''