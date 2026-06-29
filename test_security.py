from backend.auth.security import hash_password, verify_password

password = "SentinelIQ123"

hashed = hash_password(password)

print("Original:", password)
print("Hash:", hashed)

print("Correct Password:", verify_password(password, hashed))
print("Wrong Password:", verify_password("WrongPassword", hashed))