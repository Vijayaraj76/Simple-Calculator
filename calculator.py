import math
import os
import time
from datetime import datetime

# Color constants
COLORS = {
    'HEADER': '\033[95m',
    'BLUE': '\033[94m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'RED': '\033[91m',
    'ENDC': '\033[0m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m'
}

calculation_history = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    print(f"{COLORS['HEADER']}{COLORS['BOLD']}")
    print("╔══════════════════════════════════════════════╗")
    print("║             ADVANCED CALCULATOR              ║")
    print("╚══════════════════════════════════════════════╝")
    print(f"{COLORS['ENDC']}")

def display_menu():
    print(f"{COLORS['BLUE']}╔══════════════════ MENU ══════════════════╗")
    print("║                                            ║")
    print("║  1. Addition         (+)                  ║")
    print("║  2. Subtraction      (-)                  ║")
    print("║  3. Multiplication   (×)                  ║")
    print("║  4. Division         (÷)                  ║")
    print("║  5. Power            (^)                  ║")
    print("║  6. Square Root      (√)                  ║")
    print("║  7. View History                          ║")
    print("║  8. Exit                                  ║")
    print("║                                            ║")
    print("╚════════════════════════════════════════════╝")
    print(f"{COLORS['ENDC']}")

def display_history():
    clear_screen()
    print(f"{COLORS['YELLOW']}╔═══════════ Calculation History ════════════╗{COLORS['ENDC']}")
    if not calculation_history:
        print(f"{COLORS['RED']}No calculations performed yet.{COLORS['ENDC']}")
    else:
        for idx, calc in enumerate(calculation_history[-10:], 1):
            print(f"{COLORS['BLUE']}{idx}. {calc}{COLORS['ENDC']}")
    print(f"{COLORS['YELLOW']}╚════════════════════════════════════════════╝{COLORS['ENDC']}")
    input(f"\n{COLORS['GREEN']}Press Enter to return to main menu...{COLORS['ENDC']}")

def get_number(prompt):
    while True:
        try:
            print(f"{COLORS['YELLOW']}{prompt}{COLORS['ENDC']}", end=" ")
            return float(input())
        except ValueError:
            print(f"{COLORS['RED']}Error: Please enter a valid number.{COLORS['ENDC']}")

def format_operation(operation, num1, num2=None):
    operators = {1: '+', 2: '-', 3: '×', 4: '÷', 5: '^', 6: '√'}
    if operation == 6:
        return f"√{num1}"
    return f"{num1} {operators[operation]} {num2}"

def calculate(operation, num1, num2=None):
    try:
        if operation == 1:
            result = num1 + num2
        elif operation == 2:
            result = num1 - num2
        elif operation == 3:
            result = num1 * num2
        elif operation == 4:
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        elif operation == 5:
            result = num1 ** num2
        elif operation == 6:
            if num1 < 0:
                raise ValueError("Cannot calculate square root of a negative number")
            result = math.sqrt(num1)
        
        # Add to history
        timestamp = datetime.now().strftime("%H:%M:%S")
        history_entry = f"[{timestamp}] {format_operation(operation, num1, num2)} = {result:.2f}"
        calculation_history.append(history_entry)
        
        return result
    
    except ZeroDivisionError:
        return f"{COLORS['RED']}Error: Division by zero is not allowed{COLORS['ENDC']}"
    except ValueError as e:
        return f"{COLORS['RED']}{str(e)}{COLORS['ENDC']}"

def display_loading_animation():
    print(f"{COLORS['GREEN']}", end="")
    for _ in range(3):
        for char in "⣾⣽⣻⢿⡿⣟⣯⣷":
            print(f"\rCalculating {char}", end="", flush=True)
            time.sleep(0.1)
    print(f"{COLORS['ENDC']}")

def main():
    while True:
        clear_screen()
        display_header()
        display_menu()

        try:
            choice = int(input(f"\n{COLORS['YELLOW']}Select operation (1-8): {COLORS['ENDC']}"))
            
            if choice == 8:
                print(f"\n{COLORS['GREEN']}Thank you for using Advanced Calculator!{COLORS['ENDC']}")
                time.sleep(1.5)
                clear_screen()
                break
            
            if choice == 7:
                display_history()
                continue

            if choice < 1 or choice > 8:
                print(f"{COLORS['RED']}Error: Please select a valid operation (1-8){COLORS['ENDC']}")
                time.sleep(1.5)
                continue

            print(f"\n{COLORS['BOLD']}Enter your numbers:{COLORS['ENDC']}")
            if choice == 6:
                num1 = get_number("\nEnter number:")
                result = calculate(choice, num1)
            else:
                num1 = get_number("\nEnter first number:")
                num2 = get_number("Enter second number:")
                result = calculate(choice, num1, num2)

            display_loading_animation()
            print(f"\n{COLORS['BOLD']}Result:", end=" ")
            if isinstance(result, str):
                print(result)
            else:
                print(f"{COLORS['GREEN']}{result:.2f}{COLORS['ENDC']}")

            input(f"\n{COLORS['BLUE']}Press Enter to continue...{COLORS['ENDC']}")

        except ValueError:
            print(f"{COLORS['RED']}Error: Please enter a valid choice{COLORS['ENDC']}")
            time.sleep(1.5)

if __name__ == "__main__":
    main() 