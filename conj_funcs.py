import keys as ks
import read_web as rw

"""
Functions to handle raw input from Spanish conjugations 
on https://wordreference.com
"""


class NoResultset(Exception):
    "Raised when the query returns no resultset"
    pass


def parse_conj(text: str, keys, new_keys):
    """Parse a text to cut out given key strings to create a
    dictionary with (new) keys
    """
    output = {}
    i, start, end = 0, 0, 0
    count = len(keys) - 1

    while i < count:
        start = text.find(keys[i], end) + len(keys[i])
        end = text.find(keys[i + 1], start)
        output[new_keys[i]] = text[start:end].strip()
        i += 1

    start = text.find(keys[i], end) + len(keys[i])

    output[new_keys[i]] = text[start:].strip()
    return output


# def handle_tiempo(tiempo: tuple):
#     return f"{tiempo[1]} {tiempo[0]}"


def get_conju_dicts(verb):
    """sumary_line
    argument -- string - a Spanish verb
    Return: dictionary of dictionaries of tenses of conjugation of a given Spanish verb
    """
    conj_resultset = rw.read_conj(verb)
    if not conj_resultset:
        raise NoResultset
    text = ""
    for ele in conj_resultset:
        text += ele.text
    keys_tiempos = [ele[2] for ele in ks.tiempos]
    # new_keys = [(ele[0], ele[1]) for ele in ks.tiempos] #check!!!
    new_keys = [f"{ele[1].replace(' ', '_')}_{ele[0]}" for ele in ks.tiempos]
    dict_content = parse_conj(text, keys_tiempos, new_keys)

    for ele in dict_content:
        # if not ele[0] == ks.IMPERATIVO:
        if not ks.IMPERATIVO in ele:
            dict_content[ele] = parse_conj(
                dict_content[ele], ks.pronouns, ks.pronouns_short
            )
        else:
            dict_content[ele] = parse_conj(
                dict_content[ele], ks.pronouns_imperativo, ks.pronouns_imperativo_short
            )
    return dict_content


def prettify_dict(conju_dict: dict, padding=16, no_vos=True):
    """
    To convert a dictionary with conjugation
    into a table-looking string. Omitting the 'vos' line by default
    """
    output = ""

    if no_vos:
        for ele in conju_dict:
            if not ele in ("vos", "(vos)"):
                output += f"{ele.ljust(padding)}{conju_dict[ele]}\n"
    else:
        for ele in conju_dict:
            output += f"{ele.ljust(padding)}{conju_dict[ele]}\n"

    return output

def table_impersonal(d: dict, padding=16):
    output = "<pre>"
    for ele in d:
        output += f"{ele.ljust(padding)}{d[ele]}\n"
    output += "</pre>"
    return output


def get_conj(conju_dict, verb, tiempo="presente_indicativo"):
    """
    Builds a string to represent a conjugation table of a given verb
    for a given tense
    Keyword arguments:
    argument --
    Return: return_description
    """

    output = f"<b>{verb}</b>: {tiempo.replace('_', ' ')}\n<pre>{prettify_dict(conju_dict[tiempo])}</pre>"
    # print(output)
    return output
