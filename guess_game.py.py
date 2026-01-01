import random

def Menu():
    e = None   # initialize so the function can always return them
    l = None
    while True:
        print("Press 0 to Select Difficulty!")
        print("Press 1 to Start !")
        q = input()

        if q == "1":
            # Only break if difficulty was selected before
            if e is None or l is None:
                print("Select difficulty first!")
            else:
                return l,e

        elif q == "0":
            print("Choose !")
            print("""
                1) Type "E" for Easy Difficulty.
                2) Type "M" for Medium Difficulty.
                3) Type "H" for Hard Difficulty. 
            """)
            z = input().lower()

            if z == "e":
                l = 0
                e = 50
            elif z == "m":
                l = 0
                e = 100
            elif z == "h":
                l = 0
                e = 1000
            else:
                print("Invalid difficulty!")
        else:
            print("Please Enter a Valid Response!")
def hint(x, l, e):
    
    low = max(l, x - 10)
    high = min(e, x + 10)
    print(f"\n✔ The number is BETWEEN {low} and {high} (inclusive)")

def logic(x,l,e):
    c=1
    h=0
    points=1000
    while True:
            print ("\nType 'hint' to get help at cost of 400 points but you will only get ONE")
            print(f"\nPOINTS LEFT === {points} !!!")
            print(f"\nGuess a number between {l} and {e}")
            guess=input("Your Response: ").lower()
            if guess=="hint":
              if points<400:
                  print ("\nYOU CAN'T AFFORD IT !!!!!")
                  continue
              elif h>=1:
                  print("RUN OUT OF HINT !!!! ")
                  continue
              else:  
                   
                hint(x,l,e)
                h+=1
                points-=400
                continue
                
            if not guess.lstrip('-').isdigit() and guess!="hint":
                print("\nWRONG INPUT!!!!    PENALTY OF -100")
                points-=100
                if points<0:
                    print(f"\n____GAME OVER YOU LOST____Your final score: {points}")
                    break                
                print("\nPLEASE ENTER A VALID INTEGER!")

                c+=1
                continue

                
            guess=int(guess)
            if guess>e or guess<l:
                print("\nOUT OF RANGE !!!!    PENALTY OF -100")
                points-=100
                if points<0:
                    print(f"\n____GAME OVER YOU LOST____Your final score: {points}")
                    break                
                print("\nPLEASE BE IN RANGE!!!")

                c+=1
                continue
            if x==guess:
                 print(f"\n🎉 Congratulations! You made it in {c} guesses and your have scored {points} points")
                 break
            elif x!=guess:
                 if x>guess:
                     points-=50
                     if points<0:
                        print(f"\n____GAME OVER YOU LOST____Your final score: {points}")
                        break                                          
                     print("\nLOW → GO HIGHER")
                     
                     
                 elif x<guess:
                      points-=50
                      if points<0:
                        print(f"\n____GAME OVER YOU LOST____Your final score: {points}")
                        break                                             
                      print("\nHIGH → GO LOWER")
                      

            c+=1          
       

#Calling Menu() function and storing the returning value
while True:
    l, e = Menu()
    x = random.randint(l, e)
    logic(x, l, e)

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("\nThanks for playing! 👋")
        break
