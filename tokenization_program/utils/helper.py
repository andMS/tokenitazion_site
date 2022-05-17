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


def get_urls(found_tokens):
    tokens_url = {}
    for key, value in found_tokens.items():
        tokens_url[key] = []
        for values in value:
            url = f'/templates/{values[0].replace(".html", "")}/'
            tokens_url[key].append([url, values[0], values[1]])
    return tokens_url
