words = ['grapes', 'mango', 'apple', 'gun', 'fan', 'door', 'tv', 'mobile', 'laptop','expert','wrong','master',
'express','excellent','ridiculous','light','fetch','cheer','field','travel','attach','beneficial','puncture',
'boast','match','effect','deserve','parcel','funny','yummy','glamorous','flower','pinch','expand','swing','defective',
'accept','breath','attention','authority','challenge','character','check','charge','either','effect','perhaps','pick']



def labelSlider():
    global count, sliderWords
    text = 'Welcome to Typing Speed Checker Game'
    if (count >= len(text)):
        count = 0
        sliderWords = ''
    sliderWords += text[count]
    count += 1
    fontLabel.configure(text=sliderWords)
    fontLabel.after(150, labelSlider)


def time():
    global timeleft, score, miss
    if (timeleft >= 11):
        pass
    else:
        timeLableCount.configure(fg='red')
    if (timeleft > 0):
        timeleft -= 1
        timeLableCount.configure(text='{} sec'.format(timeleft))
        timeLableCount.after(1000, time)
    else:
        gamePlayDetailLabel.configure(text='Hit = {} | Miss = {} | Total Score = {}'.format(score, miss, score - miss),fg='green')
        rr = messagebox.askretrycancel('Notification', 'For Play Again Hit Retry Button')
        if (rr == True):
            score = 0
            timeleft = 60
            miss = 0
            timeLableCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLableCount.configure(text=score)


def startGame(event):
    global score, miss
    if (timeleft == 60):
        time()
    gamePlayDetailLabel.configure(text='')
    if (wordEntry.get() == wordLabel['text']):
        score += 1
        scoreLableCount.configure(text=score)
    else:
        miss += 1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0, END)


from tkinter import *  # package to create standard python interface
import random
from tkinter import messagebox

####################################################################  Root Method
root = Tk()  # to create screen(GUI)
root.geometry('800x600+400+100')  # Dimensions to screen
root.configure(bg='powder blue')
root.title('Typing Speed Checker Game')
root.iconbitmap('icon.ico')
###################################################################### Variables
score = 0
timeleft = 60
count = 0
sliderWords = ''
miss = 0
######################################################################  Label Methods
fontLabel = Label(root, text='', font=('airal', 25, 'italic bold'),
                  bg='powder blue', fg='red', width=40)
fontLabel.place(x=10, y=10)
labelSlider()

random.shuffle(words)
wordLabel = Label(root, text=words[0], font=('airal', 40, 'bold'), bg='powder blue')
wordLabel.place(x=350, y=200)

scoreLable = Label(root, text='Your Score  ', font=('airal', 25, 'italic bold'), bg='powder blue')
scoreLable.place(x=10, y=100)

scoreLableCount = Label(root, text=score, font=('airal', 25, 'italic bold'), bg='powder blue', fg='blue')
scoreLableCount.place(x=80, y=160)

timerLabel = Label(root, text='Time Left ', font=('airal', 25, 'italic bold'), bg='powder blue')
timerLabel.place(x=620, y=100)

timeLableCount = Label(root, text='{} sec'.format(timeleft), font=('airal', 25, 'italic bold'), bg='powder blue',
                       fg='blue')
timeLableCount.place(x=655, y=160)

gamePlayDetailLabel = Label(root, text='Type Word And Hit Enter Button', font=('arial', 30, 'italic bold'),
                            bg='powder blue', fg='dark grey')
gamePlayDetailLabel.place(x=120, y=450)
######################################################################  Entry Method
wordEntry = Entry(root, font=('airal', 25, 'italic bold'), bd=10, justify='center')
wordEntry.place(x=230, y=300)
wordEntry.focus_set()
###################################################################
root.bind('<Return>', startGame)  # bind function used to deal with event return means enter button of keyboard
root.mainloop()

