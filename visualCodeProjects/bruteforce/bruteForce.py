from datetime import datetime
lst=['a','a','a','a','a','a']
def p(lst):
    while(not lst==['z','z','z','z','z','z']):
        for i in range(len(lst)-1,0,-1):
            if(not lst[i]=='z'):
                num_letter = ord(lst[i])+1
                lst[i] = chr(num_letter)
                break
            else:
                num_letter = ord(lst[i])+1-26
                lst[i] = chr(num_letter)
        print(lst)



def main(lst):
    start_time = datetime.now()
    print(lst)
    p(lst)
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
main(lst)