import random
class Ramandsita:
    def __init__(self):
        li=["sita","lakshman","Hanuman"]
        ra=[]
        while(len(li)!=0):
            b=random.choice(li)
            ra.append(b)
            li.remove(b)
        print("End user is the ram")
        pos_of_sita=int(input())
        if pos_of_sita>len(ra):
            print("Invalid answer")
        elif pos_of_sita!=ra.index("sita"):
            print(" Wrong answer")
        elif pos_of_sita==ra.index("sita"):
            print("ram idedntified sita")
        else:
            pass
obj=Ramandsita()
