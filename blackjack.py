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
def stand():
    print(f'{bcolors.FAIL}Stand!{bcolors.ENDC}')
def double():
    print(f'{bcolors.WARNING}Double!{bcolors.ENDC}')
def split():
    print(f'{bcolors.OKBLUE}Split!{bcolors.ENDC}')

def calc(dealer, carta1, carta2):
    sum = carta1+carta2
    double = (carta1 == carta2)
    if (carta1 == 1): card_a(dealer, carta2)
    elif (double): card_d(dealer, carta1)
    elif (sum > 12 and not double): card_h(dealer,sum)
    elif (sum > 4 and sum < 9): hit()
    else: card_m(dealer, sum)

def card_m(dealer, sum):
    if (sum == 12):
        if (dealer < 7 and dealer > 3):
            stand()
        else:
            hit()
    elif (sum == 11):
        if (dealer == 1):
            hit()
        else:
            double()
    elif (sum == 10):
        if (dealer == 1 or dealer == 10):
            hit()
        else:
            double()
    else:
        if (dealer < 6 and dealer > 2):
            double()
        else:
            hit()

def card_h(dealer, sum):
    if (dealer > 6 and sum < 17):
        hit()
        return
    else:
        stand()

def card_d(dealer, carta1):
    if (carta1 == 8):
        split()
    elif (carta1 == 10):
        stand()
    elif (carta1 == 5):
        if (dealer == 10 or dealer == 1):
            hit()
        else:
            double()
    elif (carta1 == 7 or carta1 == 2 or carta1 == 3):
        if (dealer > 7 or dealer == 1):
            hit()
        else:
            split()
    elif (carta1 == 4):
        if(dealer == 5 or dealer == 6):
            split()
        else:
            hit()
    elif (carta1 == 6):
        if (dealer > 6 or dealer == 1):
            hit()
        else:
            split()
    else:
        if (dealer == 10 or dealer == 7 or dealer == 1):
            stand()
        else:
            split()

def card_a(dealer, carta2):
    if (carta2 == 1):
        split()
    elif (carta2 == 7):
        if (dealer == 2 or dealer == 7 or dealer == 8):
            stand()
        elif (dealer > 2 and dealer < 7):
            double()
        else:
            hit()       
    elif (carta2 > 7):
        stand()
    elif (dealer > 6):
        hit()
    else:
        if (dealer > 4):
            double()
        elif (carta2 == 2 or carta2 == 3):
            hit()
        elif (carta2 == 4 or carta2 == 5):
            if (dealer < 4):
                hit()
            else:
                double()
        else:
            if (dealer < 3):
                hit()
            else:
                double()

def subs_a(carta1, carta2):
    if (carta2 == 1):
        aux = carta1
        carta1 = carta2
        carta2 = aux
    return (carta1, carta2)

def main():
    while(1):
        cls()
        dealer = int(input('Dealer upcard: '))
        if(dealer == 99): break
        carta1 = int(input('Your card: '))
        carta2 = int(input('Your card: '))
        carta1, carta2 = subs_a(carta1,carta2)
        calc(dealer, carta1, carta2)
        input('Enter to next card...')
    return 0

if __name__ == "__main__":
    main()