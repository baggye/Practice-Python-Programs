"""This function will encrypt a message"""
def encrypt(text, n):
    message = text
    for i in range(n):
        message.split()
        even_message = []
        odd_message = []
        for x in range(len(message)):
            if x%2==0:
                even_message.append(message[x])
            else:
                odd_message.append(message[x])
        odd_message.extend(even_message)
        message = ''.join(odd_message)
    return message


"""This function will decrypt a message encoded through the previous function"""
def decrypt(encrypted_text, n):
    message = encrypted_text

    for i in range(n):
        message.split()
        even_message = []
        odd_message = []
        new_message = []
        l = len(message)
        if l ==0: #if there is no text
            message = []
        elif l%2==0: #If the text has an even number of values
            for a in range(int(l/2)):
                odd_message.append(message[a])
            for b in range(1,int(l/2)+1):
                even_message.append(message[a+b])
            for c in range(int(l/2)):
                new_message.append(even_message[c])
                new_message.append(odd_message[c])
        else: #If the text has an odd number of values
            for a in range(int(l//2)):
                odd_message.append(message[a])
            for b in range(1,int(l//2)+2):
                even_message.append(message[a+b])
            for c in range(int(l//2)):
                new_message.append(even_message[c])
                new_message.append(odd_message[c])
            new_message.append(even_message[c+1])
        message = ''.join(new_message)
                
    return message
