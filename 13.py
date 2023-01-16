
import os
import sys
def Display_ext(length, *arguments):
    print(length)
    for arg in arguments :
    	path = arg[1]
    print(path)
#    path=arguments[1]
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for foldername, subfolder, filname in os.walk(path):
            print("Current folder is : "+foldername)

            for filen in filname:
                split = os.path.splitext(filen) 
	
                for i in range(2,length,1) :
                    for ext in arguments :
                        if(ext[i].startswith(".") == False ) :
                            ext[i]="."+ext[i]
                        if split[1] == ext[i]:
                                data = str(filen) +"\n"
                                print(data)
    else:
        print("Invalid Path")
length =len(sys.argv)
Display_ext(length, sys.argv)        
#Display_ext("C:/Users/poojanava - pc/Desktop/Msc-II/ML",".pdf")