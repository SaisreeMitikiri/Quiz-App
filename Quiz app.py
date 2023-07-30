import tkinter as tk
from tkinter import StringVar

root = tk.Tk()
root.title("Quiz")
root.geometry('500x500')

questions =["The largest irrigation canal in India?",
            "who has won the Emerging Asia Cup 2023(cricket) title?",
            "which of the following rivers does not drain into the Arabian Sea?",
            "what is the total cost of the Chandrayaan-3 mission?",
            "who among the folllowing attacked the Somnath temple?"]
options = [["Indira Gandhi Canal","Yamuna Canal","Sirhand Canal","Upper Bari Doab Canal","Triveni Canal"],
           ["Sri Lanka A","Pakisthan-A","India-A","Bangladesh-A","Indonesia"],
           ["Tapti","Narmada","Godavari","Indus","Krishna"],
           ["600 Cr","715 Cr","700 Cr","615 Cr","800 Cr"],
           ["Bahadur Shah Zafar","Muhammad Ghori","Iltumish","Qutbuddin Aibak","Mahmud of Ghazni"]]

frame = tk.Frame(root, padx=10, pady=10, bg='#fff')
question_label = tk.Label(frame, height=5, width=28, bg='grey', fg="#fff", font=('Verdana', 20), wraplength=500)

v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)
v5 = StringVar(frame)


option1 = tk.Radiobutton(frame, bg="#fff", variable=v1, font=('Verdana', 20), command = lambda : checkAnswer(option1))
option2 = tk.Radiobutton(frame, bg="#fff", variable=v2, font=('Verdana', 20), command = lambda : checkAnswer(option2))
option3 = tk.Radiobutton(frame, bg="#fff", variable=v3, font=('Verdana', 20), command = lambda : checkAnswer(option3))
option4 = tk.Radiobutton(frame, bg="#fff", variable=v4, font=('Verdana', 20), command = lambda : checkAnswer(option4))
option5 = tk.Radiobutton(frame, bg="#fff", variable=v5, font=('Verdana', 20), command = lambda : checkAnswer(option5))

button_next = tk.Button(frame, text='Next',bg="Orange", font=('Verdana', 20), command = lambda : displayNextQuestion())

frame.pack(fill="both", expand="true")
question_label.grid(row=0,column=0)

option1.grid(sticky='w', row=1, column=0)
option2.grid(sticky='w', row=2, column=0)
option3.grid(sticky='w', row=3, column=0)
option4.grid(sticky='w', row=4, column=0)
option5.grid(sticky='w', row=5, column=0)

button_next.grid(row=7, column=0)

index = 0
correct = 0
r = 0
def disableButtons(state):
    option1['state']=state
    option2['state']=state
    option3['state']=state
    option4['state']=state
    option5['state']=state

def checkAnswer(radio):
    global correct,index,r 
    
    if radio['text'] == options[index][r]:
        correct += 1
    index += 1
    r += 1 
    disableButtons('disable')


def displayNextQuestion():
    global index, correct,r

    if button_next['text'] == 'Restart The Quiz':
        correct = 0
        index = 0
        r = 0
        question_label['bg'] = 'grey'
        button_next['text']='Next'

    if index == len(options):
        question_label['text'] = str(correct) +"/"+str(len(options))
        button_next['text'] = 'Restart The Quiz'
        if correct >= len(options)/2:
            question_label['bg'] = 'green'
        else:
            question_label['bg'] = 'red'
            


    else:
        question_label['text'] = questions[index]
        
        disableButtons('normal')
        opts = options[index]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
        option5['text'] = opts[4]
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])
        v5.set(opts[4])

        if index == len(options)- 1:
            button_next['text'] = 'Check the Results'
            





displayNextQuestion()

root.mainloop()
