import re


def is_success_response(response):
    return response and 200 <= response.status_code < 300

def str_replace(from_texts, to_text, text, caseinsentive):
    from_texts = from_texts if isinstance(from_texts, list) else [from_texts]
    for from_text in from_texts:
        text = (
            text.replace(from_text, to_text)
            if caseinsentive
            else re.sub(re.escape(from_text), to_text, text, flags=re.IGNORECASE)
        )
    return text


def map_replace(text, map, caseinsentive=False):
    for key, val in map.items():
        text = str_replace(val, key, text, caseinsentive)
    return text
