import time

from jose import jwk, jwt

pem = "devteamtask.2023-11-27.private-key.pem"

app_id = "384729"

# Open PEM
with open(pem, "rb") as pem_file:
    signing_key = jwk.construct(pem_file.read(), algorithm="RS256")

payload = {
    # Issued at time
    "iat": int(time.time()),
    # JWT expiration time (10 minutes maximum)
    "exp": int(time.time()) + 600,
    # GitHub App's identifier
    "iss": app_id,
}

# Create JWT
encoded_jwt = jwt.encode(payload, signing_key, algorithm="RS256")

print(f"JWT:  {encoded_jwt}")
