#!/usr/bin/env python3

def return_evens(int_list):
    # Use list comprehension to return even numbers from int_list
    return [num for num in int_list if num % 2 == 0]
pass

def make_exclamation(sentences):
    # Use list comprehension to add '!' at the end of each sentence in the list
    return [sentence + '!' for sentence in sentences]
pass