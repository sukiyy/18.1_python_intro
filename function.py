def send_email(to_email, from_email, subject, body):
    email = f"""
        to: {to_email}
        from: {from_email}
        subject: {subject}
        ------------------------
        body: {body}
    """
    print(email)


send_email(body="hi,blue. how is going on?", to_email="blue@gmail.com", from_email="sookie@gmail.com",subject="meow")


def power(num, power):
    return num**power

    