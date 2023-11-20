def chat(convo):
    interrogatives = ("why", "what", "how", "where")
    if convo.startswith(interrogatives):
        return "{}?".format(convo)
    else:
        return "{}.".format(convo)

user_a = ''
user_b = ''
result = []

while True:
    user_a = input("Say Something: ")
    if user_a == '':
        print ("your turn")
        while True:
            user_b = input("My turn: ")
            if user_b == '':
                user_a += input("Say Something: ")
                result.append(chat(user_a))
                continue
                
            elif user_b == "/end":
                break
                result.append(chat(user_b))
                
            else:
                result.append(chat(user_b))
        break
    result.append(chat(user_a))
       

print(" ---> ".join(result))


