from src.constants import (
    AWS_SECRET_ACCESS_KEY_ENV_KEY,
    AWS_ACCESS_KEY_ID_ENV_KEY,
    REGION_NAME
)
import os

__access_key_id = os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY)
__secret_access_key = os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY)


print("AWS_ACCESS_KEY_ID_ENV_KEY:", AWS_ACCESS_KEY_ID_ENV_KEY)
print("AWS_SECRET_ACCESS_KEY_ENV_KEY:", AWS_SECRET_ACCESS_KEY_ENV_KEY)

print("AWS Access Key ID:",
      __access_key_id if __access_key_id else "❌ NOT FOUND")

print("AWS Secret Access Key:",
      __secret_access_key[:4] + "****" if __secret_access_key else "❌ NOT FOUND")
