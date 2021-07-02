import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def hit():
    print(f'{bcolors.OKGREEN}Hit!{bcolors.ENDC}')
    return 'hit'
def stand():
    print(f'{bcolors.FAIL}Stand!{bcolors.ENDC}')
    return 'stand'
def double():
    print(f'{bcolors.WARNING}Double!{bcolors.ENDC}')
    return 'double'
def split():
    print(f'{bcolors.OKBLUE}Split!{bcolors.ENDC}')
    return 'split'

def calc(dealer, carta1, carta2):
    sum = carta1+carta2
    double = (carta1 == carta2)
    if (carta1 == 1): return card_a(dealer, carta2)
    elif (double): return card_d(dealer, carta1)
    elif (sum > 12 and not double): return card_h(dealer,sum)
    elif (sum > 4 and sum < 9): return hit()
    else: return card_m(dealer, sum)

def card_m(dealer, sum):
    if (sum == 12):
        if (dealer < 7 and dealer > 3):
            return stand()
        else:
            return hit()
    elif (sum == 11):
        if (dealer == 1):
            return hit()
        else:
            return double()
    elif (sum == 10):
        if (dealer == 1 or dealer == 10):
            return hit()
        else:
            return double()
    else:
        if (dealer < 6 and dealer > 2):
            return double()
        else:
            return hit()

def card_h(dealer, sum):
    if (dealer > 6 and sum < 17):
        return hit()
    else:
        return stand()

def card_d(dealer, carta1):
    if (carta1 == 8):
        return split()
    elif (carta1 == 10):
        return stand()
    elif (carta1 == 5):
        if (dealer == 10 or dealer == 1):
            return hit()
        else:
            return double()
    elif (carta1 == 7 or carta1 == 2 or carta1 == 3):
        if (dealer > 7 or dealer == 1):
            return hit()
        else:
            return split()
    elif (carta1 == 4):
        if(dealer == 5 or dealer == 6):
            return split()
        else:
            return hit()
    elif (carta1 == 6):
        if (dealer > 6 or dealer == 1):
            return hit()
        else:
            return split()
    else:
        if (dealer == 10 or dealer == 7 or dealer == 1):
            return stand()
        else:
            return split()

def card_a(dealer, carta2):
    if (carta2 == 1):
        return split()
    elif (carta2 == 7):
        if (dealer == 2 or dealer == 7 or dealer == 8):
            return stand()
        elif (dealer > 2 and dealer < 7):
            return double()
        else:
            return hit()       
    elif (carta2 > 7):
        return stand()
    elif (dealer > 6):
        return hit()
    else:
        if (dealer > 4):
            return double()
        elif (carta2 == 2 or carta2 == 3):
            return hit()
        elif (carta2 == 4 or carta2 == 5):
            if (dealer < 4):
                return hit()
            else:
                return double()
        else:
            if (dealer < 3):
                return hit()
            else:
                return double()

def subs_a(carta1, carta2):
    if (carta2 == 1):
        aux = carta1
        carta1 = carta2
        carta2 = aux
    return (carta1, carta2)

def card_c(dealer, carta1, carta2) -> int:
    count1=0
    cards = [dealer,carta1,carta2]
    for card in cards:
        if(card == 1 or card == 10): count1-=1
        if(card > 6 and card < 10): count1=count1
        if(card < 7 and card > 1): count1+=1
        if(card == 0): count1=count1
    return count1

resp = 'oi'

def main():
    count=[0,0]
    baralho=6
    while(1):
        cls()
        if(count[0] > 51):
            count[0] = 0
            baralho -= 1
        print(f'Total Cards: {count[0]} | Points: {count[1]}/{baralho}')
        dealer = int(input('Dealer upcard: '))
        count[0]+=1
        if(dealer == 99): break

        carta1 = int(input('Your card: '))
        carta2 = int(input('Your card: '))

        count[0]+=2
        count[1] += card_c(dealer,carta1,carta2)

        carta1, carta2 = subs_a(carta1,carta2)
        resp = calc(dealer, carta1, carta2)

        while(resp == 'hit'):
            carta3 = int(input('Your card: '))
            carta2+= carta3
            count[0]+=1
            count[1] += card_c(0,0,carta3)
            resp = calc(dealer,carta1,carta2)

        if(resp == 'double'):
            carta3 = int(input('Your card: '))
            count[0]+=1
            count[1] += card_c(0,0,carta3)

        if(resp == 'split'):
            carta3 = int(input('Your card: '))
            count[0]+=1
            count[1] += card_c(0,0,carta3)
            calc(dealer,carta1,carta3)
            carta3 = int(input('Your card: '))
            count[0]+=1
            count[1] += card_c(0,0,carta3)
            calc(dealer,carta1,carta3)

        option = str(input('Enter to next card...'))
        if(option == 's'):
            carta_extra = int(input('Carta Extra: '))
            while(carta_extra != 99):
                count[0]+=1
                count[1] += card_c(0,0,carta_extra)
                carta_extra = int(input('Carta Extra: '))
                

    return 0

if __name__ == "__main__":
    main()