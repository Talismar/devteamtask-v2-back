from datetime import datetime


def authenticated_user_audit(email: str):
    with open("authenticated_user_audit.txt", mode="a") as file:
        authentication_date = datetime.now()
        content = f"Authentication info: Date {authentication_date} Username {email}\n"
        file.write(content)
        print("Acabou de escrever")
