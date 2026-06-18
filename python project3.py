import random
import string

def generate_password():
    # ---------------------------------------------------------
    # PHASE 1: INPUT & VALIDATION
    # ---------------------------------------------------------
    print("=== DecodeLabs Enterprise Password Generator ===")
    
    try:
        length = int(input("Enter the desired password length: "))
        if length < 8:
            print("\n[!] Security Warning: Passwords shorter than 8 characters are vulnerable.")
            print("Defaulting to a secure length of 12 characters.\n")
            length = 12
            
    except ValueError:
        print("\n[!] Invalid input! Please enter a valid number.")
        print("Defaulting to a secure length of 12 characters.\n")
        length = 12

    # ---------------------------------------------------------
    # PHASE 2: PROCESS (Core Logic)
    # ---------------------------------------------------------
    letters = string.ascii_letters
    digits = string.digits         
    symbols = string.punctuation    
    
    all_characters = letters + digits + symbols
    
    password_list = random.choices(all_characters, k=length)
    secure_password = "".join(password_list)

    # ---------------------------------------------------------
    # PHASE 3: OUTPUT
    # ---------------------------------------------------------
    print("------------------------------------------------")
    print(f"Generated Password : {secure_password}")
    print(f"Password Length    : {length} characters")
    print("------------------------------------------------")

# Simply call the function directly to execute it
generate_password()
