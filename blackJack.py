import sys
import random
import os
import time

deck = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
global total
global newTotal
add = 0
add2 = 0
temp = 0
temp2 = 0

n = 2
playerHand = random.sample(deck, n)
n = 1
dealerHand = random.sample(deck, n)

cardToCountMap = {
    'A': None,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}

def rules():
    cmd = "clear"
    os.system(cmd)
    print("\n\t==========  Rules of the Game  ==========")
    print("")
    print("\t1.  Achieve \'21\' without going over.")
    print("\t2.  Beat the dealer to closest to \'21\'"
    "\n\twhithout going over.")
    print("\t3.  If you get \'21\' or closest to it,"
    "\n\tyou win.")
    print("\t4.  If the dealer gets \'21\' or closest"
    "\n\tto it, you lose.")
    print("\t5.  All \'J\', \'Q\', \'K\' equal 10.")
    print("\t6.  All \'A\' are either 11 or 1.")
    print("")
    print("\t\t\tGood Luck!")
    print("\t=========================================")

def start():
    question = "\n\tAre you ready to play? "
    reply = [0]
    while 1:
        reply = str(input(question+' \t(y/n): ')).lower().strip()
        if reply[0] == 'y':
            drawCards()
            break
        elif reply[0] == 'n':
            print("\n\t\t\tHave a good day!\n")
            print("\t=========================================")
            time.sleep(3)
            cmd = 'clear'
            os.system(cmd)
            exit(1)
        else:
            print("\t\t\tSorry, didn't catch that.")

def drawCards():
    print("")
    print("\t=========================================")
    print("\n\tYour Hand: \t\tDealers Hand:")
    print("\t" +str(playerHand)[1:-1] +"\t\t" +str(dealerHand)[1:-1] +", ?")

    if(playerHand[0] == 'A' and playerHand[1] == 'J' or playerHand[0] == 'A' and playerHand[1] == 'Q' or playerHand[0] == 'A' and playerHand[1] == 'K'):
        #print("\t" +str(hit)[1:-1] +"\tTotal:" +str(newTotal))
        print("\n\t\t====  You Win!!  ====")
    elif(playerHand[0] == 'J' and playerHand[1] == 'A' or playerHand[0] == 'Q' and playerHand[1] == 'A' or playerHand[0] == 'K' and playerHand[1] == 'A'):
        #print("\t" +str(hit)[1:-1] +"\tTotal:" +str(newTotal))
        print("\n\t\t====  You Win!!  ====")
    else:
        decision()

def decision():
    print("\t=========================================")
    question = "\n\tDo you want to hit or stay? "
    reply = [0]
    while 1:
        reply = str(input(question+' \t(h/s): ')).lower().strip()
        if reply[0] == 'h':
            print("")
            print("\t=========================================")
            hit(add)
            break
        elif reply[0] == 's':
            print("\n\t\t      Dealers turn.")
            dealer(None, None) #TODO - seems like this functions doesnt need any parameters
            break
        else:
            print("\t\tSorry, didn't catch that.")

def hit(add):
    n = 1

    print("\n\tYour Hand: \t\tDealers Hand:")
    print("\t" +str(playerHand)[1:-1] +"\t\t" +str(dealerHand)[1:-1] +", ?")

    global count
    if playerHand[0] == 'A':
        ace(total, newTotal)
    else:
        count = cardToCountMap[playerHand[0]]
    
    global count2
    if playerHand[1] == 'A':
        ace(total, newTotal)
    else:
        count2 = cardToCountMap[playerHand[1]]

    total = count + count2
    temp2 == total

    global count3
    global temp3
    hit = random.sample(deck,n)
    if hit[0] == 'A':
        ace(total, newTotal)
    else:
        count3 = cardToCountMap[hit[0]]
    newTotal = total + count3

    if newTotal == 21:
        print("\t" +str(hit)[1:-1] +"\tTotal:" +str(newTotal))
        print("\n\t\t====  You Win!!  ====")
        #playAgain()

    elif newTotal > 21:
        print("\t" +str(hit)[1:-1] +"\tTotal:" +str(newTotal))
        print("\n\t\t       Busted!")
        print("\t\t====  You Lose!  ====")
        #playAgain()

    else:
        add += newTotal
        print("\t" +str(hit)[1:-1] +"\tTotal:" +str(add))
        temp == add
        nextHit()

def nextHit():
    print("\t=========================================")
    question = "\n\tDo you want to hit or stay? "
    reply = [0]
    while 1:
        reply = str(input(question+' \t(h/s): ')).lower().strip()
        if reply[0] == 'h':
            print("")
            print("\t=========================================")
            hit(add)
            break
        elif reply[0] == 's':
            print("\n\t\t      Dealers turn.")
            dealer(hit, add)
            break
        else:
            print("\t\tSorry, didn't catch that.")

def dealer(hit, add):
    print("\t=========================================")
    print("\n\tYour Hand: \t\tDealers Hand:")
    print("\t" +str(playerHand)[1:-1] +"\t\t" +str(dealerHand)[1:-1] +", ?")
    #print("\t" +str(hit)[1:-1] +"\tTotal:" +str(add))

    n = 1
    dealerHand2 = random.sample(deck, n)
    hand = str(dealerHand)[1:-1] +", " +str(dealerHand2)[1:-1]

    count = 0
    if dealerHand[0] == 'A':
        count = 11
    else: 
        count = cardToCountMap[dealerHand[0]]

    count2 = 0
    if dealerHand2[0] == 'A':
        count2 = 11
    else:
        count2 = cardToCountMap[dealerHand2[0]]

    total = count + count2
    if total == 21:
        print("\t\t\t\t" +hand +"  is: " +str(total))
        print("\n\t\t====  Dealer Wins!!  ====")
        #playAgain()
    else:
        hit = random.sample(deck,n)

        newTotal = 0
        count3 = 0
        if hit[0] == 'A':
            count3 == 11
        else:
            count3 = cardToCountMap[hit[0]]
        newTotal = total + count3

        print("\t\t\t\t" +str(hit)[1:-1] +"\tTotal:" +str(newTotal))

        if newTotal == 21:
            #print("\t" +str(hit)[1:-1] +"\tTotal:" +str(newTotal))
            print("\n\t\t====  You Lose!  ====")
            #playAgain()

        elif newTotal > 21:
            #print("\t" +str(hit)[1:-1] +"\tTotal:" +str(newTotal))
            print("\n\t\t    Dealer Busted!")
            print("\t\t====  You Win!!  ====")
            #playAgain()
        else:
            determineWinner(newTotal, temp, temp2)

def ace(total, newTotal):
    question = "\n\tYou have an Ace, do you want to make that a 1 or an 11? "
    reply = [0]
    while 1:
        reply = str(input(question+' \t(1/11): ')).lower().strip()
        if reply[0] == '1':
            count, count2, count3 = 1
            newTotal = total + 1
            break
        elif reply[0] == '11':
            count, count2, count3 = 11
            newTotal = total + 11
            break
        else:
            print("\t\t\tSorry, didn't catch that.")

def determineWinner(newTotal, temp, temp2):
    if temp > newTotal:
        print("\n\t\t====  You Win!!  ====")
    elif temp2 > newTotal:
        print("\n\t\t====  You Win!!  ====")
    else:
        print("\n\t\t====  You Lose!  ====")

def playAgain():
    question = "\n\tWant to play again? "
    reply = [0]
    while 1:
        reply = str(input(question+' \t(y/n): ')).lower().strip()
        if reply[0] == 'y':
            cmd = 'python3 blackJack.py'
            os.system(cmd)
            break
        elif reply[0] == 'n':
            print("\n\t\t\tHave a good day!\n")
            print("\t=========================================")
            time.sleep(3)
            cmd = 'clear'
            os.system(cmd)
            exit(1)
        else:
            print("\t\t\tSorry, didn't catch that.")

def main(argv):
    rules()
    start()
    playAgain()

if __name__ == "__main__":
    main(sys.argv)
