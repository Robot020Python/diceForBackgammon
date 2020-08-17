import random

def dice(n):
    n1 = """
  *
         """
    n2 = """*
    
    *"""
    n3 = """*
  *
    *"""
    n4 = """*   *
      
*   *"""
    n5 = """*   * 
  *
*   *"""
    n6 = """*   *
*   *
*   *   """ 
    kosti = [n1, n2, n3, n4, n5, n6]
    print(kosti[n-1])
    
def mixDice():
    for perem in range(2):
        n = random.randint(1, 6)   
        dice(n)
        print("-----")

#НАЧАЛО ПРОГРАММЫ
mix = "1"
while(mix != "0"):
    mix = input(" DO you want to mix the dice??? Yes = 1 ,  No = 0: ")
    if(mix == "1"):
        mixDice()
    elif(mix =="0"):
        print("Bye bye ")
    else:
        print("Can you write again???")













