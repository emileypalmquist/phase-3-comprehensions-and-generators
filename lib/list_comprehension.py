#!/usr/bin/env python3

# LIST COMPREHENSION
# new_list = [optional_operation(item) for item in old_list if optional_condition == True]

# GENERATOR EXPRESSIONS
# generator_object = (optional_operation(item) for item in old_list)
#### used for big datasets #####

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]


def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]
