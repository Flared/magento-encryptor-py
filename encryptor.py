def _explode_hash(hash_):
    hash_, salt, version = hash_.split(":")
    if not version:
        version = 1
    version = int(version)

def verify(password, hash_):
    return False

