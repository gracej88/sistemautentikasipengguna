from validation import validate_email, validate_password, validate_phone

print("=== VALIDASI DATA USER ===")

email = input("Masukkan email: ")
password = input("Masukkan password: ")
phone = input("Masukkan nomor telepon: ")

print("\nHasil Validasi:")
print("Email:", validate_email(email))
print("Password:", validate_password(password))
print("Nomor Telepon:", validate_phone(phone))