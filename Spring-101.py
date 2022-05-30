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
                        Block_10eT_T=0   
                        compress_or_not_compress1=0
                        Block_10e=2
                        Predict_Number=10
                        Predict_Number2=10
                        Last_bits=""
                        Last_bits_Save=""
                        File_stop=1
                        E=0
                        Block_file=0
                        Block_file2=-1024
                        Block_count=1

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
                        Compress_times=0
                       
                       
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
               
                                    if  Circle_times2==0 and SpinS==0:
                                        Equal_info_between_of_the_cirlce_of_the_file="1"+Equal_info_between_of_the_cirlce_of_the_file
                                        SpinS=1

                                   


                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                           
                                   
                                    INIT=""
                                    Number_N=""
                                    INIT=Equal_info_between_of_the_cirlce_of_the_file
                                    if Block_101!=1:
                                        INIT[Block_file2:Block_file]
                                    #print(INIT)
                                    block=0
                                    Block_10T=0
                                    Number_N4=""

                                   
                                    Predict_Number=Predict_Number2
                                    Predict_Number3=Predict_Number2
                                    Predict_Number4=str(Predict_Number3)
                                    Number_Predict_Save=0
                                    E=0
                                   

                                    while block<lenf6:
                                            Number_N1=INIT[block:block+1]
                                            Number_N2=INIT[block+1:block+2]
                                            Number_N3=INIT[block+2:block+3]
                                            Number_N14=INIT[block+3:block+4]
                                            Number_N15=INIT[block+4:block+5]
                                            Number_N16=INIT[block+5:block+6]
                                         
                                            Block_101_binary=bin(Block_101)[2:]

                                            if Block_101==1:
                                                    Last_bits=Number_N1+Number_N2+Number_N3
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

                                                   
                                                    Block_10T=Block_10T
                                                    Block_10E=Block_101E
                                                       
                                                   
                                                    Block_10T1=str(Block_10T_U)

                                                    Block_10T4=Block_10T1
                                                    long1=len(Block_10T4)
                                                   
                                       
                                                   


                                                                   
                                                    #print(Block_10T4)     
                                                           
                                                 

                                                    Block_103=Predict_Number
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary
                                           
                                                   

                                                   
                                                    Block_101_4_1_binary=Block_106_binary

                                                    X2=Block_106_binary
                                                    long1=len(X2)


                                                    Predict_Number11=Predict_Number+1
                                                    if  Predict_Number11==100:
                                                            Predict_Number11=10
                                                           


                                                    Block_1031=Predict_Number11
                                                    Block_1051_binary=str(Block_1031)

                                                    Block_10611_binary=Block_1051_binary
                                           
                                                   

                                                   
                                                    Block_101_4_11_binary=Block_10611_binary

                                                    X12=Block_10611_binary
                                                    long11=len(X12)
                                                    #print(X2)

                                                 
                                                    long=len(Block_101_4_1_binary)
                                                    Number_N17=INIT[block:block+long]
                                                    Number_N12=Number_N17
                                                    X10=Number_N12
                                                    #print(Number_N12)
                                                    #print(Block_101_4_1_binary)
                                                   

                                                                                                       
                                                   
                                                    #print(Block_102_binary)
                                            if Block_101==1:
                                                    if Number_N==Block_102_binary:

                                                            Block_103=Block_101+1
                                                            Block_105_binary=str(Block_103)

                                                            Block_106_binary=Block_105_binary
                                                   
                                                            Number_N4=Number_N4+Block_106_binary
                                                            if Block_101==1:
                                                                    block=block+3
                                                            else:
                                                                    block=block+6
                                                                   
                                                   
                                                    elif Number_N==Block_122_binary:

                                                            Block_103=Block_101+2
                                                            Block_105_binary=str(Block_103)

                                                            Block_106_binary=Block_105_binary
                                                   
                                                            Number_N4=Number_N4+Block_106_binary
                                                            if Block_101==1:
                                                                    block=block+3
                                                            else:
                                                                    block=block+6
                                               
                                                            #print(Block_106_binary)
                                                    elif Number_N==Block_123_binary:

                                                            Block_103=Block_101+3
                                                            Block_105_binary=str(Block_103)

                                                            Block_106_binary=Block_105_binary
                                                   
                                                            Number_N4=Number_N4+Block_106_binary
                                                            if Block_101==1:
                                                                    block=block+3
                                                            else:
                                                                    block=block+6


                                                    elif Number_N==Block_101_1_binary:

                                                            Block_103=Block_101+4
                                                            Block_105_binary=str(Block_103)

                                                            Block_106_binary=Block_105_binary
                                                   
                                                            Number_N4=Number_N4+Block_106_binary
                                                            if Block_101==1:
                                                                    block=block+3
                                                            else:
                                                                    block=block+6

                                                    elif Number_N==Block_101_2_binary:

                                                            Block_103=Block_101+5
                                                            Block_105_binary=str(Block_103)

                                                            Block_106_binary=Block_105_binary
                                                   
                                                            Number_N4=Number_N4+Block_106_binary
                                                            if Block_101==1:
                                                                    block=block+3
                                                            else:
                                                                    block=block+6
                                                           
                                                    elif Number_N==Block_101_3_binary:

                                                            Block_103=Block_101+6
                                                            Block_105_binary=str(Block_103)

                                                            Block_106_binary=Block_105_binary
                                                   
                                                            Number_N4=Number_N4+Block_106_binary
                                                            if Block_101==1:
                                                                    block=block+3
                                                            else:
                                                                    block=block+6


                                                    elif Number_N==Block_101_1_1_binary:

                                                            Block_103=Block_101+7
                                                            Block_105_binary=str(Block_103)

                                                            Block_106_binary=Block_105_binary
                                                   
                                                            Number_N4=Number_N4+Block_106_binary
                                                            if Block_101==1:
                                                                    block=block+3
                                                            else:
                                                                    block=block+6

                                                    elif Number_N==Block_101_2_1_binary:

                                                            Block_103=Block_101+8
                                                            Block_105_binary=str(Block_103)

                                                            Block_106_binary=Block_105_binary
                                                   
                                                            Number_N4=Number_N4+Block_106_binary
                                                            if Block_101==1:
                                                                    block=block+3
                                                            else:
                                                                    block=block+6
                                                            #print(Number_N4)
                                                   
                                                    else:
                                                            #print(Block_101_4_1_binary

                                                         
                                                            Last_bits_Save=Last_bits
                                                            #print(Block_10T4+"1")
                                                            block=block+3               
                                            if Block_101!=1:
                                               
                                               
                                                    if X10==X2 and long1==2:
                                                            #print(Block_101_4_1_binary)

                                                         
                                                            Number_N4=Number_N4+"1"
                                                            #print(X2)
                                                            block=block+long
                                                            Number_Predict_Save=1
                                                           
                                                           
                                                    if X10==X12 and long11==2:
                                                            #print(Block_101_4_1_binary)

                                                         
                                                            Number_N4=Number_N4+"0"
                                                            #print(X2)
                                                            block=block+long
                                                            Number_Predict_Save=1
                                                           
                                                 
                                                 
                                                    else:
                                                            #print(Block_101_4_1_binary

                                                         
                                                            Number_N4=Number_N4+Number_N1
                                                            #print(Block_10T4+"1")
                                                            block=block+1
                                           
                                                    Predict_Number=Predict_Number+1#
                                                    if Predict_Number==100:
                                                            Predict_Number=10
                                    if Block_101==1:
                                        Block_101=2
                                   
                                       
                                       
                                    Block_10e=Block_10e+1
                                    Block_101E=Block_101E+1
                                    if Number_Predict_Save==1:
                                           
                                            if Predict_Number3==10:
                                                    Predict_Number4="222"
                                            if Predict_Number3==11:
                                                    Predict_Number4="223"
                                            if Predict_Number3==12:
                                                    Predict_Number4="224"
                                            if Predict_Number3==13:
                                                    Predict_Number4="225"
                                            if Predict_Number3==14:
                                                    Predict_Number4="226"
                                            if Predict_Number3==15:
                                                    Predict_Number4="227"

                                            if Predict_Number3==16:
                                                    Predict_Number4="228"

                                            if Predict_Number3==17:
                                                    Predict_Number4="229"

                                            if Predict_Number3==18:
                                                    Predict_Number4="232"
                                                   
                                            if Predict_Number3==19:
                                                    Predict_Number4="233"


                                            if Predict_Number3==20:
                                                    Predict_Number4="234"
                                            if Predict_Number3==21:
                                                    Predict_Number4="235"
                                            if Predict_Number3==22:
                                                    Predict_Number4="236"
                                            if Predict_Number3==23:
                                                    Predict_Number4="237"
                                            if Predict_Number3==24:
                                                    Predict_Number4="238"
                                            if Predict_Number3==25:
                                                    Predict_Number4="239"

                                            if Predict_Number3==26:
                                                    Predict_Number4="242"

                                            if Predict_Number3==27:
                                                    Predict_Number4="243"

                                            if Predict_Number3==28:
                                                    Predict_Number4="244"
                                                   
                                            if Predict_Number3==29:
                                                    Predict_Number4="245"


                                            if Predict_Number3==30:
                                                    Predict_Number4="246"
                                            if Predict_Number3==31:
                                                    Predict_Number4="247"
                                            if Predict_Number3==32:
                                                    Predict_Number4="248"
                                            if Predict_Number3==33:
                                                    Predict_Number4="249"
                                            if Predict_Number3==34:
                                                    Predict_Number4="252"
                                            if Predict_Number3==35:
                                                    Predict_Number4="253"

                                            if Predict_Number3==36:
                                                    Predict_Number4="254"

                                            if Predict_Number3==37:
                                                    Predict_Number4="255"

                                            if Predict_Number3==38:
                                                    Predict_Number4="256"
                                                   
                                            if Predict_Number3==39:
                                                    Predict_Number4="257"

                                            if Predict_Number3==40:
                                                    Predict_Number4="258"

                                            if Predict_Number3==41:
                                                    Predict_Number4="259"
                                                   
                                            if Predict_Number3==42:
                                                    Predict_Number4="262"

                                            if Predict_Number3==43:
                                                    Predict_Number4="263"

                                            if Predict_Number3==44:
                                                    Predict_Number4="264"

                                            if Predict_Number3==45:
                                                    Predict_Number4="265"

                                            if Predict_Number3==46:
                                                    Predict_Number4="266"

                                            if Predict_Number3==47:
                                                    Predict_Number4="267"
                                                   
                                            if Predict_Number3==48:
                                                    Predict_Number4="268"

                                            if Predict_Number3==49:
                                                    Predict_Number4="269"

                                            if Predict_Number3==50:
                                                    Predict_Number4="272"

                                            if Predict_Number3==51:
                                                    Predict_Number4="273"



                                            if Predict_Number3==52:
                                                    Predict_Number4="274"
                                            if Predict_Number3==53:
                                                    Predict_Number4="275"
                                            if Predict_Number3==54:
                                                    Predict_Number4="276"
                                            if Predict_Number3==55:
                                                    Predict_Number4="277"
                                            if Predict_Number3==56:
                                                    Predict_Number4="278"
                                            if Predict_Number3==57:
                                                    Predict_Number4="279"

                                            if Predict_Number3==58:
                                                    Predict_Number4="282"

                                            if Predict_Number3==59:
                                                    Predict_Number4="283"

                                            if Predict_Number3==60:
                                                    Predict_Number4="284"
                                                   
                                            if Predict_Number3==61:
                                                    Predict_Number4="285"


                                            if Predict_Number3==62:
                                                    Predict_Number4="286"
                                            if Predict_Number3==63:
                                                    Predict_Number4="287"
                                            if Predict_Number3==64:
                                                    Predict_Number4="288"
                                            if Predict_Number3==65:
                                                    Predict_Number4="289"
                                            if Predict_Number3==66:
                                                    Predict_Number4="292"
                                            if Predict_Number3==67:
                                                    Predict_Number4="293"

                                            if Predict_Number3==68:
                                                    Predict_Number4="294"

                                            if Predict_Number3==69:
                                                    Predict_Number4="295"

                                            if Predict_Number3==70:
                                                    Predict_Number4="296"
                                                   
                                            if Predict_Number3==71:
                                                    Predict_Number4="297"


                                            if Predict_Number3==72:
                                                    Predict_Number4="298"
                                            if Predict_Number3==73:
                                                    Predict_Number4="299"
                                            if Predict_Number3==74:
                                                    Predict_Number4="322"
                                            if Predict_Number3==75:
                                                    Predict_Number4="323"
                                            if Predict_Number3==76:
                                                    Predict_Number4="324"
                                            if Predict_Number3==77:
                                                    Predict_Number4="325"

                                            if Predict_Number3==78:
                                                    Predict_Number4="326"

                                            if Predict_Number3==79:
                                                    Predict_Number4="327"

                                            if Predict_Number3==80:
                                                    Predict_Number4="328"
                                                   
                                            if Predict_Number3==81:
                                                    Predict_Number4="329"

                                            if Predict_Number3==82:
                                                    Predict_Number4="332"

                                            if Predict_Number3==83:
                                                    Predict_Number4="333"
                                                   
                                            if Predict_Number3==84:
                                                    Predict_Number4="334"

                                            if Predict_Number3==85:
                                                    Predict_Number4="335"

                                            if Predict_Number3==86:
                                                    Predict_Number4="336"

                                            if Predict_Number3==87:
                                                    Predict_Number4="337"

                                            if Predict_Number3==88:
                                                    Predict_Number4="338"

                                            if Predict_Number3==89:
                                                    Predict_Number4="339"
                                                   
                                            if Predict_Number3==90:
                                                    Predict_Number4="342"

                                            if Predict_Number3==91:
                                                    Predict_Number4="343"

                                            if Predict_Number3==92:
                                                    Predict_Number4="344"

                                            if Predict_Number3==93:
                                                    Predict_Number4="345"

                                            if Predict_Number3==94:
                                                    Predict_Number4="346"

                                            if Predict_Number3==95:
                                                    Predict_Number4="347"

                                            if Predict_Number3==96:
                                                    Predict_Number4="348"

                                            if Predict_Number3==97:
                                                    Predict_Number4="349"
                                               
                                            if Predict_Number3==98:
                                                    Predict_Number4="352"

                                            if Predict_Number3==99:
                                                    Predict_Number4="353"

                                            Number_N4=Predict_Number4+Number_N4

                                            if Block_count==254:

                                                Block_file=1024
                                                Block_file2=-1024
                                                Block_count=0
                                                Block_101=1

                                            Block_file=Block_file+1024
                                            Block_file2=Block_file2+1024
                                            Block_count=Block_count+1

                                           

                                           
                                         
                                            Equal_info_between_of_the_cirlce_of_the_file_17=Number_N4
                                           

                                           
                                            lenf6=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                                                       

                                            INIT=""
                                            Number_N=""
                                            INIT=Equal_info_between_of_the_cirlce_of_the_file_17
                                            block=0
                                            Number_N4=""

                                            while block<lenf6:
                                                    Number_N1=INIT[block:block+1]
                                                   
                                                    if Number_N1=="0":
                                                            Number_N4=Number_N4+"9"

                                                    elif Number_N1=="1":
                                                            Number_N4=Number_N4+"8"


                                                    elif Number_N1=="2":
                                                            Number_N4=Number_N4+"7"

                                                    elif Number_N1=="3":
                                                            Number_N4=Number_N4+"6"

                                                    elif Number_N1=="4":
                                                            Number_N4=Number_N4+"5"

                                                    elif Number_N1=="5":
                                                            Number_N4=Number_N4+"4"

                                                    elif Number_N1=="6":
                                                            Number_N4=Number_N4+"3"

                                                    elif Number_N1=="7":
                                                            Number_N4=Number_N4+"2"


                                                    elif Number_N1=="8":
                                                            Number_N4=Number_N4+"1"

                                                    elif Number_N1=="9":
                                                            Number_N4=Number_N4+"0"



                                                    block=block+1
                                                   
                                            Equal_info_between_of_the_cirlce_of_the_file_17=Number_N4
                                           
                                            Number_N4=Equal_info_between_of_the_cirlce_of_the_file_17
                                       
                                           
                                            Compress_times=Compress_times+1
                                            E=1
                                           

                                       
                                           
                                    #print(Block_101)
                                    Predict_Number2=Predict_Number2+1
                                    if Predict_Number2==100:
                                            Predict_Number2=10
                                   
                                   
                                   
                                         
                                    if Block_10eT_T==1000:
                                          Block_10eT_T=0
                                         
                                          Block_10e=2
                                          Block_101E=2
                                         
                                    Block_10eT_T=Block_10eT_T+1     

                                   
                                   
                                 
                                 
                                    if compress_or_not_compress==1:
                                       
                                            Equal_info_between_of_the_cirlce_of_the_file_17=Number_N4
                                            #print(Number_N4)
                                 
                                   
   
                                    if compress_or_not_compress==1:
                                         
                                            Equal_info_between_of_the_cirlce_of_the_file_17=Number_N4
                                            sda18=Equal_info_between_of_the_cirlce_of_the_file
                                            #print(len(Equal_info_between_of_the_cirlce_of_the_file_17))
                             
                                   
                                    lenfS=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    #print(lenfS)

                                    if lenfS<20:
                                            File_stop=0

                                   

                                    if compress_or_not_compress==2 and Circle_times2==0:
                                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[1:]
                                   
                                 
                                    Circle_times2=Circle_times2+1
                         
                                    Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file_17

                                    if compress_or_not_compress==2:
                                                  
                                            Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file


                                    if Circle_times2==(2**16)-1:
                                            compress_or_not_compress1=3
                  


                                         
                                           
                                           
                                 
                                   
                                    if  lenfS<=Deep3 or compress_or_not_compress==2:
                                        Circle_times3=Circle_times2
                                       
                                        if compress_or_not_compress==2:
                                            Circle_times3=Circle_times2-1


                                   
                                    if  lenfS<=Deep3 or compress_or_not_compress1==3:

                                            Number_N4=Number_N4+INIT[(1024*254):]
                                            Number_N4=Number_N4+"0"+Last_bits_Save
                                            Equal_info_between_of_the_cirlce_of_the_file_17=Number_N4
                                            Last_bits_long=len(Last_bits_Save)
                                            Last_bits_long=Last_bits_long+1
                                            Last_bits_long_str=str(Last_bits_long)
                                            Number_N4=Last_bits_long_str+Number_N4
                                            Equal_info_between_of_the_cirlce_of_the_file_17=Number_N4

                                            Number_N5=int(Number_N4)

                                            Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_N5)[2:]
                                            Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file_17[::-1]
                                   

                                    if  lenfS<=Deep3 or compress_or_not_compress1==3:
                                            lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)                                         
                                            Equal_info_between_of_the_cirlce_of_the_file_17="1"+Equal_info_between_of_the_cirlce_of_the_file_17
                                            lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    if  lenfS<=Deep3 or compress_or_not_compress1==3:

                                                                                             
                                                times_compress=bin(Compress_times)[2:]
                                                lenf1=len(times_compress)
                                                add_bitst=""
                                               
                                                count_bitst=48-lenf1%48
                                                z=0
                                                if count_bitst!=0:
                                                        if count_bitst!=48:
                                                            while z<count_bitst:
                                                                add_bitst="0"+add_bitst
                                                                z=z+1

                                    if  lenfS<=Deep3 or compress_or_not_compress1==3:
                                               
                                                add_bits=""
                                                count_bits=8-lenf%8
                                                z=0
                                                if count_bits!=0:
                                                        if count_bits!=8:
                                                            while z<count_bits:
                                                                add_bits="0"+add_bits
                                                                z=z+1
                                    if  lenfS<=Deep3 or compress_or_not_compress1==3:
                                           
                                           
                                            Equal_info_between_of_the_cirlce_of_the_file_17=add_bitst+times_compress+add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                           
                                    if  lenfS<=Deep3 or compress_or_not_compress1==3:
                                               
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
                                        if  Circle_times2==0:

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
                                               
                                        if  Circle_times2>0:
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
