"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Erik Stojaspal

email: erast@seznam.cz

discord: erastxxi
"""

from random import randint

import time


# FUNKCE NA GENEROVÁNÍ UNIKÁTNÍHO ČÍSLA 1 - 10:


def random_number_generator(number_count: int) -> int:
    """
    Popis:
    ------
    Tato funkce vygeneruje 1 až 10-místné číslo,
    kde každé číslo je unikátní a nebude začínat 0.
    v případě nezadání argumentu číslo 1-10,
    funkce nahlási chybu a bude ukočena, 
    jinak by nastala nekonečná smyčka nebo chyba.
    Funkce vrací integer.

    Ukázka:
    -------
    random_number_generator(5)
    Funkce vrátí hodnotu : například - 12340
    """    
    if not number_count in (range(1,11)):
        print("NOTE: Number 1-10 must be entered. The function is terminated.")
        quit()
    gen_numbers = ""
    while len(gen_numbers) < number_count:
        number = str(randint(0,9))
        if (
            number == "0" 
            and len(gen_numbers) == 0 
            or number in gen_numbers
            ):
            continue
        else:
            gen_numbers += number
    return int(gen_numbers)


# FUNKCE NA KONTROLU UNIKÁTNÍHO ČÍSLA:


def check_unique_num(control_num: str, len_num: int) -> bool:
    """
    Funkce kontroluje zdali zadané číslo je unikátní.
    Zadané číslo musí mít každou číslici jinou, nesmí začínat nulou,
    a musí mít požadovanou délku.
    control_num: KONTROLOVANÉ ČÍSLO
    len_num: POŽADOVANÁ DÉLKA KONROLOVANÉHO ČÍSLA
    
    PŘÍKLAD:
    check_unique_num("1234", 4)
    return True
    
    Funkce vrací boolean hodnotu.
    """
    if (
        len(control_num) == len(set("".join(control_num)))
        and len(control_num) == len_num and control_num.isnumeric() 
        and not control_num.startswith("0")
        ): 
        return True
    else:
        return False
    
    
# FUNKCE NA VYPSÁNÍ VYHODNOCENÍ BULLS AND COWS:


def evaluation_bull_cow(num1, num2: str) -> print:
    """
    Funkce vyhodnotí a výpíše srovnání
    dvou unikátních čísel převedené do stringu.
    bulls: jsou stejná čísla na svých pozicích
    cows: jsou stejná čísla na jiných pozicích
    
    PŘÍKLAD:
    evaluation_bull_cow("1234", 1243)
    2 bulls, 2 cows
    """    
    bulls = 0
    for i in range(0,len(num1)):
        if num1[i] == num2[i]:
            bulls += 1 
    cows = len(set(num1).intersection(set(num2))) - bulls               
    print(
        (f"{bulls} bulls,") if (bulls) > 1 else (f"{bulls} bull,"),
        (f"{cows} cows") if cows > 1 else (f"{cows} cow"),
    )
    

# ČÁRA OKRAJE =================================

line = "=" * 55

# HISTORIE HER

games = []

# UVÍTÁNÍ

print(f"{line}\nHi there!")

# KLÍČOVÉ ČÍSLO (1-10) JINÉ ČÍSLO ZMĚNÍ OBTÍŽNOST

key_num = 4

# PROMĚNNÁ NA POKRAČOVÁNÍ HRY

next_game = "y"

# SPUŠTĚNÍ HRY 

while next_game == "y":
    
    # ZAČÁTEK MĚŘENÍ ČASU
    
    start_time = time.time()
    
    # POKUSY
    
    attempts = 1
    
    print(
        f'''{line}
I've generated a random {key_num} digit number for you.
Let's play a bulls and cows game.\n{line}'''
)
    
    # GENEROVÁNÍ ČÍSLA A PŘEVEDENO NA STRING   
    
    gen_num = str(random_number_generator(key_num))

    # TIPOVANÉ ČÍSLO
    
    you_tip_num = ""
        
    game_running = True
    
    # A HRA BĚŽÍ
    
    while game_running:
        if gen_num == you_tip_num:
            print(
                f"{line}\nCorrect, you've guessed the right number in {key_num} guesses!"
            )
            break
        elif check_unique_num(you_tip_num,key_num): 
            # FUNKCE A FUNKCE
            evaluation_bull_cow(gen_num, you_tip_num)
            attempts += 1
            you_tip_num = input(
                f"attempts: {attempts}. Enter a {key_num}-digit number:\n{line}\n"
            )
        else:
            you_tip_num = input(
                f"attempts: {attempts}. Enter a {key_num}-digit number:\n{line}\n"
            )

    # KONEC MĚŘENÍ ČASU
    
    end_time = time.time()
    
    # VYPSÁNÍ VYHODNOCENÍ HRY
    
    elapsed_time = end_time - start_time
    print(f"Attempts: {attempts}\nTime elapsed: {round(elapsed_time, 2)} seconds.")
    
    #  ODESLÁNÍ DO HISTORIE HER
    
    games.append((attempts, round(elapsed_time, 2)))
    
    # DALŠÍ HRA?
    
    next_game = input(f"{line}\ninsert y or Y (yes) for next game:\n{line}\n").lower()
        
# VYHODNOCENÍ  VŠECH HER  

print("YOURS GAMES:\n" + ("-"*22) + "\nGAME|ATTEMPTS|TIME(s.)\n"+("-"*22))

for i, val in enumerate (games, 1):
    print(
        str(i).rjust(4)
        + "|"
        + str(val[0]).center(8)
        + "|"
        + str(val[1])
        + "\n"
        + ("-" * 22)
    )
    
print(f"{line}\nThank you for using our game application.")    
    


