#!/usr/bin/env python

if __name__ == "__main__":
    banner = '-' * 80

    #### Exercise 1a #####
    print "\nExercise 1a"
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

    #### Exercise 1b #####
    print "\nExercise 1b"
    print banner
    try:
        print my_user['city']
    except KeyError:
        my_user['city'] = 'San Francisco'
        print my_user['city']
    print banner

    #### Exercise 1c #####
    print "\nExercise 1c"
    print banner
    city = my_user.pop('city')
    print city
    print my_user
    if not my_user.get('city'):
        my_user['city'] = 'Denver'
        print my_user.get('city')
    print banner

    #### Exercise 1d #####
    print "\nExercise 1d"
    print banner
    city = my_user.pop('city')
    print city
    print my_user
    print my_user.setdefault('city', 'Los Angeles')
    print my_user
    print banner

    #### Exercise 1e #####
    print "\nExercise 1e"
    print banner
    print "Using format with a dictionary"
    print "{name:15} {phone:15} {address:30} {city:30}".format(**my_user)
    print banner

    #### Exercise 1f #####
    print "\nExercise 1f"
    print banner
    print "Print out just the keys"
    for k in my_user:
        print k
    print banner

    #### Exercise 1g #####
    print "\nExercise 1g"
    print banner
    print "Print out the key, value pairs"
    for k, v in my_user.items():
        print k, v
    print banner
    print
