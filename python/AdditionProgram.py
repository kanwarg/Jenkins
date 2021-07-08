import numpy
from numpy.random.mtrand import randint






num1=0
num2=0
count=0

def generateRandomNumbers():
    global num1
    global num2
    num1=randint(0,20)
    num2=randint(0,20)


def inputMessage():
    print("please enter the sum of %d + %d = ?" %(num1, num2))



def calculate():
  sum = int(input())
  if(sum==(num1+num2)):
      print("Correct answer well done !!!\n")
      global count
      count=count+1
  else:
      print("Wrong answer")
      





def main():
    
     for i in range(10):
         generateRandomNumbers()
         inputMessage()
         calculate()

     global count
     print("Total correct answer is:" + str(count) + " out of 10")


    
    
 
if __name__=="__main__":
    main()
   
   