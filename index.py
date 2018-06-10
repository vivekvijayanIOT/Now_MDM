#python code: BEACON
import time
import math
from random import randint

starttime=time.time()
visited=0
times=0
mfile=open("mobile_node_data.txt","w")
mfile.write("\t\tData collected by Mobile node\n\n---------------------------------------------------\n\n")
def timer():
	global times
	times=times+1
class node:
	def __init__(self,c,x,y):
		self.radius=2
		self.xpos=x
		self.ypos=y
		self.charge=c
		self.xp1=self.radius+self.xpos
		self.xm1=self.radius-self.xpos
		self.yp1=self.radius+self.ypos
		self.ym1=self.radius-self.ypos
		self.check=0
		self.times=0
	def discharge(self):
		if(self.charge>10):
			self.charge-=0.5
	def charger(self,n):
		global times
		for x in range(0,100):
			n=n+10
			b = "\t\tCharging [" + "*" * x+"] %d%%"%n
			print(b,end="\r")
			time.sleep(1)
			times=times+1
			self.times=times
			if(n>=80):
				break
		self.charge=self.charge+n
		
		print("\t\t************ 80% Charging completed*************")

	def show(self):
		u="Unknown -Not yet visited"
		if(self.check==1):
			c=str(self.charge)+"%"
			return c
		else:
			return u
	def update_time(self,times):
		self.times=times

	
class dyn_node:
	def __init__(self,radius):
		self.charge=100
		self.xpos=0
		self.ypos=0
		self.radius=radius
		self.xp1=radius+self.xpos
		self.xm1=radius-self.xpos
		self.yp1=radius+self.ypos
		self.ym1=radius-self.ypos
	def discharge(self):
		self.charge-=0.1
		self.radius-=0.1
total_nodes=20


# Node declaration
N1,N2,N3,N4,N5=node(80,20,60),node(30,70,10),node(70,60,80),node(100,100,90),node(90,40,120)
N6,N7,N8,N9,N10=node(70,50,110),node(100,30,170),node(70,90,20),node(60,20,190),node(50,190,190)
N11,N12,N13,N14,N15=node(90,200,130),node(100,150,60),node(90,120,40),node(80,160,180),node(90,190,30)
N16,N17,N18,N19,N20=node(60,110,160),node(100,130,50),node(70,140,100),node(90,180,150),node(20,0,0)
#endnode 
N21=node(200,200,200)
print("**** WSN Execution starts ****\n")
Mobile_node_radius=int(input("Enter the Mobile node range\t :"))
D=dyn_node(Mobile_node_radius)
n=1


# Searching function starts here
def result():
	global visited
	data='''\t\t\t-----*****Result******-----\n\n\n\tTotal Nodes : %d \t\t Nodes visited: %d\n
	        \t\tNote : 0-Not visited   1-Visited\n\n\n
		Node 1 :   %d -->Time: %d sec 	---> Charge remaining : %s  
		Node 2 :   %d -->Time: %d sec 	---> Charge remaining : %s
		Node 3 :   %d -->Time: %d sec 	---> Charge remaining : %s
		Node 4 :   %d -->Time: %d sec 	---> Charge remaining : %s
		Node 5 :   %d -->Time: %d sec 	---> Charge remaining : %s
		Node 6 :   %d -->Time: %d sec 	---> Charge remaining : %s
		Node 7 :   %d -->Time: %d sec 	---> Charge remaining : %s
		Node 8 :   %d -->Time: %d sec 	---> Charge remaining : %s
		Node 9 :   %d -->Time: %d sec 	---> Charge remaining : %s
		Node 10 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 11 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 12 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 13 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 14 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 15 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 16 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 17 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 18 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 19 :  %d -->Time: %d sec 	---> Charge remaining : %s
		Node 20 :  %d -->Time: %d sec 	---> Charge remaining : %s
		'''%(total_nodes,visited,N1.check,N1.times,N1.show(),N2.check,N2.times,N2.show(),N3.check,N3.times,N3.show(),N4.check,N4.times,N4.show(),N5.check,N5.times,N5.show(),N6.check,N6.times,N6.show(),N7.check,N7.times,N7.show(),N8.check,N8.times,N8.show(),N9.check,N9.times,N9.show(),N10.check,N10.times,N10.show(),N11.check,N11.times,N11.show(),N12.check,N12.times,N12.show(),N13.check,N13.times,N13.show(),N14.check,N14.times,N14.show(),N15.check,N15.times,N15.show(),N16.check,N16.times,N16.show(),N17.check,N17.times,N17.show(),N18.check,N18.times,N18.show(),N19.check,N19.times,N19.show(),N20.check,N20.times,N20.show())
	print(data)
	write_to_file(data)



def discharge_all():
	N1.discharge()
	N2.discharge()
	N3.discharge()
	N4.discharge()
	N5.discharge()
	N6.discharge()
	N7.discharge()
	N8.discharge()
	N9.discharge()
	N10.discharge()
	N11.discharge()
	N12.discharge()
	N13.discharge()
	N14.discharge()
	N15.discharge()
	N16.discharge()
	N17.discharge()
	N18.discharge()
	N19.discharge()
	N20.discharge()

file=open("Output.txt","w")

def write_to_file(data):
	global n

	now = time.asctime( time.localtime(time.time()))
	if n==1:
		a="*******Python Code**********\n\tOutput for Execution done on :"+now+"\n\n *** With charging ***"
		file.write(a)
	if n==0:
		a="*******Python Code**********\n\tOutput for Execution done on :"+now+"\n\n *** Without charging *** "
		file.write(a)
	file.write(data)
	

def searching(x,y,r,times):
	global visited
	global n
	if(N1.check!=1):
		z=math.sqrt((pow(N1.xpos-x,2))+pow(N1.ypos-y,2))
		if(z < (N1.radius+r)):
			w=("\t\tNode1 Found at [xpos:%s][ypos:%s]  \n\t\tNode1 -> Charge:%d"%(N1.xpos,N1.ypos,N1.charge))
			mfile.write("\n\n"+w)
			print(w)
			N1.check=1
			visited+=1
			N1.update_time(times)
			if N1.charge<30 and n==1:
				print("\t\tLow Battery...")
				N1.charger(N1.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4

	if(N2.check!=1):
		z=math.sqrt((pow(N2.xpos-x,2))+pow(N2.ypos-y,2))
		if(z < (N2.radius+r)):
			w=("\t\tNode2 Found at [xpos:%s][ypos:%s]  \n\t\tNode2 -> Charge:%d"%(N2.xpos,N2.ypos,N2.charge))
			mfile.write("\n\n"+w)
			print(w)
			N2.check=1
			visited+=1
			N2.update_time(times)
			if N2.charge<30 and n==1:
				print("\t\tLow Battery...")
				N2.charger(N2.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
		
	if(N3.check!=1):
		z=math.sqrt((pow(N3.xpos-x,2))+pow(N3.ypos-y,2))
		if(z < (N3.radius+r)):
			w=("\t\tNode3 Found at [xpos:%s][ypos:%s]  \n\t\tNode3 -> Charge:%d"%(N3.xpos,N3.ypos,N3.charge))
			mfile.write("\n\n"+w)
			print(w)
			N3.check=1
			visited+=1
			N3.update_time(times)
			if N3.charge<30  and n==1:
				print("\t\tLow Battery...")
				N3.charger(N3.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
		
	if(N4.check!=1):
		z=math.sqrt((pow(N4.xpos-x,2))+pow(N4.ypos-y,2))
		if(z < (N4.radius+r)):
			w=("\t\tNode4 Found at [xpos:%s][ypos:%s]  \n\t\tNode4 -> Charge:%d"%(N4.xpos,N4.ypos,N4.charge))
			mfile.write("\n\n"+w)
			print(w)
			N4.check=1
			N4.update_time(times)
			visited+=1
			if N4.charge<30  and n==1:
				print("\t\tLow Battery...")
				N4.charger(N4.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
		
	if(N5.check!=1):
		z=math.sqrt((pow(N5.xpos-x,2))+pow(N5.ypos-y,2))
		if(z < (N5.radius+r)):
			w=("\t\tNode5 Found at [xpos:%s][ypos:%s]  \n\t\tNode5 -> Charge:%d"%(N5.xpos,N5.ypos,N5.charge))
			mfile.write("\n\n"+w)
			print(w)
			N5.check=1
			visited+=1
			N5.update_time(times)
			if N5.charge<30  and n==1:
				print("\t\tLow Battery...")
				N5.charger(N5.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
		
	if(N6.check!=1):
		z=math.sqrt((pow(N6.xpos-x,2))+pow(N6.ypos-y,2))
		if(z < (N6.radius+r)):
			w=("\t\tNode6 Found at [xpos:%s][ypos:%s]  \n\t\tNode6 -> Charge:%d"%(N6.xpos,N6.ypos,N6.charge))
			mfile.write("\n\n"+w)
			print(w)
			N6.check=1
			visited+=1
			N6.update_time(times)
			if N6.charge<30  and n==1:
				print("\t\tLow Battery...")
				N6.charger(N6.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
		
	if(N7.check!=1):
		z=math.sqrt((pow(N7.xpos-x,2))+pow(N7.ypos-y,2))
		if(z < (N7.radius+r)):
			w=("\t\tNode7 Found at [xpos:%s][ypos:%s]  \n\t\tNode7 -> Charge:%d"%(N7.xpos,N7.ypos,N7.charge))
			mfile.write("\n\n"+w)
			print(w)
			N7.check=1
			visited+=1
			N7.update_time(times)
			if N7.charge<30  and n==1:
				print("\t\tLow Battery...")
				N7.charger(N7.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
		
	if(N8.check!=1):
		z=math.sqrt((pow(N8.xpos-x,2))+pow(N8.ypos-y,2))
		if(z < (N8.radius+r)):
			w=("\t\tNode8 Found at [xpos:%s][ypos:%s]  \n\t\tNode8 -> Charge:%d"%(N8.xpos,N8.ypos,N8.charge))
			mfile.write("\n\n"+w)
			print(w)
			N8.check=1
			visited+=1
			N8.update_time(times)
			if N8.charge<30  and n==1:
				print("\t\tLow Battery...")
				N8.charger(N8.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
		
	if(N9.check!=1):
		z=math.sqrt((pow(N9.xpos-x,2))+pow(N9.ypos-y,2))
		if(z < (N9.radius+r)):
			w=("\t\tNode9 Found at [xpos:%s][ypos:%s]  \n\t\tNode9 -> Charge:%d"%(N9.xpos,N9.ypos,N9.charge))
			mfile.write("\n\n"+w)
			print(w)
			N9.check=1
			visited+=1
			N9.update_time(times)
			if N9.charge<30  and n==1:
				print("\t\tLow Battery...")
				N9.charger(N9.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
		
	if(N10.check!=1):
		z=math.sqrt((pow(N10.xpos-x,2))+pow(N10.ypos-y,2))
		if(z < (N10.radius+r)):
			w=("\t\tNode10 Found at [xpos:%s][ypos:%s]  \n\t\tNode10 -> Charge:%d"%(N10.xpos,N10.ypos,N10.charge))
			mfile.write("\n\n"+w)
			print(w)
			N10.check=1
			visited+=1
			N10.update_time(times)
			if N10.charge<30  and n==1:
				print("\t\tLow Battery...")
				N10.charger(N10.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
		
	if(N11.check!=1):
		z=math.sqrt((pow(N11.xpos-x,2))+pow(N11.ypos-y,2))
		if(z < (N11.radius+r)):
			w=("\t\tNode11 Found at [xpos:%s][ypos:%s]  \n\t\tNode11 -> Charge:%d"%(N11.xpos,N11.ypos,N11.charge))
			mfile.write("\n\n"+w)
			print(w)
			N11.check=1
			visited+=1
			N11.update_time(times)
			if N11.charge<30  and n==1:
				print("\t\tLow Battery...")
				N11.charger(N11.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
		

	if(N12.check!=1):
		z=math.sqrt((pow(N12.xpos-x,2))+pow(N12.ypos-y,2))
		if(z < (N12.radius+r)):
			w=("\t\tNode12 Found at [xpos:%s][ypos:%s]  \n\t\tNode12 -> Charge:%d"%(N12.xpos,N12.ypos,N12.charge))
			mfile.write("\n\n"+w)
			print(w)
			N12.check=1
			visited+=1
			N12.update_time(times)
			if N12.charge<30  and n==1:
				print("\t\tLow Battery...")
				N12.charger(N12.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
		
	if(N13.check!=1):
		z=math.sqrt((pow(N13.xpos-x,2))+pow(N13.ypos-y,2))
		if(z < (N13.radius+r)):
			w=("\t\tNode13 Found at [xpos:%s][ypos:%s]  \n\t\tNode13 -> Charge:%d"%(N13.xpos,N13.ypos,N13.charge))
			mfile.write("\n\n"+w)
			print(w)
			N13.check=1
			visited+=1
			N13.update_time(times)
			if N13.charge<30  and n==1: 
				print("\t\tLow Battery...")
				N13.charger(N13.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
		
	if(N14.check!=1):
		z=math.sqrt((pow(N14.xpos-x,2))+pow(N14.ypos-y,2))
		if(z < (N14.radius+r)):
			w=("\t\tNode14 Found at [xpos:%s][ypos:%s]  \n\t\tNode14 -> Charge:%d"%(N14.xpos,N14.ypos,N14.charge))
			mfile.write("\n\n"+w)
			print(w)
			N14.check=1
			visited+=1
			N14.update_time(times)
			if N14.charge<30  and n==1:
				print("\t\tLow Battery...")
				N14.charger(N14.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
		
	if(N15.check!=1):
		z=math.sqrt((pow(N15.xpos-x,2))+pow(N15.ypos-y,2))
		if(z < (N15.radius+r)):
			w=("\t\tNode15 Found at [xpos:%s][ypos:%s]  \n\t\tNode15 -> Charge:%d"%(N15.xpos,N15.ypos,N15.charge))
			mfile.write("\n\n"+w)
			print(w)
			N15.check=1
			visited+=1
			N15.update_time(times)
			if N15.charge<30  and n==1:
				print("\t\tLow Battery...")
				N15.charger(N15.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
		
	if(N16.check!=1):
		z=math.sqrt((pow(N16.xpos-x,2))+pow(N16.ypos-y,2))
		if(z < (N16.radius+r)):
			w=("\t\tNode16 Found at [xpos:%s][ypos:%s]  \n\t\tNode16 -> Charge:%d"%(N16.xpos,N16.ypos,N16.charge))
			mfile.write("\n\n"+w)
			print(w)
			N16.check=1
			visited+=1
			N16.update_time(times)
			if N16.charge<30  and n==1:
				print("\t\tLow Battery...")
				N16.charger(N16.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
		
	if(N17.check!=1):
		z=math.sqrt((pow(N17.xpos-x,2))+pow(N17.ypos-y,2))
		if(z < (N17.radius+r)):
			w=("\t\tNode17 Found at [xpos:%s][ypos:%s]  \n\t\tNode17 -> Charge:%d"%(N17.xpos,N17.ypos,N17.charge))
			mfile.write("\n\n"+w)
			print(w)
			N17.check=1
			visited+=1
			N17.update_time(times)
			if N17.charge<30  and n==1:
				print("\t\tLow Battery...")
				N17.charger(N17.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
		
	if(N18.check!=1):
		z=math.sqrt((pow(N18.xpos-x,2))+pow(N18.ypos-y,2))
		if(z < (N18.radius+r)):
			w=("\t\tNode18 Found at [xpos:%s][ypos:%s]  \n\t\tNode18 -> Charge:%d"%(N18.xpos,N18.ypos,N18.charge))
			mfile.write("\n\n"+w)
			print(w)
			N18.check=1
			visited+=1
			N18.update_time(times)
			if N18.charge<30  and n==1:
				print("\t\tLow Battery...")
				N18.charger(N18.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
		
	if(N19.check!=1):
		z=math.sqrt((pow(N19.xpos-x,2))+pow(N19.ypos-y,2))
		if(z < (N19.radius+r)):
			w=("\t\tNode19 Found at [xpos:%s][ypos:%s]  \n\t\tNode19 -> Charge:%d"%(N19.xpos,N19.ypos,N19.charge))
			mfile.write("\n\n"+w)
			print(w)
			N19.check=1
			visited+=1
			N19.update_time(times)
			if N19.charge<30  and n==1:
				print("\t\tLow Battery...")
				N19.charger(N19.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
		
	if(N20.check!=1):
		z=math.sqrt((pow(N20.xpos-x,2))+pow(N20.ypos-y,2))
		if(z < (N20.radius+r)):
			w=("\t\tNode20 Found at [xpos:%s][ypos:%s]  \n\t\tNode20 -> Charge:%d"%(N20.xpos,N20.ypos,N20.charge))
			mfile.write("\n\n"+w)
			print(w)
			N20.check=1
			visited+=1
			N20.update_time(times)
			if N20.charge<30  and n==1:
				print("\t\tLow Battery...")
				N20.charger(N20.charge)
				mfile.write("\tCharged by Mobile node")
				times=times+4
	if(N21.check!=1):
		N21.update_time(times)
		
def forward(y):
	while(D.ypos in range(y,y+40)):
		timer()
		D.ypos+=2
		D.xpos+=10		
		time.sleep(0.5)
		searching(D.xpos,D.ypos,D.radius,times)
		discharge_all()
		a=("Last postion of ypos: %d  xpos: %d "%(D.ypos,D.xpos))
		print(a,end="\r")
		

def backward(y):
	while(D.ypos in range(y,y+40)):
		timer()
		D.ypos+=2
		D.xpos-=10
		time.sleep(0.5)
		searching(D.xpos,D.ypos,D.radius,times)
		discharge_all()
		a=("Last postion of ypos: %d  xpos: %d "%(D.ypos,D.xpos))
		print(a,end="\r")
		


# Execution starts 

forward(0)
backward(40)
forward(80)
backward(120)
forward(160)
result()
endtime=time.time()
exetime=endtime-starttime
file.write("Total time taken : %d sec"%N21.times)
file.close()
mfile.close()






	 
	
