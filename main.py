import mykie_stat as mk
import myka_ev as my

counter = 1
while counter == 1:
    print ("\n[1] Stat Calculator")
    print ("[2] EV Calculator")
    num0 = int(input("Choose number: "))

    BAS = int (input("\nBase STAT:"))
    LVL = int (input("Level:"))
    EV = int (input("EV-HP:"))
    IV = int (input("IV-HP:"))
    STATS = int(input("Desired increase in stat:"))

    if num0 == 1:
        print ("\nHp = ", mk.mykie.hpcal(BAS,IV,EV,LVL))
        print ("Attack = ", mk.mykie.otherstat(BAS,IV,EV,LVL))
        print ("Defense = ", mk.mykie.otherstat(BAS,IV,EV,LVL))
        print ("Super Attack = ", mk.mykie.otherstat(BAS,IV,EV,LVL))
        print ("Super Defense = ", mk.mykie.otherstat(BAS,IV,EV,LVL))
        print ("SPEED = ", mk.mykie.otherstat(BAS,IV,EV,LVL))
        print ("\nThe needed Evs to increase stat is ", my.myka.evneed(STATS,BAS,IV,EV,LVL))
    
    elif num0 == 2:
        print ("\n[1] Single stat")
        print ("[2] All stat")
        num1 = int (input("Choose a number:"))

        if num1 == 1:
            print ("\n[1] Attack")
            print ("[2] DEFENSE")
            print ("[3] Super.ATTACK")
            print ("[4] Super.DEFENSE")
            print ("[5] SPEED")
            print ("[6] HP")
            num20= int (input ("Choose Stat:"))

            if num20 == 1 or 2 or 3 or 4 or 5:
                print ("\nThe Stat is", mk.mykie.otherstat(BAS,IV,EV,LVL))
            elif num20 == 6:
                print ("\nHp = ", mk.mykie.hpcal(BAS,IV,EV,LVL))

        elif num1 == 2:
            print ("\nHp =", mk.mykie.hpcal(BAS,IV,EV,LVL))
            print ("Attack =", mk.mykie.otherstat(BAS,IV,EV,LVL))
            print ("Defemse =", mk.mykie.otherstat(BAS,IV,EV,LVL))
            print ("Super. Attack =", mk.mykie.otherstat(BAS,IV,EV,LVL))
            print ("Super. Defense =", mk.mykie.otherstat(BAS,IV,EV,LVL))
            print ("SPEED=", mk.mykie.otherstat(BAS,IV,EV,LVL))
    
    print ("\n[1] Perform another calculation")
    print ("[2] End the program")
    num3 = int (input("Choose a number:"))
    if num3 ==2:
        break
    elif num3 == 1:
        continue