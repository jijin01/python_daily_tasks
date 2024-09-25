def is_valid_email(email):
    if len(email) > 254:
        return "Invalid mail. The mail is too long"
    if email[0] == ".":
        return "Invalid mail.The mail can't start with a dot"
    if email.count("@") != 1:
        return "Invalid email: Email must contain exactly one '@' symbol."

    local_part, domain_part = email.split("@")

    if not local_part or not domain_part:
        return "Invalid email: Local part or domain part cannot be empty."
    if ".." in email:
        return "Invalid email: Email cannot contain consecutive dots."

    if "." not in domain_part:
        return "Invalid email: Domain part must contain at least one dot."

    if domain_part[0] == "." or domain_part[-1] == ".":
        return "Invalid email: Domain part cannot start or end with a dot."
    else:
        return "Valid email."


email_id = input("Enter an email address: ")
result = is_valid_email(email_id)
print(result)
