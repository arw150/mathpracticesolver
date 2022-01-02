#IMPORTANT, Before Each Run, press the square to interupt the kernel, press the rewind symbol to restat, then press run

import tkinter
import pprint
from sympy import symbols, sin, pi, pprint, latex, Limit, limit, Integral, oo, integrate, diff
import tkinter.font as font
from tkinter import messagebox
import random

x_symbolic = symbols('x')
sinc = sin(pi * x_symbolic) / (pi * x_symbolic)

def stringify_exponent(n, m):
    superscripted = "".join(_DIGITS[int(d)] for d in str(m))
    return f"{n}{superscripted}"
def correctanswer():  
    messagebox.showinfo('Correct!', 'You got it right, on to the next step!')
    loop = False
    
def wronganswer():
    messagebox.showinfo('Incoreect', 'Nope not right try again!')

    
    
#LOOPS FOR RANDOMLY CHOOSING LOCATION OF BOXES BETWEEN THREE X VALUES BELOW
    
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
Problem1_question = '∫½x²'
Problem1_First_Correct_Answer = '½'+'∫'+ str(stringify_exponent(x_symbolic,2))
Problem1_First_Wrong_Answer = '∫'+ '½'+ str(stringify_exponent(x_symbolic,2))
Problem1_Second_Wrong_Answer = '∫'+ '½' + str(stringify_exponent(x_symbolic,3))



#OPENS THE WINDOW, DISPLAYS THE BUTTONS,SETS THEIR COMMANDS AND CALL BACKS, A LOOP WILL BE PUT IN TELLING IT TO GO AGAIN 
#WITH THE NEXT STAGE OF THE PROBLEM WHEN A CORRECT ANSWER IS CHOSEN

window = tkinter.Tk()
window.title("Math Practice Solver")
window.geometry("1000x750")
Current_step = tkinter.Button(window,text= '∫½x²')
Current_step['font'] = font.Font(size=50)
Choosenext_textbox = tkinter.Button(window,text='Pick the correct next step in solving this problem')
Choosenext_textbox['font'] = font.Font(size=25)

#THE CORRECT BUTTON
button_correct_text = Problem1_First_Correct_Answer
button_correct = tkinter.Button(window,text= button_correct_text, command=correctanswer)
button_correct['font'] = font.Font(size=50)
button_correct.pack()  
button_correct.place(x=button_correct_xcoord,y=300)
print(button_correct_xcoord)
#button_correct.grid(row = 10, column = 0)

#THE FIRST INCORRECT PROBLEM
button_false1_text = Problem1_First_Wrong_Answer
button_false1 = tkinter.Button(window,text= button_false1_text, command = wronganswer)
button_false1['font'] = font.Font(size=50)
button_false1.pack()
button_false1.place(x=(button_false1_xcoord-40),y=300)
print(button_false1_xcoord)

#THE SECOND INCORRECT PROBLEM
button_false2_text = Problem1_Second_Wrong_Answer
button_false2 = tkinter.Button(window,text= button_false2_text, command = wronganswer)
button_false2['font'] = font.Font(size=50)
button_false2.pack()
button_false2.place(x=button_false2_xcoord, y=300)
print(button_false2_xcoord)

Current_step.pack()
Choosenext_textbox.pack()


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
