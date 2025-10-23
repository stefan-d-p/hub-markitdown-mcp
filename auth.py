import os
from fastmcp.server.auth.providers.jwt import JWTVerifier

# Default public key (fallback)
default_public_key_pem = """-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAs8mqjGdg6sJN4EoaSZlL
fqhKs8yVTCBnj/abzpFmR4tA60cAimltk4U1P8/IZYzD34HNKUadEhbk44fAt6X4
qhb7QDZe3NVJcRVRgIlbaBkpNiKGFJpRbrdoeDrXM6PF3tHOaBh0VFNTDpghhhIZ
mR4NTvBQ4KwKxcVWazS6CiKobChjrR0JVzANCBCozaJJVfjTXjXApsLoX52LnUZe
HQ//9/3PrjbtAqSs+1UM0elHV5wPVGbs9Y6WTmz7oAbvTYiQ8Gw5YP8gWYO4hMMO
E1CqDMaBm4r5NRB6i5zPRRq+IoVGqE3Eiccgv+flNtt9jmRETkefzmkurRTcV5sc
0QIDAQAB
-----END PUBLIC KEY-----"""

verifier = JWTVerifier(
    public_key=os.getenv("JWT_PUBLIC_KEY"),
    issuer=os.getenv("JWT_ISSUER"),
    audience=os.getenv("JWT_AUDIENCE")
)