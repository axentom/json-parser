import json

def check_char_count(mystr):

    assert isinstance(mystr, str), 'Input to this function should be a string'

    if ( len(mystr) == 2 ):
        return( f'{mystr} count passes' )
    else:
        return( f'{mystr} count FAILS' )

def check_char_type(mystr):
    if (mystr.isalpha() and mystr.isupper()):
        return( f'{mystr} type passes' )
    else:
        return( f'{mystr} type FAILS' )

def check_char_match(mystr, mystr2):
    assert isinstance(mystr, str)
    assert isinstance(mystr2, str)

    if (mystr[0] == mystr2[0]):
        return( f'{mystr} match passes' )
    else:
        return( f'{mystr} match FAILS' )

def main():
     with open('states.json', 'r') as f:
        states = json.load(f)

     for i in range(50):
        print(check_char_count( states['states'][i]['abbreviation']))
        print(check_char_type( states['states'][i]['abbreviation']))
        print(check_char_match( states['states'][i]['abbreviation'], states['states'][i]['name']))

if __name__ == '__main__':
     main()



