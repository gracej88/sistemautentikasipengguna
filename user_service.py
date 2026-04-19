import json
from validation import validate_email, validate_password, validate_phone

FILE_NAME = "users.json"

def register_user(email, password, phone):
    if validate_email(email) != "Valid":
        return "Email tidak valid"
    
    if validate_password(password) != "Valid":
        return "Password tidak valid"
    
    if validate_phone(phone) != "Valid":
        return "Nomor telepon tidak valid"

    user = {
        "email": email,
        "password": password,
        "phone": phone
    }

    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(user)

    with open(FILE_NAME, "w") as f:
        json.dump(data, f)

    return "User registered successfully"