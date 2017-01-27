#!/usr/bin/env python

if __name__ == "__main__":

    #### Exercise 6a #####
    print "\nExercise 6a"
    print "-" * 80
    my_list = ['whatever', 99, True, 'hello', 22, 'some string', 'another']

    for entry in my_list:
        print entry
    print "-" * 80

    #### Exercise 6b #####
    print "\nExercise 6b"
    print "-" * 80
    my_list.append('whatever')

    for i, entry in enumerate(my_list):
        print i, entry
    print "-" * 80

    #### Exercise 6c #####
    print "\nExercise 6c"
    print "-" * 80
    my_list[2] = False
    my_list[-1] = 'changed'
    print my_list
    print "-" * 80

    #### Exercise 6d #####
    print "\nExercise 6d"
    print "-" * 80
    my_list.pop()
    my_list.pop(0)
    my_list.pop(2)
    print "List length: {}".format(len(my_list))
    print my_list
    print "-" * 80

    #### Exercise 6e #####
    print "\nExercise 6e"
    print "-" * 80
    new_list = [3, 2, 9]
    my_list.extend(new_list)
    print my_list
    print "-" * 80

    #### Exercise 6f #####
    print "\nExercise 6f"
    print "-" * 80
    my_list.insert(1, 'whatever')
    print my_list
    print "-" * 80

    #### Exercise 6g #####
    print "\nExercise 6g"
    print "-" * 80
    print my_list[:4]

    new_list = my_list[-5:]
    print new_list
    print "-" * 80
    print
