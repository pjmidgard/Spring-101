from time import time
cvf=0
Portal=2
import os
import binascii

zzaax=""
szxzzzas=""
asaaq=""
assa=0
adwll1=0
ddf=0
cvz31=0
rw=0
qqw1q=""
lenfzzz=0
fffgjv=""
fffgjv1=""
zzaax1=""
qqqs=0
a=0
blockw=5
blockw1=4
cvb=0
aqw1=0
zsaqq=""
qqqwz=0
assx=0
ass=0
asss=0
b=0
aaqw=""
aaqws=""
l=""
j=0
b=0
aq=0
qfl=0
t=0
h=0
byteb=""
notexist=""
lenf=0
numberschangenotexistq = []
numberschangenotexistqz = []
qwa=0
add=0
m = []
p=0
namea=""
d=1
a=0
asd=""
b=0
szx=""
asf2="0b"
while b<1790:
    m+=[-1]
    b=b+1
k = []
wer=""
qtqweqw=""
numberschangenotexist = []
numbers = []
namez = input("ul,c2 or for compress cl for extract for u2? ")
#@Author Jurijus pacalovas
class compression:
                      
            
                                            
                                    
                                      
    def cryptograpy_compression(self):
                
                self.name = "Written: Jurijus pacalovas Price Protal 5 000 000 Euro cost Date: 29/08/2021 21:33 Deep 14.5 ERA"
                
                if namez=="ul" or namez=="cl":
                    if namez=="ul":
                        i=1
                    if namez=="cl":
                        i=2
                        
                    corridors=0
                    cor=7
                    name = input("What is name of file? ")
                    namea="file.W"
                    namem=""
                    namema="?"
                    Portal=2
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)

                    if i==2:
                        if nameas[nac-4:nac]!=".bin":
                             print("Program close because this is file is not .bin")
                             raise SystemExit
                        
                        nameas=name[:nac-4]
                        nac=len(nameas)
                    
                    
                    if nameas[nac-5:nac]==".docx":
                        Portal=1
                    if nameas[nac-4:nac]==".pdf":
                        Portal=3
                    if nameas[nac-4:nac]==".doc":
                        Portal=1
                    if nameas[nac-4:nac]==".png":
                        Portal=7
                    if nameas[nac-4:nac]==".jpg":
                        Portal=9
                    if nameas[nac-4:nac]==".mp4":
                        Portal=8
                      
                    if i==1:
                       
                        nameas=name+".bin"
                    
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                 
                    sda3=""
                    sda2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()

                     
                

                        
                        if i==1:
                            if Portal==9 and data[0:3]!=b'\xff\xd8\xff':
                                    print("Program close because this is file incorrect")
                                    raise SystemExit
                            if Portal==9 and data[0:3]==b'\xff\xd8\xff': 
                                    data=data[3:]
                            if Portal==7 and data[0:4]!=b'\x89\x50\x4e\x47' :
                                    print("Program close because this is file incorrect")
                                    raise SystemExit
                            if Portal==7 and data[0:4]==b'\x89\x50\x4e\x47' :             
                                    data=data[4:]
                            if Portal==8 and data[0:11]!=b'\x00\x00\x00\x18\x66\x74\x79\x70\x6d\x70\x34':
                                    print("Program close because this is file incorrect")
                                    raise SystemExit
                            if Portal==8 and data[0:11]==b'\x00\x00\x00\x18\x66\x74\x79\x70\x6d\x70\x34':             
                                    data=data[11:]
      
                        s=str(data)
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:

                                 
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if countraz==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)  
                                                
                                e4=sda2[e2:e3]
                                
                                block=block+1
                                
                                if Portal<10:
	                                corridors=corridors+1%257
	                                
	                                if block<=corridors:
	                                    if e4=="0":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=corridors
	                                        e4=""
	                                        
	                                    if e4=="1":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=7
	                                        e4=""
	
	                                if block>=corridors:
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=0
	                                        e4=""
	                                        
	                                    if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=0
	                                        e4=""
	                                        
	                                if block<=6:
	                                    if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=7
	                                        e4=""
	                                       
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=7
	                                        e4=""
	                                             
	                                if block==corridors:
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=corridors
	                                        e4=""
	                                                 
	                                if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=0
	                                        e4=""    

                                if Portal<10:
	                                corridors=corridors+1%257
	                                
	                                if block<=3:
	                                    if e4=="0":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=corridors
	                                        e4=""
	                                        
	                                    if e4=="1":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=7
	                                        e4=""
	
	                                if block>=8:
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=0
	                                        e4=""
	                                        
	                                    if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=0
	                                        e4=""
	                                        
	                                if block<=6:
	                                    if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=7
	                                        e4=""
	                                       
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=7
	                                        e4=""
	                                             
	                                if block==7:
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=corridors
	                                        e4=""
	                                                 
	                                if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=0
	                                        e4=""    
                                                
                                if Portal<10:
                                 
                                     corridors=corridors+1%8
                                     if block==corridors%3:
                                         if e4=="0":
                                         	sda3=sda3+"0"
                                         	e4="0"
                                         	block=0
                                         	e4=""
                                         	
                                         if e4=="1":
                                         	sda3=sda3+"1"
                                         	e4="1"
                                         	block=0
                                         	e4=""
                                     if block>=corridors%8:
                                         if e4=="1":
                                         	sda3=sda3+"0"
                                         	e4="0"
                                         	
                                         	e4=""
                                         	
                                         if e4=="0":
                                             sda3=sda3+"1"
                                             e4="1"
                                             
                                             e4=""
                                     if block<=corridors%6 and block>3:
                                         if e4=="0":
                                         	sda3=sda3+"1"
                                         	e4="1"
                                         	
                                         	e4=""
                                         	
                                         if e4=="1":
                                         	sda3=sda3+"0"
                                         	e4="0"
                                         	
                                         	e4=""
                                     if block==corridors%7:
                                         if e4=="1":
                                         	sda3=sda3+"0"
                                         	e4="0"
                                         	e4=""
                                     if e4=="0":
                                         sda3=sda3+"1"
                                         e4="1"
                                         
                                         e4=""   

                                if Portal<10:
	                                corridors=corridors+1%257
	                                
	                                if block<=corridors:
	                                    if e4=="0":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=corridors
	                                        e4=""
	                                        
	                                    if e4=="1":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=7
	                                        e4=""
	
	                                if block>=corridors:
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=0
	                                        e4=""
	                                        
	                                    if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=0
	                                        e4=""
	                                        
	                                if block<=6:
	                                    if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=7
	                                        e4=""
	                                       
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=7
	                                        e4=""
	                                             
	                                if block==corridors:
	                                    if e4=="1":
	                                        sda3=sda3+"0"
	                                        e4="0"
	                                        block=corridors
	                                        e4=""
	                                                 
	                                if e4=="0":
	                                        sda3=sda3+"1"
	                                        e4="1"
	                                        block=0
	                                        e4=""    
                                
                               
	                           
                                if Portal<10:
                                 
                                     corridors=corridors+1%8
                                                                       
                                     if block==corridors%1 or block==corridors%4:
                                         if e4=="0":
                                         	sda3=sda3+"0"
                                         	e4="0"
                                         	block=0
                                         	e4=""
                                         	
                                         if e4=="1":
                                         	sda3=sda3+"1"
                                         	e4="1"
                                         	block=0
                                         	e4=""
                                     if block>=corridors%2:
                                         if e4=="1":
                                         	sda3=sda3+"0"
                                         	e4="0"
                                         	
                                         	e4=""
                                         	
                                         if e4=="0":
                                             sda3=sda3+"1"
                                             e4="1"
                                             
                                             e4=""
                                     if block<=corridors%13 or block==corridors%7 or block>3:
                                         if e4=="0":
                                         	sda3=sda3+"1"
                                         	e4="1"
                                         	
                                         	e4=""
                                         	
                                         if e4=="1":
                                         	sda3=sda3+"0"
                                         	e4="0"
                                         	
                                         	e4=""
                                     if  block<=corridors%9:
                                         if e4=="1":
                                         	sda3=sda3+"0"
                                         	e4="0"
                                         	e4=""
                                     if e4=="0":
                                         sda3=sda3+"1"
                                         e4="1"
                                         
                                         e4="" 
                                         
   
                                if assxw==e3%2 or assxw==e3%10:
                                               
                                            if e4=="1" and e3== e3%10:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                
                                            elif e4=="0" and e3== e3%11:
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""
                                                
                                                    
                                            elif e4=="1":
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                
                                         
                                            elif e4=="1":
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""   
                                               
                                            elif e4=="1" and e3== e3%3:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                
                                            elif e4=="0" and e3== e3%2:
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""
                                                
                                                    
                         
                                    
                                    
                                            elif e4=="0" and e3== e3%9:
                                                    sda3=sda3+"1"
                                                    e4="1"
                                                    e4=""
                                                
                                            elif e4=="1" and e3== e3%8:
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4=""
                                                
                                                    
                                            elif e4=="1" and e3 ==e3%1:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                    
                                            elif e4=="0" and e3 ==e3%1:
                                                    sda3=sda3+"1"
                                                    e4="1"
                                                    e4=""
                                                    
                                                    
                                                    
                                        
                                            
                                
                                
                                if e4=="1" and e3== e3%9+assxw:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="0" and e3== e3%8+assxw:
                                    sda3=sda3+"1"
                                    e4="1"
                                    e4=""
                                
                                elif e4=="0" and e3== e3%7:
                                	sda3=sda3+"1"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%6:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                
                                elif e4=="0" and e3== e3%5:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%4:
                                    sda3=sda3+"1"
                                    e4="1"
                                    e4=""
                                    
                           
                                elif e4=="1" and e3== e3%3:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="0" and e3== e3%2:
                                    sda3=sda3+"1"
                                    e4="1"
                                    e4=""
                                    
                                        
                                elif e4=="1":
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="0":
                                    sda3=sda3+"1"
                                    e4="1"
                                    e4=""  
                                if assxw>=e3%2:
	                                if e4=="1" and e3== e3%19+assxw:
	                                	sda3=sda3+"0"
	                                	e4="0"
	                                	e4=""
	                                    
	                                elif e4=="0" and e3== e3%18+assxw:
	                                    sda3=sda3+"1"
	                                    e4="1"
	                                    e4=""
	                                    
	                                elif e4=="0" and e3== e3%18+assxw:
	                                    sda3=sda3+"1"
	                                    e4="1"
	                                    e4=""
	                                
	                                
	                                elif e4=="1" and e3== e3%1+assxw:
	                                	sda3=sda3+"1"
	                                	e4="1"
	                                	e4=""
	                                    
	                                elif e4=="0" and e3== e3%2+assxw:
	                                    sda3=sda3+"0"
	                                    e4="0"
	                                    e4=""  
	                                
                                    
	                                    
	                                if e4=="0" and e3== e3%4+assxw:
	                                    sda3=sda3+"0"
	                                    e4="0"
	                                    e4=""  
	                                    
	                                   	
	                                if e4=="1" and e3== e3%6+assxw:
	                                    sda3=sda3+"0"
	                                    e4="0"
	                                    e4=""  
                               
                                    
	                                if e4=="1" and e3== e3%2+assxw:
	                                	sda3=sda3+"0"
	                                	e4="1"
	                                	e4=""
	                                    
	                                if e4=="0" and e3== e3%3+assxw:
	                                    sda3=sda3+"1"
	                                    e4="0"
	                                    e4=""  
	                                              
	                                if e4=="0" and e3== e3%5+assxw:
	                                	sda3=sda3+"0"
	                                	e4="1"
	                                	e4=""                                                
 
                             
                                e2=e2+1
                                e3=e3+1

                                e4=""
                          
                                if e3==cvf:
                                    e2=0
                                    e3=1
                                    
                                    cvf=cvf+1

                                    cvf=sw
                                    sw=sw+1
                             
                                if cvf==lenf5*8+4:
                                    sw=sw+2
                                    cvf=c
                                    cvf1=cvf1+1
                                     
                                    c=c+2

                                if cvf1==1:
                                   
                                    n = int(sda3, 2)
                                
                                    qqwslenf=len(sda3)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    data=jl
                                    
                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                            
                                    assxw=assxw+1
                                    if assxw==200:
                                        assx=10
                                        if assx==10:
                                              
                                               

                                                if i==2:
                                                    if Portal==7:
                                                        jl= b'\x89\x50\x4e\x47'+jl
                                                    if Portal==8:
                                                        jl=b'\x00\x00\x00\x18\x66\x74\x79\x70\x6d\x70\x34'+jl
                                                    if Portal==9:
                                    	                jl=b'\xff\xd8\xff'+jl
                                    	                
                                                f2.write(jl)
                                                x2 = time()
                                                x3=x2-x
                                                return print(x3)

d=compression()



xw=d.cryptograpy_compression()
print(xw)
