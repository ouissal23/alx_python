def validate_password(password):
    Symbol = ["@", "#", "$", " ", "&", "%"]
    val = True 

    if len(password) < 8:  
        return False 
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    
    if " " not in password:
        return True
    else:
        return False    
    if val:
        return val
print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))
    