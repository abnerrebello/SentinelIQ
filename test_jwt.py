from backend.auth.security import create_access_token, verify_access_token

token = create_access_token(
    {
        "sub": "abner"
    }
)

print("TOKEN:")
print(token)

print()

print("DECODED:")
print(verify_access_token(token))