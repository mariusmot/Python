import secrets
import string

alphabet = string.ascii_letters + string.digits + string.punctuation
password = "".join(secrets.choice(alphabet)
for i in range(10))

print(password)