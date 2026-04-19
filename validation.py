import re

def validate_email(email):
    if not email:
        return "Email tidak boleh kosong"
    
    if " " in email:
        return "Email tidak boleh mengandung spasi"
    
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if not re.match(pattern, email):
        return "Format email tidak valid"
    
    return "Valid"


def validate_password(password):
    if not password:
        return "Password tidak boleh kosong"
    
    if len(password) < 8:
        return "Password minimal 8 karakter"
    
    if " " in password:
        return "Password tidak boleh mengandung spasi"
    
    if not re.search(r'[A-Z]', password):
        return "Password harus mengandung huruf besar"
    
    if not re.search(r'[a-z]', password):
        return "Password harus mengandung huruf kecil"
    
    if not re.search(r'[0-9]', password):
        return "Password harus mengandung angka"
    
    return "Valid"


def validate_phone(phone):
    if not phone:
        return "Nomor telepon tidak boleh kosong"
    
    if not phone.isdigit():
        return "Nomor telepon hanya boleh angka"
    
    if len(phone) < 10 or len(phone) > 13:
        return "Nomor telepon harus 10-13 digit"
    
    return "Valid"