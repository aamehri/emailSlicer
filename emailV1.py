email = input("Enter your email: ")
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
print("User name: ", username)
print("domain: ", domain_name)