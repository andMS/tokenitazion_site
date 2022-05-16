import os
import time

FOLDER = os.path.join(os.path.dirname(__file__), '../..')

def search_token(tokens):
    search_dict = {'found': {}, 'not_found': {} }
    posting_file = os.path.join(FOLDER,'resources/generated/posting_file.txt')
    dictionary_path = os.path.join(FOLDER, 'resources/generated/token_dictionary.txt')
    docs_id_path = os.path.join(FOLDER,'resources/generated/documents_id.txt')
    posting_lines, dictionary_id, posting_weights, document_id = generate_files_dict(posting_file, dictionary_path, docs_id_path)

    for token in tokens:
        key, results = generate_ocurrences_dict(token, posting_lines, dictionary_id, posting_weights, document_id)
        search_dict[key].update(results)

    return search_dict


def generate_ocurrences_dict(token, posting_lines, dictionary_id, posting_weights, document_id):
    key = ''
    ocurrences = {}
    try:
        positions = dictionary_id[token]
        ocurrences[token] = []
        key = 'found'
        occs = posting_lines[int(positions[1]):int(positions[0]) + int(positions[1])]
        weights = posting_weights[int(positions[1]):int(positions[0]) + int(positions[1])]
        ocurrences_dict = {occs[x]:weights[x] for x in range(0,len(occs))}
        sorted_occ = sorted(ocurrences_dict.items(), key=lambda x:x[1], reverse=True)
        for char in range(0, len(sorted_occ)):
            ocurrences[token].append([document_id[sorted_occ[char][0]], sorted_occ[char][1]])
    except KeyError:
        ocurrences = {token: 'NA'}
        key = 'not_found'

    return key, ocurrences



def generate_files_dict(posting, dictionary, docs_id):
    # Generate posting_dict
    posting_lines = []
    posting_weights = []
    with open(posting, 'r', encoding='utf-8') as posting_obj:
        lines = posting_obj.readlines()
        for line in lines:
            posting_lines.append(line.split('|')[0].strip())
            posting_weights.append(line.split('|')[1].strip())
    # Generate dictionary dict
    dictionary_id = {}
    with open(dictionary, 'r', encoding='utf-8') as dictionary_obj:
        lines = dictionary_obj.readlines()
        for line in lines:
            elements = line.split()
            dictionary_id[elements[0]] = [elements[1], elements[2]]

    document_id = {}
    with open(docs_id, 'r', encoding='utf-8') as document_obj:
        lines = document_obj.readlines()
        for line in lines:
            elements = line.split()
            document_id[elements[0]] = elements[1]
    return posting_lines, dictionary_id, posting_weights, document_id


