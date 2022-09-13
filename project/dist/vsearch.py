# @Time: 2022/9/11 19:44
# @Author: 李树斌
# @File : vsearch.py
# @Software :PyCharm

# def search4vowels(phrase:str) -> set:
#     """从单词中查找元音"""
#     vowels = set('aeiou')
#     return vowels.intersection(set(phrase))

def search4letters(phrase:str, letters:str='aeiou') -> set:
    """Return a set of 'letters' found in‘phrase'"""
    return set(letters).intersection(set(phrase))

