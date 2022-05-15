import os
import sys

def get_token_list(tokens):
    new_options = []
    if ',' in tokens:
        tokens = tokens.split(',')
    else:
        tokens = tokens.split(' ')
    for token in tokens:
        new_options.append(token.strip().lower())
    return new_options
