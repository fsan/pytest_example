def hashed_password(password):
	import hashlib
	return hashlib.md5(password.encode('utf-8')).hexdigest()


def authenticate(user, password):
    users = {       "root": hashed_password("root"),
                    "admin": hashed_password("admin"),
                    "user": hashed_password("zer0c00l")
                    }
    if user in users.keys():
        if hashed_password(password) == users[user]:
            return True
    return False
