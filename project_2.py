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

# FUNCE KONTROLY - ZADANÝ STRING = POŽADOVANÝ LEN
def check_requied_str_len(control_text: str, len_num: int) -> bool:
    """
    Funkce kontroluje zdali zadaný string má požadovaný počet znaků.
    
    Ukázka:
    -------
    check_requied_str_len("Erik", 4)
    True
    check_requied_str_len("Erika", 4)
    False
    
    Funkce vrací boolean hodnotu
    """
    if len(control_text) == len_num:
        return True
    else:
        return False

# FUNKCE NA KONTOLU NE DUPLICITY VE STRINGU
def check_string_no_duplicate(control_text: str) -> bool:
    """
    Funkce kontroluje zdali je zadaný string bez duplicitních
    znaků.
    
    Ukázka:
    -------
    check_text_no_duplicate("1234")
    True
    
    Funkce vrací boolean hodnotu.
    """
    if len(control_text) == len(set("".join(control_text))):
        return True
    else:
        return False
    
# FUNKCE NA KONTROLU UNIKÁTNÍHO ČÍSLA
def check_unique_num(control_num: str, len_num: int) -> bool:
    """
    Funkce kontroluje zdali zadané číslo je unikátní.
    Zadané číslo musí mít každou číslici jinou, nesmí začínat nulou,
    a musí mít požadovanou délku.
    control_num: KONTROLOVANÉ ČÍSLO
    len_num: POŽADOVANÁ DÉLKA KONROLOVANÉHO ČÍSLA
        
    Ukázka:
    -------
    check_unique_num("1234", 4)
    return True
    
    Funkce vrací boolean hodnotu.
    """
    if (
        check_string_no_duplicate(control_num)
        and check_requied_str_len(control_num, len_num) 
        and control_num.isnumeric() 
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
    
    Ukázka:
    -------
    evaluation_bull_cow("1234", 1243)
    2 bulls, 2 cows
    """    
    bulls = 0
    for i in range(0,len(num1)):
        if num1[i] == num2[i]:
            bulls += 1 
    cows = len(set(num1).intersection(set(num2))) - bulls               
    print(
        "Your interim result:",
        (f"{bulls} bulls,") if (bulls) > 1 else (f"{bulls} bull,"),
        (f"{cows} cows") if cows > 1 else (f"{cows} cow")
    )
# FUNKCE VYPÍŠE KLÍČOVÝ TEXT
def key_text(num) -> str: 
    """
    Funkce vrátí důležitý text
    """
    text = (f"""The entered number must contain digits 
and must not start with 0, must not contain duplicates 
and must not be longer or shorter than {num}.""")
    return text 

# FUNKCE ODČÍTÁNÍ
def subtraction (num1: int or float, num2: int or float) -> int or float: 
    """
    Funce na odčítání se zaokrouhlením na dvě desetinná čísla.
    Funkce vrací výsledek
    """
    result = round(num1 - num2, 2)
    return result

# FUNKCE NA VYPSÁNÍ CHYB
def text_is_longer(tip_num: str, key_num: int):
    """
    Funkce v případě,že text (tip_num) je delší než požadovaná délka textu 
    to vypíše. Jinak neudělá nic.
    """
    if len(tip_num) > key_num:
        print(f"- your guessed number is longer than {key_num}")  
            
def text_is_shorter(tip_num: str, key_num: int):
    """
    Funkce v případě,že text (tip_num) je kratší než požadovaná délka textu 
    to vypíše. Jinak neudělá nic.
    """
    if len(tip_num) < key_num:
        print(f"- your guessed number is shorter than {key_num}")   
        
def text_has_duplicates(tip_num: str):
    """
    Funkce v případě,že v textu (tip_num) jsou duplicity
    to vypíše. Jinak neudělá nic.
    """
    if not check_string_no_duplicate(tip_num):
        print("- your guessed number must not have duplicates") 
        
def text_start_zero(tip_num: str):
    """
    Funkce v případě,že text (tip_num) začne "0" to vypíše. Jinak neudělá nic.
    """
    if tip_num.startswith("0"):
        print("- your guessed number must not start with 0") 
        
def text_no_numeric(tip_num: str):
    """
    Funkce v případě,že text (tip_num) není jen s číslicemi to vypíše. 
    Jinak neudělá nic.
    """
    if not tip_num.isnumeric():
        print("- your guessed number must be digits only")        

# FUNCE NA VYPSÁNÍ CHYBOVÉHO HLÁŠENÍ
def all_text_errors(tip_num: str, key_num: int, line: str) -> print:
    """
    Funkce s více funkcí.
    Funkce výpíše hlášení chyb u zadaného hádaného čísla 
    a vypíše důležítý text(návod).
    Funkce vyprintuje texty.
    """
    print(f"WARNING: your number > {tip_num} < is wrong!!!\n{line}")
    text_is_longer(tip_num, key_num)
    text_is_shorter(tip_num, key_num)
    text_has_duplicates(tip_num)
    text_start_zero(tip_num)
    text_no_numeric(tip_num)
    print(f"{line}\n{key_text(key_num)}")  
# FUNKCE NA VYHODNOCENÍ HER
def evaluation_games(seznam: list) -> print:
    """
    Funkce vypíše tabulku všech her ze seznamu s tuply.
    Funkce vrací print.
    """
    print(f"YOUR GAMES: {len(seznam)} \n" + ("-"*22) + 
        "\nGAME|GUESSES|TIME(s.)\n"+("-"*22))
    for i, val in enumerate (seznam, 1):
        print(
            str(i).rjust(4)
            + "|"
            + str(val[0]).center(7)
            + "|"
            + str(val[1])
            + "\n"
            + ("-" * 22)
    )   
# FUNKCE NA OZNÁMKOVÁNÍ
def grading(grade:int) -> str:  
    """
    Funkce na oznámkování výsledku hádání:
    1-5 = Excellent,6-10 = Commendable,
    11-15 = Good, 16-20 = Sufficient,
    > 20 = Insufficient
    PŘÍKLAD:
    grad = grading(10)
    print(grad)
    >> Commendable
    
    Funkce vrací ohodnocení ve stringu 
    """ 
    if grade < 6:
        grading_text = "Excellent"
    elif grade >= 6 and grade < 11:
        grading_text =  "Commendable" 
    elif grade >= 11 and grade < 16:
        grading_text =  "Good"  
    elif grade >= 16 and grade < 21:
        grading_text =  "Sufficient" 
    else:
        grading_text =  "Insufficient"  
    return grading_text             
# ČÁRA OKRAJE =================================
line = "=" * 60
# HISTORIE HER
games = []
# KLÍČOVÉ ČÍSLO (1-10) JINÉ ČÍSLO ZMĚNÍ OBTÍŽNOST
key_num = 4
# PROMĚNNÁ NA POKRAČOVÁNÍ HRY
next_game = "y"
# UVÍTÁNÍ
print(f'''
{line}
Hello, welcome to the game "Bulls and Cows"
- a game based on guessing a {key_num}-digit number.\n{line}
The program displays the number of bull(s) 
(if the user guesses both the number and its location), 
and the cow(s)
(if the user only guesses the number but not its location).\n{line}
{key_text(key_num)}\n{line}
I've generated a random {key_num} digit number for you.
Let's play a Bulls and Cows game. Good luck.\n{line}'''
)       

# SPUŠTĚNÍ HRY 
while next_game == "y":
    # ZAČÁTEK MĚŘENÍ ČASU
    start_time = time.time()
    # POKUSY
    guesses = 1    
    # GENEROVÁNÍ ČÍSLA A PŘEVEDENO NA STRING   
    gen_num = str(random_number_generator(key_num))
    game_running = True  
    print(f"\nGAME NO. {len(games)+1}\n{line}")
    # A HRA BĚŽÍ       
    while game_running:
        # TIPOVANÉ ČÍSLO
        you_tip_num = input(f"Enter a {key_num}-digit number:\n{line}\n")  
        
        if gen_num == you_tip_num:
            break
        elif check_unique_num(you_tip_num,key_num): 
            # FUNKCE A FUNKCE
            evaluation_bull_cow(gen_num, you_tip_num)
            guesses += 1            
        else:
            all_text_errors(you_tip_num, key_num, line)
            
    # KONEC MĚŘENÍ ČASU
    end_time = time.time()  
    # VYPSÁNÍ VYHODNOCENÍ HRY                   
    print(
        f'''{line}
Correct, you've guessed the right number in {guesses} guesses!
Time elapsed: {subtraction(end_time, start_time)} seconds.
That's {grading(guesses)}.'''
    )           
    # ODESLÁNÍ DO HISTORIE HER
    games.append((guesses, subtraction(end_time, start_time)))
    # DALŠÍ HRA?
    next_game = input(f"{line}\nInsert y or Y for next game, others for end game:\n{line}\n"
    ).lower()   
# VYHODNOCENÍ  VŠECH HER  
evaluation_games(games)
# NASHLE   
print(f"{line}\nThank you for using our game application. Have a nice day")    
    


