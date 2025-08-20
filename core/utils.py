from datetime import datetime
import random
import string


def now_slug(prefix: str = "post") -> str:
    ts = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    rand = "".join(random.choices(string.ascii_lowercase + string.digits, k=4))
    return f"{prefix}-{ts}-{rand}"