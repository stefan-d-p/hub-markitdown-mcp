import os
from fastmcp.server.auth.providers.jwt import JWTVerifier

verifier = JWTVerifier(
    public_key=os.getenv("JWT_PUBLIC_KEY"),
    issuer=os.getenv("JWT_ISSUER"),
    audience=os.getenv("JWT_AUDIENCE")
)