str = raw_input("insert the string!")
word = raw_input("insert the word!")
def func(str, word):
    count_result= 0
    new_str = ""
    split_str = str.split()
    for s in split_str:
        if s == word:
            count_result+=1
#----------------------------------------------------- counts the number of word
        else:
            new_str += s + ' '

    print "Here are the results!!!!!!!"
    print "This many time word comes in string :", count_result
    print "This is how string looks without that word :", new_str
#----------------------------------------------------- will create new string by removing that word
    for i in range(count_result):
        new_str += word + " "

# #---------------------------------------------------- will append the words in string
    print "New string after appending word to it ", new_str
func(str,word)

