import db


def get_sellers():
    sellers = db.select_all("""select * from "user" u where email like 'supplier%'""")
    return sellers


def get_user_by_email(email: str):
    users = db.select_all(f"""select * from "user" u where email = '{email}'""")
    return users


def get_password(email):
    password = db.select_all(f"""select password from "user" u join user_credentials uc on u.id = uc.user_id where u.email = '{email}'""")
    return password
