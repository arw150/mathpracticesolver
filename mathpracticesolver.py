#IMPORTANT, Before Each Run, press the square to interupt the kernel, press the rewind symbol to restat, then press run

import tkinter
import pprint
from sympy import symbols, sin, pi, pprint, latex, Limit, limit, Integral, oo, integrate, diff
import tkinter.font as font
from tkinter import messagebox
import random
global loopstage
global button_correct_xcoord
global answerlocations
global button_false1_xcoord
global button_false2_xcoord 
loopstage = 0
x_symbolic = symbols('x')
sinc = sin(pi * x_symbolic) / (pi * x_symbolic)

def stringify_exponent(n, m):
    superscripted = "".join(_DIGITS[int(d)] for d in str(m))
    return f"{n}{superscripted}"
def correctanswer():  
    messagebox.showinfo('Correct!', 'You got it right, on to the next step!')
    global loopstage
    global questionbuttontext
    
    loopstage = loopstage + 1
    if (loopstage ==1):
        Current_step['text'] = Problem1_Step2_question
        button_correct['text'] = Problem1_Step2_First_Correct_Answer
        button_false1['text'] = Problem1_Step2_First_Wrong_Answer
        button_false2['text'] = Problem1_Step2_Second_Wrong_Answer
        picklocations()
    if (loopstage == 2):
        Current_step['text'] = Problem1_Step3_question
        button_correct['text'] = Problem1_Step3_First_Correct_Answer
        button_false1['text'] = Problem1_Step3_First_Wrong_Answer
        button_false2['text'] = Problem1_Step3_Second_Wrong_Answer
        picklocations()
    if (loopstage == 3):
        Current_step['text'] = Problem_Final_Answer
        button_correct['text'] = Problem1_Final_Answer_First_Correct_Answer
        button_false1['text'] = Problem1_Final_Answer_First_Wrong_Answer
        button_false2['text'] = Problem1_Final_Answer_Second_Wrong_Answer
        Choosenext_textbox['text'] = gotitright
        picklocations()
        
def getquestionbuttontext():
    global loopstage
    global questionbuttontext
    if (loopstage == 0):
        questionbuttontext = Problem1_Step1_question
    if (loopstage == 1):
        questionbuttontext = Problem1_Step2_question
    #return questionbuttontext
def wronganswer():
    messagebox.showinfo('Incoreect', 'Nope not right try again!')
    

    
    
#LOOPS FOR RANDOMLY CHOOSING LOCATION OF BOXES BETWEEN THREE X VALUES BELOW
def picklocations():
    global answerlocations
    global button_correct_xcoord
    global button_false1_xcoord
    global button_false2_xcoord
    answerlocations = [50,400,750]
    button_correct_xcoord = int(random.choice(answerlocations))
    button_false1_xcoord = button_correct_xcoord
    button_false2_xcoord = button_correct_xcoord
    print(button_correct_xcoord)
    equal = False
    while (equal == False): 
        button_false1_xcoord = int(random.choice(answerlocations))
        if (button_false1_xcoord == button_correct_xcoord):
            equal = False
        else:
            equal = True
    print(button_false1_xcoord)
    equal = False
    while (equal == False):
        button_false2_xcoord = int(random.choice(answerlocations))
        if ((button_false2_xcoord == button_correct_xcoord) or (button_false2_xcoord == button_false1_xcoord)):
            equal = False
        else:
            equal = True

    print(button_false2_xcoord)
    equal = False
        
picklocations()

#LITTLE LIBRARY OF SUPERSCRIPT DIGITS

_DIGITS = [
    "\N{superscript zero}",
    "\N{superscript one}",
    "\N{superscript two}",
    "\N{superscript three}",
    "\N{superscript four}",
    "\N{superscript five}",
    "\N{superscript six}",
    "\N{superscript seven}",
    "\N{superscript eight}",
    "\N{superscript nine}"
]

#PROBLEM 1 DIFFERENT STEPS AND THEIR ANSWERS
Problem1_Step1_question = '∫½x²'
Problem1_Step1_First_Correct_Answer = '½'+'∫'+ str(stringify_exponent(x_symbolic,2))
Problem1_Step1_First_Wrong_Answer = '∫'+ '½'+ str(stringify_exponent(x_symbolic,2))
Problem1_Step1_Second_Wrong_Answer = '∫'+ '½' + str(stringify_exponent(x_symbolic,3))
Problem1_Step2_question = '½'+'∫'+ str(stringify_exponent(x_symbolic,2))
Problem1_Step2_First_Correct_Answer = '½ * ⅓' + str(stringify_exponent(x_symbolic,3))
Problem1_Step2_First_Wrong_Answer = '½ / ⅓' + str(stringify_exponent(x_symbolic,3))
Problem1_Step2_Second_Wrong_Answer = '½ * ⅓' + str(stringify_exponent(x_symbolic,4))
Problem1_Step3_question = '½ * ⅓' + str(stringify_exponent(x_symbolic,3))
Problem1_Step3_First_Correct_Answer = '⅙' + str(stringify_exponent(x_symbolic,3))
Problem1_Step3_First_Wrong_Answer = '⅙' + str(stringify_exponent(x_symbolic,4))
Problem1_Step3_Second_Wrong_Answer = '⅖' + str(stringify_exponent(x_symbolic,3))
Problem_Final_Answer = '∫½x² = ' + '⅙' + str(stringify_exponent(x_symbolic,3))
Problem1_Final_Answer_First_Correct_Answer = ''
Problem1_Final_Answer_First_Wrong_Answer = ''
Problem1_Final_Answer_Second_Wrong_Answer = ''
gotitright = 'You got it right!'


window = tkinter.Tk()
window.title("Math Practice Solver")
window.geometry("1250x750")
Current_step = tkinter.Button(window,text= Problem1_Step1_question)
Current_step['font'] = font.Font(size=50)
Current_step.pack()
Current_step.place(x=400,y=0)

Choosenext_textbox = tkinter.Button(window,text='Pick the correct next step in solving this problem')
Choosenext_textbox.pack_forget()
Choosenext_textbox['font'] = font.Font(size=25)
Choosenext_textbox.pack()
Choosenext_textbox.place(x=200,y=150)
#OPENS THE WINDOW, DISPLAYS THE BUTTONS,SETS THEIR COMMANDS AND CALL BACKS, A LOOP WILL BE PUT IN TELLING IT TO GO AGAIN 
#WITH THE NEXT STAGE OF THE PROBLEM WHEN A CORRECT ANSWER IS CHOSEN
#while (loopstage <=3):
   

#picklocations()   #THIS HAS TO MAKE THE LOCATIONS CHANGE, BUT IS CURRENTLY NOT DOING THAT

    
    
    
#THE CORRECT BUTTON
button_correct_text = Problem1_Step1_First_Correct_Answer
button_correct = tkinter.Button(window,text= button_correct_text, command=correctanswer)
button_correct.pack_forget()
button_correct['font'] = font.Font(size=50)
button_correct.pack()  
button_correct.place(x=button_correct_xcoord,y=300)
print(button_correct_xcoord)
#button_correct.grid(row = 10, column = 0)

#THE FIRST INCORRECT PROBLEM
button_false1_text = Problem1_Step1_First_Wrong_Answer
button_false1 = tkinter.Button(window,text= button_false1_text, command = wronganswer)
button_false1.pack_forget()
button_false1['font'] = font.Font(size=50)
button_false1.pack()
button_false1.place(x=(button_false1_xcoord),y=300)
print(button_false1_xcoord)

#THE SECOND INCORRECT PROBLEM
button_false2_text = Problem1_Step1_First_Wrong_Answer
button_false2 = tkinter.Button(window,text= button_false2_text, command = wronganswer)
button_false2.pack_forget()
button_false2['font'] = font.Font(size=50)
button_false2.pack()
button_false2.place(x=button_false2_xcoord, y=300)
print(button_false2_xcoord)
window.update()

if (loopstage == 3):
    window.quit()

print(loopstage)

#if()
tkinter.mainloop()


#Example Problem1 (integral of 1/2x^2) answers
#button_correct.grid(row = 10, column = 0)
#side=RIGHT, padx=300, pady=150                   
'''
print('∫')
button_widget0.pack()
button_widget1.pack()
tkinter.mainloop()
x = symbols('x')
sinc = sin(pi * x) / (pi * x)
a = pprint(Integral(sinc, (x, -oo, oo)))
#r'$\alpha > \beta$'



pprint(Limit(sinc, x, 0))
'''
