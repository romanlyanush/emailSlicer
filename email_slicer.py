# get user email address
email = input("What is your email address?: ").strip()

# slice out user name
user = email[:email.index("@"):1]

# slice out domain name
domain = email[email.index("@")+1::1]


# format the message
output = "Wow, you're super-awesome-user name is {} and your domain name is {}".format(user, domain)

# display output message
print(output)


