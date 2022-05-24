from time import time
import os
import binascii
import math
import os.path

lenf=0
name=""
add_bits=""
Make_togher=""

namez = input("c,  compress or e, extract? ")

#@Author Jurijus Pacalovas
class compression:
       
        def cryptograpy_compression4(self):
                
                self.name = "Written: Jurijus pacalovas"

                if namez!="c" and namez!="e":
                        print("The wrong letter")
                        raise SystemExit
                if namez=="c" or namez=="e":        
                    if namez=="c":

                        Deep3=-1
                        Block_101=1
                        Block_101E=2
                        compress_or_not_compress1=0
                        Block_10e=2

                        i=1

                    if namez=="e":
                        i=2
                 
                    Number_add_plus_one=""
                    Prime_Not=""
                    Times_6=""
                    Corrupted=0
                      
                    name = input("What is name of file? ")

                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                            
                    
                    namem=""
                    namema="?"
                    Number_N12=""
                    X_1=""
                    X_2=""
        
                    nameas=name
                    nac=len(nameas)
                    
                    compress_or_not_compress=1
                    Circle_times3=0

                    if i==2:
                        if nameas[nac-4:nac]==".bin":
                   
                        	nameas=name[:nac-4]
                        	nac=len(nameas)
                        	
                        	C=1

                        elif nameas[nac-4:nac]!=".bin":
                                print("Sorry, this is not binary file!")
                                raise SystemExit
                   
                    if i==1:
                        
                        nameas=name+".bin"
                        N_N=0
                        N_n=0
                    
                    	
                    nac=len(nameas)
                    
                    Block_10R=0
                    Block_10T_U=0
                    Block_10TU10=0
                    Block_10TU11=0
                    
                   
                    s=""

                    Equal_info_between_of_the_cirlce_of_the_file=""
                    Equal_info_between_of_the_cirlce_of_the_file_2=""

                    Prime_Not=""
                    Times_6=""

                    Translate_info_Decimal=""

                    D=0

                    x=0
                    x1=0
                    x2=0
                    n=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
      
                        s=str(data)

                        lenf1=len(data)
                        lenf7=len(data)
                        if lenf7==0:
                        	 raise SystemExit
                        
                        END_working=0
                        Circle_times2=0
                                   
                        Equal_info_between_of_the_cirlce_of_the_file_23=""
 
                        sda18=""
                        Equal_info_between_of_the_cirlce_of_the_file_29=""
                        
                        SpinS=0
                        while END_working<10:
                       
                            Circle_times3=Circle_times3+1
                            D=1
                            if D==1:
                                if Circle_times3==1:

                                 
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    count_bits=(lenf1*8)-lenf
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    

                                    if Circle_times3==1:
                                        Equal_info_between_of_the_cirlce_of_the_file_2=sda
                            
                                    n = int(Equal_info_between_of_the_cirlce_of_the_file_2, 2)
                                
                                    width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                    width_bits=(width_bits/8)*2
                                    width_bits=str(width_bits)
                                    width_bits="%0"+width_bits+"x"
                             
                                    width_bits3=binascii.unhexlify(width_bits % n)                                    
                                    width_bits2=len(width_bits3)
                                    
                                    data=width_bits3
                                  
                                    lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    count_bits=(lenf1*8)-lenf
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            sda="0"+sda
                                            z=z+1

                                    Equal_info_between_of_the_cirlce_of_the_file_2=sda

                                    lenf3=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                lenf2=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                #print(lenf2)
                                if i==1:
                                    if lenf7>=(2**40)-1:
                                        raise SystemExit

                                #########################################################################################################################################################
                                
                                
                                if i==1:

                                    lenf5=len(Equal_info_between_of_the_cirlce_of_the_file_2)

                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                 
                                    lenf5=len(Equal_info_between_of_the_cirlce_of_the_file)
                                    
                                    
                                    #Extract
                            
                                    s=""

                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                    
                                    Number_add_plus_one=""
                                    Prime_Not=""
                                    Times_6=""
                                  
                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                   
                                    g=0

                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2

                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)                      
                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                                
                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                    
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                
                                    add_bits=""

                                    Times_6=""

                                    #Compression

                                    sda10=""
                                    Translate_info_Decimal=""
                                    
                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                 
                                    if   Circle_times2==0 and SpinS==0:
                                    	Equal_info_between_of_the_cirlce_of_the_file="1"+Equal_info_between_of_the_cirlce_of_the_file
                                    	SpinS=1

                                    if Circle_times2>=(2**32)-1:
                                            compress_or_not_compress1=3


                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                            
                                    
                                    INIT=""
                                    Number_N=""
                                    INIT=Equal_info_between_of_the_cirlce_of_the_file
                                    #print(INIT)
                                    block=0
                                    Block_10T=0
                                    Number_N4=""

                                    while block<lenf6:
                                            Number_N1=INIT[block:block+1]
                                            Number_N2=INIT[block+1:block+2]
                                            Number_N3=INIT[block+2:block+3]
                                            Number_N14=INIT[block+3:block+4]
                                            Number_N15=INIT[block+4:block+5]
                                            Number_N16=INIT[block+5:block+6]
                                           
                                            Block_101_binary=bin(Block_101)[2:]

                                            if Block_101==1:
                                                    Block_103=Block_101+0
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary
                                            
                                                    Number_N=Number_N1+"0"+Number_N2+"0"+Number_N3+"0"
                                                    
                                                    Block_102_binary="0"+"0"+"0"+"0"+"0"+"0"
                                                    Block_122_binary="0"+"0"+"0"+"0"+"1"+"0"
                                                    Block_123_binary="0"+"0"+"1"+"0"+"0"+"0"

                                                    Block_103=Block_101+0
                                                    Block_105_binary=str(Block_103)

                                                    


                                                    Block_101_1_binary="0"+"0"+"1"+"0"+"1"+"0"
                                                    Block_101_2_binary="1"+"0"+"0"+"0"+"0"+"0"
                                                    Block_101_3_binary="1"+"0"+"0"+"0"+"1"+"0"


                                                    Block_103=Block_101+0
                                                    Block_105_binary=str(Block_103)

                                                    


                                                    Block_101_1_1_binary="1"+"0"+"1"+"0"+"0"+"0"
                                                    Block_101_2_1_binary="1"+"0"+"1"+"0"+"1"+"0"

                                                    Block_101_4_1_binary=""
                                                    
                                                    
                                                    
                                            else:
                                                    Block_103=Block_101+0
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary
                                            
                                                    Number_N=Number_N1+Number_N2+Number_N3+Number_N14+Number_N15+Number_N16
                                                    
                                                    #print(Number_N2)
                                                    
                                                    Block_102_binary=""


                                                    Block_103=Block_101+1
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary
                                            
                                                    

                                                    
                                                    Block_122_binary=""


                                                    Block_103=Block_101+2
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary
                                            
                                                    
                                                    
                                                    Block_123_binary=""




                                                    Block_103=Block_101+3
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary
                                            
                                                    
                                                    
                                                    Block_101_1_binary=""


                                                    Block_103=Block_101+4
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary


                                                    Block_1031=Block_101+3
                                                    Block_105_binary1=str(Block_1031)

                                                    Block_106_binary1=Block_105_binary1
                                            
                                                    

                                                    
                                                    Block_101_2_binary=""


                                                    Block_103=Block_101+5
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary
                                            
                                                    
                                                    
                                                    Block_101_3_binary=""


                                                    Block_103=Block_101+6
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary
                                            
                                                    
                                                    
                                                    Block_101_1_1_binary=""


                                                    Block_103=Block_101+7
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary
                                            
                                                    
                                                    
                                                    
                                                    Block_101_2_1_binary=""


                                                    #Predict

                                                    Block_10T=Block_10e+1
                                                    #print(Block_10T)
                                                    
                                                    Block_10TU10=Block_10T%10
                                                    Block_10TU11=Block_10T%11
                                                    if Block_10T==1:
                                                        Block_10T_U=Block_10T+1 
                                                        Block_10R=Block_101E+1
                                                    
                                                        
                                                    elif Block_10TU11==0:
                                                        Block_10T_U=Block_10T+Block_10T
                                                        Block_10R=Block_101E+Block_101E
                                                        
                                                    elif Block_10TU10==0:
                                                        Block_10T_U=Block_10T+Block_10T
                                                        Block_10R=Block_101E+Block_101E
                                                        
                                                    else:
                                                        Block_10T_U=Block_10T
                                                        Block_10R=Block_101E
                                                        
                                                    
                                                    Block_10T1=str(Block_10T_U)

                                                    Block_10T4=Block_10T1
                                                    long1=len(Block_10T4)
                                            
                                                    


                                                                    
                                                    #print(Block_10T4)      
                                                            
                                                    
                                                    

                                                    Block_103=Block_10R+1
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary
                                            
                                                    Number_N18=INIT[block:block+2]

                                                    
                                                    Block_101_4_1_binary=Number_N18+Block_106_binary+"0"

                                                    X2="02"+Block_106_binary+"01"

                                                    X3="03"+Block_106_binary+"01"

                                                    X4="04"+Block_106_binary+"01"
                                                    X5="05"+Block_106_binary+"01"
                                                 
                                                    X6="06"+Block_106_binary+"01"
                                                        
                                                    X7="07"+Block_106_binary+"01"
                                                 
                                                    X8="08"+Block_106_binary+"01"
                                                        
                                                    X9="09"+Block_106_binary+"01"


                                                    long=len(Block_101_4_1_binary)
                                                    Number_N17=INIT[block:block+long]
                                                    Number_N12=Number_N17
                                                    X10=Number_N12
                                                    #print(Number_N12)
                                                    #print(Block_101_4_1_binary)
                                                    

                                                                                                        
                                                    
                                                    #print(Block_102_binary)
                                            if Circle_times2==0:
                                                    if Number_N==Block_102_binary:

                                                            Block_103=Block_101+1
                                                            Block_105_binary=str(Block_103)

                                                            Block_106_binary=Block_105_binary
                                                    
                                                            Number_N4=Number_N4+Block_106_binary+"0"
                                                            if Block_101==1:
                                                                    block=block+3
                                                            else:
                                                                    block=block+6
                                                                    
                                                    
                                                    elif Number_N==Block_122_binary:

                                                            Block_103=Block_101+2
                                                            Block_105_binary=str(Block_103)

                                                            Block_106_binary=Block_105_binary
                                                    
                                                            Number_N4=Number_N4+Block_106_binary+"0"
                                                            if Block_101==1:
                                                                    block=block+3
                                                            else:
                                                                    block=block+6
                                                
                                                            #print(Block_106_binary)
                                                    elif Number_N==Block_123_binary:

                                                            Block_103=Block_101+3
                                                            Block_105_binary=str(Block_103)

                                                            Block_106_binary=Block_105_binary
                                                    
                                                            Number_N4=Number_N4+Block_106_binary+"0"
                                                            if Block_101==1:
                                                                    block=block+3
                                                            else:
                                                                    block=block+6


                                                    elif Number_N==Block_101_1_binary:

                                                            Block_103=Block_101+4
                                                            Block_105_binary=str(Block_103)

                                                            Block_106_binary=Block_105_binary
                                                    
                                                            Number_N4=Number_N4+Block_106_binary+"0"
                                                            if Block_101==1:
                                                                    block=block+3
                                                            else:
                                                                    block=block+6

                                                    elif Number_N==Block_101_2_binary:

                                                            Block_103=Block_101+5
                                                            Block_105_binary=str(Block_103)

                                                            Block_106_binary=Block_105_binary
                                                    
                                                            Number_N4=Number_N4+Block_106_binary+"0"
                                                            if Block_101==1:
                                                                    block=block+3
                                                            else:
                                                                    block=block+6
                                                            
                                                    elif Number_N==Block_101_3_binary:

                                                            Block_103=Block_101+6
                                                            Block_105_binary=str(Block_103)

                                                            Block_106_binary=Block_105_binary
                                                    
                                                            Number_N4=Number_N4+Block_106_binary+"0"
                                                            if Block_101==1:
                                                                    block=block+3
                                                            else:
                                                                    block=block+6


                                                    elif Number_N==Block_101_1_1_binary:

                                                            Block_103=Block_101+7
                                                            Block_105_binary=str(Block_103)

                                                            Block_106_binary=Block_105_binary
                                                    
                                                            Number_N4=Number_N4+Block_106_binary+"0"
                                                            if Block_101==1:
                                                                    block=block+3
                                                            else:
                                                                    block=block+6

                                                    elif Number_N==Block_101_2_1_binary:

                                                            Block_103=Block_101+8
                                                            Block_105_binary=str(Block_103)

                                                            Block_106_binary=Block_105_binary
                                                    
                                                            Number_N4=Number_N4+Block_106_binary+"0"
                                                            if Block_101==1:
                                                                    block=block+3
                                                            else:
                                                                    block=block+6
                                                            #print(Number_N4)
                                                    
                                                    else:
                                                            #print(Block_101_4_1_binary

                                                           
                                                            Number_N4=Number_N4+"0"+Number_N
                                                            #print(Block_10T4+"1")
                                                            block=block+3                
                                            if Circle_times2!=0:
                                                    if X10==X2 or X10==X2 or X10==X3 or X10==X4  or X10==X5  or X10==X6 or X10==X7 or X10==X8 or X10==X9 
                                                            #print(Block_101_4_1_binary)

                                                           
                                                            Number_N4=Number_N4+Number_N18+Block_10T4+"1"
                                                            #print(Block_10T4+"1")
                                                            block=block+long

                                                  
                                                    else:
                                                            #print(Block_101_4_1_binary

                                                           
                                                            Number_N4=Number_N4+Number_N
                                                            #print(Block_10T4+"1")
                                                            block=block+6
                                            
                                                    
                                    Block_101=Block_101+1
                                    Block_10e=Block_10e+1
                                    Block_101E=Block_101E+1
                                    #print(Block_101)

                                    
                                    
                                   
                                  
                                    if compress_or_not_compress==1:
                                    	
                                    	    Equal_info_between_of_the_cirlce_of_the_file_17=Number_N4
                                    	    #print(Number_N4)
                                   
                                    
     
                                    if compress_or_not_compress==1:
                                           
                                            Equal_info_between_of_the_cirlce_of_the_file_17=Number_N4
                                            sda18=Equal_info_between_of_the_cirlce_of_the_file
                                            #print(len(Equal_info_between_of_the_cirlce_of_the_file_17))
                              
                                    
                                    lenfS=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    #print(lenfS)

                                    

                                    if compress_or_not_compress==2 and Circle_times2==0:
                                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[1:]
                                    
                                   
                                    Circle_times2=Circle_times2+1
                          
                                    Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file_17

                                    if compress_or_not_compress==2:
                                            
                                            Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file

                                    if compress_or_not_compress1==3:


                                            lenf6=len(Equal_info_between_of_the_cirlce_of_the_file_17)

                                            INIT=""
                                            Number_N=""
                                            INIT=Equal_info_between_of_the_cirlce_of_the_file_17
                                            block=0
                                            Number_N4=""

                                            while block<lenf6:
                                                    Number_N1=INIT[block:block+1]
                                                    if Number_N1=="1":
                                                            Number_N4=Number_N4+"0"

                                                    elif Number_N1=="0":
                                                            Number_N4=Number_N4+"1"

                                                    else:
                                                            Number_N4=Number_N4+Number_N1

                                                    block=block+1
                                                             
                                            Number_N5=int(Number_N4)
                                            Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_N5)[2:]
                                   
                                    
                                    if   lenfS<=Deep3 or compress_or_not_compress==2:
                                        Circle_times3=Circle_times2
                                        
                                        if compress_or_not_compress==2:
                                        	Circle_times3=Circle_times2-1


                                    
                                            		

                                    
                                    

                                    if   lenfS<=Deep3 or compress_or_not_compress1==3:
                                            lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)                                           
                                            Equal_info_between_of_the_cirlce_of_the_file_17="1"+Equal_info_between_of_the_cirlce_of_the_file_17
                                            lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)

                                    if   lenfS<=Deep3 or compress_or_not_compress1==3:
                                                
                                            	add_bits=""
                                            	count_bits=8-lenf%8
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=8:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                    if   lenfS<=Deep3 or compress_or_not_compress1==3:
                                            Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                            
                                    if   lenfS<=Deep3 or compress_or_not_compress1==3:
                                                
                                    		L=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    		n = int(Equal_info_between_of_the_cirlce_of_the_file_17, 2)
                                    		width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    		width_bits=(width_bits//8)*2
                                    		width_bits=str(width_bits)
                                    		width_bits="%0"+width_bits+"x"
                                    		width_bits3=binascii.unhexlify(width_bits % n)
                                    		width_bits2=len(width_bits3)
                                    		add_bitszzza=""
                                    		add_bitszs=""
                                    		Equal_info_between_of_the_cirlce_of_the_file_2=Times_6
                                    		
                                    		with open(nameas, "wb") as f2:
                                    			f2.write(width_bits3)
                                    	
                                    		x2 = time()
                                    		x3=x2-x
                                    		xs=float(x3)
                                    		return print(x3)
                                if i==2:

                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                              
                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                    
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)

                                    add_bits=""

                                    Times_6=""

                                    #Extract

                                    sda10=""
                                    Translate_info_Decimal=""
                                  
                                    Number_add_plus_one=""
                                    Prime_Not=""
                                    Times_6=""
                                
                                    Number_of_the_file=0
                                    Prime_Not=0
                                 
                                    if C==1:
                                        if   Circle_times2==0:

                                                Translate_info_Decimal=Equal_info_between_of_the_cirlce_of_the_file[0:8]
                                                Translate_info_Decimal_2 = int(Translate_info_Decimal, 2)
                                                if Translate_info_Decimal_2>7:
                                                        Corrupted=1
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[8:]
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)

                                                sda10=Equal_info_between_of_the_cirlce_of_the_file[0:16]
                                                Deep5 = int(sda10, 2)
                                                Deep5=Deep5+2
                                                Deep4=Deep5-1
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[16:]
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                                Deep7=Deep5-2
                                                
                                                Times_6=Equal_info_between_of_the_cirlce_of_the_file[0:48]
                                                T = int(Times_6, 2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[48:]
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                                print("Deep: ")
                                                print(Deep7-25)
                                                
                                        if   Circle_times2>0:
                                        	Translate_info_Decimal_2=0
                                        
                                        	
    
                                        if C==1 and T!=0:
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[Translate_info_Decimal_2:]
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                                Number_add_plus_one=Equal_info_between_of_the_cirlce_of_the_file[lenf6-Deep4:lenf6-1]
                                                Prime_Not=Equal_info_between_of_the_cirlce_of_the_file[lenf6-1:lenf6]
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[0:lenf6-Deep4]
                                        
                                                
                                                Number_of_the_file = int(Equal_info_between_of_the_cirlce_of_the_file, 2)
                                                Number_add_plus_one_2 = int(Number_add_plus_one, 2)
                                                Prime_Not = int(Prime_Not, 2)
                                                Hole_Number_information=(2**Deep5)-1
                                                add_ones_together=Hole_Number_information+Number_add_plus_one_2
                                                Number_of_the_file=Number_of_the_file*add_ones_together
                                                Number_of_the_file=Number_of_the_file+Prime_Not
                                       
                                    Times_6=Number_add_plus_one
                                    Number_add_plus_one=""
                                      
                                    #####################################################################################################################################################
                                   
                                    Prime_Not=""
                                    
                                    
                                    Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file)[2:]
                                     
                                    Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file_17
                                   

                                    if i==2:
                                        Make_togher=""
                                        Make_togher=Times_6
                                        Number_add_plus_one=""
                                        add_bits=""
                                        if C==1 and T!=0:
                                                Circle_times2=Circle_times2+1

                                        lenf9=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                        #print(Circle_times2)
                                        
                                        
                                        if  Circle_times2==T:
                                        	   
                                            if C==1 and T==0:
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file
                                            	lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	add_bits=""
                                            	count_bits=8-lenf%8
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=8:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                        
                                            if C==1 and T!=0:
 
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file)[3:]
                                            	lenf14=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	#print(lenf14)
                                            	lenf16=lenf14%8
                                            	if lenf16!=0 or lenf14>=((2**40)-1)*8 or Corrupted==1:

                                            		print("file corrupted")
                                            		raise SystemExit
                                            		
                                            	
                                            	lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	add_bits=""
                                            	count_bits=8-lenf%8
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=8:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17

                                            L=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                         
                                            n = int(Equal_info_between_of_the_cirlce_of_the_file_17, 2)
                                            width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            width_bits=(width_bits//8)*2
                                            width_bits=str(width_bits)
                                            width_bits="%0"+width_bits+"x"
                                            width_bits3=binascii.unhexlify(width_bits % n)
                                            width_bits2=len(width_bits3)

                                            add_bitszzza=""
                                            add_bitszs=""
                                            Equal_info_between_of_the_cirlce_of_the_file_2=Times_6
                                             
                                            with open(nameas, "wb") as f2:
                                            
                                              
                                            	f2.write(width_bits3)
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            return print(x3)
   
d=compression()

xw1=d.cryptograpy_compression4()
print(xw1)
