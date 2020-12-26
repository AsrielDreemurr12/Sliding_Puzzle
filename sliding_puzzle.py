from random import*
from tkinter import*
from tkinter import messagebox
import time

lst=[]
coords_list=[]

time_begin=time.time()

def OnClick(event):
    global buttons, images, images2, clicked, lst, coords_list
    t=event.widget.grid_info()
    x=t['column']
    y=t['row']
    buttons[4*y+x].config(image=images2[4*y+x])
    coords_list.append(x)
    coords_list.append(y)
    buttons[4*y+x].update_idletasks()
    clicked[4*y+x]=True
    
    if clicked.count(True)==2:
        for i in range(len(images)):
            if clicked[i]==True:
                lst.append(i)               
                   
        if images[lst[0]]=='images/16.gif' or images[lst[1]]=='images/16.gif':
            x1=coords_list[0]
            y1=coords_list[1]
            x2=coords_list[2]
            y2=coords_list[3]
            if (x2==x1-1 and y2==y1) or (x2==x1+1 and y2==y1) or (x2==x1 and y2==y1-1) or (x2==x1 and y2==y1+1):
                buttons[lst[0]].config(image=images2[lst[1]])
                buttons[lst[1]].config(image=images2[lst[0]])
                images2[lst[0]],images2[lst[1]]=images2[lst[1]],images2[lst[0]]
                images[lst[0]],images[lst[1]]=images[lst[1]],images[lst[0]]                
                 
        lst=[]
        clicked=[False]*16
        coords_list=[]

    if images==['images/1.gif','images/2.gif','images/3.gif','images/4.gif',
        'images/5.gif','images/6.gif','images/7.gif','images/8.gif',
        'images/9.gif','images/10.gif','images/11.gif','images/12.gif',
        'images/13.gif','images/14.gif','images/15.gif','images/16.gif']:
        time_end=time.time()
        messagebox.showinfo('','Поздравляем, вы выиграли за {}:{} мин'.format(int(time_end-time_begin)//60,int(time_end-time_begin)%60))
        

a=Tk()
a.title('Sliding Puzzle')
a.iconbitmap('images/icon.ico')
a.config(bg='#3c1202')
a.resizable(width=False,height=False)

buttons=[]
images=['images/1.gif','images/2.gif','images/3.gif','images/4.gif',
        'images/5.gif','images/6.gif','images/7.gif','images/8.gif',
        'images/9.gif','images/10.gif','images/11.gif','images/12.gif',
        'images/13.gif','images/14.gif','images/15.gif','images/16.gif']

shuffle(images)

images2=[]
clicked=[False]*16

for i in range(16):
    images2.append(PhotoImage(file=images[i]))

row=0
col=0
for i in range(4):
    for j in range(4):
        btn=Button(image=images2[4*i+j],bd=0)
        btn.bind('<Button-1>',OnClick)
        btn.grid(row=row,column=col)
        buttons.append(btn)
        col+=1
    if col>3:
        col=0
        row+=1
a.mainloop()
