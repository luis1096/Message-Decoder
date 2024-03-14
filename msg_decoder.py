def decode(message_file):
    #intilaize variables
    msg_dict = {}
    lst_index = []
    final_msg = []
    final_str = ''

    #open txt file and create a dictionary with key = num = value = word
    with open(message_file) as msg:
        for line in msg:
            (key, val) = line.split()
            msg_dict[int(key)] = val

    #get a list of the indexes to return from the dictionary i.e the
    #numbers at the right end of the pyramid structure
    for i in range(1, len(msg_dict)):
        i = int((i * i + i)/2)
        lst_index.append(i)

    #go through lst_index for all numbers in msg file i.e. every dictionary key
    #if you get a match add it to the final msg list
    for i in range(1, len(msg_dict)+1):
        if i in  lst_index:
            final_msg.append(msg_dict[i])

    #convery final msg list to final string 
    for i in final_msg:
        final_str = final_str + " " +  i
    
    final_str = final_str[1:]
    print(final_str)

decode(r'C:\Users\luisq\OneDrive\Desktop\test.txt')
 