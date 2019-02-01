from tkinter import * 
import random  
window=Tk()
window.geometry('590x590')
a=[" "]*10
play='O'
play1='X'
btn=['']*10
check=['No']*9
lbl1=['']*10
btn1=''
btn2=''
def hard():
	global btn10
	btn10[0].destroy()
	btn10[1].destroy()
	btn10[2].destroy()	
	window.update()
	def move(i,j):
		global a,lbl1,play,play1

		def win(a):
			if a[1]==a[2]==a[3]=='X' or a[1]==a[5]==a[9]=='X' or a[1]==a[4]==a[7]=='X' or a[2]==a[5]==a[8]=='X' or a[3]==a[6]==a[9]=='X' or a[3]==a[5]==a[7]=='X' or a[4]==a[5]==a[6]=='X' or a[7]==a[8]==a[9]=='X':
				return 1
			elif a[1]==a[2]==a[3]=='O' or a[1]==a[5]==a[9]=='O' or a[1]==a[4]==a[7]=='O' or a[2]==a[5]==a[8]=='O' or a[3]==a[6]==a[9]=='O' or a[3]==a[5]==a[7]=='O' or a[4]==a[5]==a[6]=='O' or a[7]==a[8]==a[9]=='O':
				return 2    
			else:
				return 0

		def move_left(a):
			for i in range(1,10):
				if a[i]==" ":
					return 1
			return 0            
		#first move by computer      
		def f_move(c,i):
			c[i]="X"
			return player_move(c)       
		#computer move]
		def comp_move(c):
			if win(c)==1:
				return 10
			if win(c)==2:
				 return -10 
			if move_left(c)==0:
				return 0    
			score=-1000000000000    
			for i in range(1,10):
				if c[i]==" ":
					c[i]="X"
					score1=player_move(c)
					if score<=score1:
						score=score1
					c[i]=" " 
			return score

		def player_move(c):
			if win(c)==1:
				return 10
			if win(c)==2:
				return -10 
			if move_left(c)==0:
				return 0     
			score=1000000000   
			for i in range(1,10):
				if c[i]==" ":
					c[i]="O"
					score1=comp_move(c)
					if score>=score1:
						score=score1
					c[i]=" " 
			return score   

		if a[3*i+j+1]==" ":
			btn[3*i+j].configure(text=play)
			a[3*i+j+1]=play
			if move_left(a)==0:
				lbl=Label(window,text='DRAW!',height=6,width=21)
				lbl.grid(column=1,row=4)
				return
			score=-1000000000
			score1=-100000000000	
			x=1	
			for no in range(1,10):
				if a[no]==" ":
					score1=f_move(a,no)
					a[no]=" "     
					if score1>=score:
						x=no
						score=score1
					#print(no,score)	
			x-=1		
			lbl1[x]=Label(window,text=play1,height=11,width=21)
			i=x//3
			j=x%3
			lbl1[x].grid(column=i,row=j)
			a[x+1]=play1
			check[x]='Yes'
			if win(a):
				if win(a)==1:
					lbl=Label(window,text='COMP WIN!',height=6,width=21)
				elif win(a)==2:
					lbl=Label(window,text='YOU WIN!',height=6,width=21) 
				lbl.grid(column=1,row=4)
	global btnx
	def clear():
		global a,btn,check,lbl1,btnx
		a=[" "]*10
		btn=['']*10
		check=['No']*9
		lbl1=['']*10
		btnx=['']*3
		lbl=''
		lbl=Label(window,text='',height=6,width=21)
		lbl.grid(column=1,row=4)
	def again():
		clear()
		show()	
	def	back():
		global btn
		for i in range(0,9):
			btn[i].destroy()
		for i in range(0,2):
			btnx[i].destroy()
		window.update()	
		clear()
		start()	
		#lbl.grid_forget()		
		"""btn10[0]=Button(window,text='TWO PLAYERS',command=vs,height=7,width=70)
		btn10[0].grid(column=0,row=0)
		btn10[1]=Button(window,text='ONE PLAYER (EASY)',command=easy,height=7,width=70)
		btn10[1].grid(column=0,row=1)
		btn10[2]=Button(window,text='ONE PLAYER (HARD)',command=hard,height=7,width=70)
		btn10[2].grid(column=0,row=2)"""
	def q():
		quit()				
	def show():		
		i=0
		while i<3:  
			j=0
			while j<3:
				btn[3*i+j]=Button(window,command=lambda i1=i,j1=j:move(i1,j1),height=11,width=21)
				btn[3*i+j].grid(column=i,row=j)
				j=j+1
			i=i+1 	
		btnx[0]=Button(window,text='AGAIN',command=again,height=5,width=21)
		btnx[0].place(x=0,y=505)
		btnx[1]=Button(window,text='BACK',command=back,height=5,width=9)
		btnx[1].place(x=393,y=505)	
		btnx[2]=Button(window,text='QUIT',command=q,height=5,width=8)
		btnx[2].place(x=494,y=505)	
	show()	

def easy():
	global btn10
	btn10[0].destroy()
	btn10[1].destroy()
	btn10[2].destroy()
	window.update()
	def move(i,j):
		global a,lbl1,play,play1

		def win(a):
			if a[1]==a[2]==a[3]=='X' or a[1]==a[5]==a[9]=='X' or a[1]==a[4]==a[7]=='X' or a[2]==a[5]==a[8]=='X' or a[3]==a[6]==a[9]=='X' or a[3]==a[5]==a[7]=='X' or a[4]==a[5]==a[6]=='X' or a[7]==a[8]==a[9]=='X':
				return 1
			elif a[1]==a[2]==a[3]=='O' or a[1]==a[5]==a[9]=='O' or a[1]==a[4]==a[7]=='O' or a[2]==a[5]==a[8]=='O' or a[3]==a[6]==a[9]=='O' or a[3]==a[5]==a[7]=='O' or a[4]==a[5]==a[6]=='O' or a[7]==a[8]==a[9]=='O':
				return 2    
			else:
				return 0

		def move_left(a):
			for i in range(1,10):
				if a[i]==" ":
					return 1
			return 0            
		
		if a[3*i+j+1]==" ":
			btn[3*i+j].configure(text=play)
			a[3*i+j+1]=play
			if win(a)==1:
				lbl=Label(window,text='COMP WIN!',height=6,width=21)
				lbl.grid(column=1,row=4)
				return 0 
			elif win(a)==2:
				lbl=Label(window,text='YOU WIN!',height=6,width=21)
				lbl.grid(column=1,row=4)
				return 0 
			if move_left(a)==0: 
				lbl=Label(window,text='DRAW!',height=6,width=21)
				lbl.grid(column=1,row=4)
				return 0 	
			for no in range(1,10):
				x=random.randint(1,9)
				if a[x]==" ":
				 	break	
			x-=1		
			lbl1[x]=Label(window,text=play1,height=11,width=21)
			i=x//3
			j=x%3
			lbl1[x].grid(column=i,row=j)
			a[x+1]=play1
			check[x]='Yes'
			if win(a):
				if win(a)==1:
					lbl=Label(window,text='COMP WIN!',height=6,width=21)
				elif win(a)==2:
					lbl=Label(window,text='YOU WIN!',height=6,width=21) 
				lbl.grid(column=1,row=4)
	global btnx
	def clear():
		global a,btn,check,lbl1,btnx
		a=[" "]*10
		btn=['']*10
		check=['No']*9
		lbl1=['']*10
		btnx=['']*3
		lbl=''
		lbl=Label(window,text='',height=6,width=21)
		lbl.grid(column=1,row=4)
	def again():
		clear()
		show()	
	def	back():
		global btn
		for i in range(0,9):
			btn[i].destroy()
		for i in range(0,2):
			btnx[i].destroy()
		window.update()	
		clear()
		start()	
		#lbl.grid_forget()		
		"""btn10[0]=Button(window,text='TWO PLAYERS',command=vs,height=7,width=70)
		btn10[0].grid(column=0,row=0)
		btn10[1]=Button(window,text='ONE PLAYER (EASY)',command=easy,height=7,width=70)
		btn10[1].grid(column=0,row=1)
		btn10[2]=Button(window,text='ONE PLAYER (HARD)',command=hard,height=7,width=70)
		btn10[2].grid(column=0,row=2)"""
	def q():
		quit()				
	def show():		
		i=0
		while i<3:  
			j=0
			while j<3:
				btn[3*i+j]=Button(window,command=lambda i1=i,j1=j:move(i1,j1),height=11,width=21)
				btn[3*i+j].grid(column=i,row=j)
				j=j+1
			i=i+1 	
		btnx[0]=Button(window,text='AGAIN',command=again,height=5,width=21)
		btnx[0].place(x=0,y=505)
		btnx[1]=Button(window,text='BACK',command=back,height=5,width=9)
		btnx[1].place(x=393,y=505)	
		btnx[2]=Button(window,text='QUIT',command=q,height=5,width=8)
		btnx[2].place(x=494,y=505)	
	show()		
def vs():
	global btn10
	btn10[0].destroy()
	btn10[1].destroy()
	btn10[2].destroy()
	def move(i,j):
		global a,lbl1,play,play1,moves

		def win(a):
			if a[1]==a[2]==a[3]=='X' or a[1]==a[5]==a[9]=='X' or a[1]==a[4]==a[7]=='X' or a[2]==a[5]==a[8]=='X' or a[3]==a[6]==a[9]=='X' or a[3]==a[5]==a[7]=='X' or a[4]==a[5]==a[6]=='X' or a[7]==a[8]==a[9]=='X':
				return 1
			elif a[1]==a[2]==a[3]=='O' or a[1]==a[5]==a[9]=='O' or a[1]==a[4]==a[7]=='O' or a[2]==a[5]==a[8]=='O' or a[3]==a[6]==a[9]=='O' or a[3]==a[5]==a[7]=='O' or a[4]==a[5]==a[6]=='O' or a[7]==a[8]==a[9]=='O':
				return 2    
			else:
				return 0

		def move_left(a):
			for i in range(1,10):
				if a[i]==" ":
					return 1
			return 0            
		if a[3*i+j+1]==" ":
			if moves%2==0:
				btn[3*i+j].configure(text=play)
				a[3*i+j+1]=play
			if win(a)==1:
				lbl=Label(window,text='COMP WIN!',height=6,width=21)
				lbl.grid(column=1,row=4)
				return 0 
			elif win(a)==2:
				lbl=Label(window,text='YOU WIN!',height=6,width=21)
				lbl.grid(column=1,row=4)
				return 0 
			if move_left(a)==0: 
				lbl=Label(window,text='DRAW!',height=6,width=21)
				lbl.grid(column=1,row=4)
				return 0 	
			if moves%2==1:
				btn[3*i+j].configure(text=play1)
				a[3*i+j+1]=play1			
			"""x-=1		
			lbl1[x]=Label(window,text=play1,height=11,width=21)
			i=x//3
			j=x%3
			lbl1[x].grid(column=i,row=j)
			a[x+1]=play1"""
			check[3*i+j]='Yes'
			moves+=1
			if win(a):
				if win(a)==1:
					lbl=Label(window,text='COMP WIN!',height=6,width=21)
				elif win(a)==2:
					lbl=Label(window,text='YOU WIN!',height=6,width=21) 
				lbl.grid(column=1,row=3)
	global btnx
	def clear():
		global a,btn,check,lbl1,btnx
		a=[" "]*10
		btn=['']*10
		check=['No']*9
		lbl1=['']*10
		btnx=['']*3
		lbl=''
		lbl=Label(window,text='',height=6,width=21)
		lbl.grid(column=1,row=4)
	def again():
		clear()
		show()	
	def	back():
		global btn
		for i in range(0,9):
			btn[i].destroy()
		for i in range(0,2):
			btnx[i].destroy()
		window.update()	
		clear()
		start()	
		#lbl.grid_forget()		
		"""btn10[0]=Button(window,text='TWO PLAYERS',command=vs,height=7,width=70)
		btn10[0].grid(column=0,row=0)
		btn10[1]=Button(window,text='ONE PLAYER (EASY)',command=easy,height=7,width=70)
		btn10[1].grid(column=0,row=1)
		btn10[2]=Button(window,text='ONE PLAYER (HARD)',command=hard,height=7,width=70)
		btn10[2].grid(column=0,row=2)"""
	def q():
		quit()				
	def show():		
		i=0
		while i<3:  
			j=0
			while j<3:
				btn[3*i+j]=Button(window,command=lambda i1=i,j1=j:move(i1,j1),height=11,width=21)
				btn[3*i+j].grid(column=i,row=j)
				j=j+1
			i=i+1 	
		btnx[0]=Button(window,text='AGAIN',command=again,height=5,width=21)
		btnx[0].place(x=0,y=505)
		btnx[1]=Button(window,text='BACK',command=back,height=5,width=9)
		btnx[1].place(x=393,y=505)	
		btnx[2]=Button(window,text='QUIT',command=q,height=5,width=8)
		btnx[2].place(x=494,y=505)	
	show()	

moves=0
btnx=['']*3			
btn10=['']*3
def qu():
	exit()
def start():
	btn10[0]=Button(window,text='TWO PLAYERS',command=vs,height=11,width=70)
	btn10[0].grid(column=0,row=0)
	btn10[1]=Button(window,text='ONE PLAYER (EASY)',command=easy,height=11,width=70)
	btn10[1].grid(column=0,row=1)
	btn10[2]=Button(window,text='ONE PLAYER (HARD)',command=hard,height=11,width=70)
	btn10[2].grid(column=0,row=2)
	btnx[2]=Button(window,text='QUIT',command=qu,height=5,width=8)
	btnx[2].place(x=494,y=505)		

start()
window.mainloop()