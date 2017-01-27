#!/usr/bin/env python

if __name__ == "__main__":
    banner = '-' * 80

    #### Exercise 5a #####
    print "\nExercise 5a"
    print banner
    my_user = {
        'name': 'Jane Coder',
        'phone': '555-111-2222',
        'address': '1 Whatever Lane',
    }
    print my_user['name']
    print my_user['phone']
    print my_user.get('address')
    print banner

    #### Exercise 5b #####
    print "\nExercise 5b"
    print banner
    try:
        print my_user['city']
    except KeyError:
        my_user['city'] = 'San Francisco'
        print my_user['city']
    print banner

    #### Exercise 5c #####
    print "\nExercise 5c"
    print banner
    city = my_user.pop('city')
    print city
    print my_user
    if not my_user.get('city'):
        my_user['city'] = 'Denver'
        print my_user.get('city')
    print banner

    #### Exercise 5d #####
    print "\nExercise 5d"
    print banner
    city = my_user.pop('city')
    print city
    print my_user
    print my_user.setdefault('city', 'Los Angeles')
    print my_user
    print banner

    #### Exercise 5e #####
    print "\nExercise 5e"
    print banner
    print "Using format with a dictionary"
    print "{name:15} {phone:15} {address:30} {city:30}".format(**my_user)
    print banner

    #### Exercise 5f #####
    print "\nExercise 5f"
    print banner
    print "Print out just the keys"
    for k in my_user:
        print k
    print banner

    #### Exercise 5g #####
    print "\nExercise 5g"
    print banner
    print "Print out the key, value pairs"
    for k, v in my_user.items():
        print k, v
    print banner
    print
