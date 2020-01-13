!/usr/bin/python3
"""
function that prints a text with 2 new lines after each of these
characters: ., ? and :
"""


def text_indentation(text):
    """
    Function that prints  a text with
    2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    text1 = text.replace('?', '?\n\n')
    text1 = text1.replace('.', '?\n\n')
    text1 = text1.replace(':', '?\n\n')
    print("\n".join([i.strip() for i in text1.split("\n")]), end="")
