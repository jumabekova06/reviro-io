from collections import Counter
from statistics import mean
import re
from .models import *
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        rest=[]
        for i in range(10):
            async with session.get('https://api.kanye.rest/') as response:
                html = await response.json()
                rest.append(html['quote'])
        return rest

def total_letters(quote: str) -> int:
    """It`s function get quote and count total letters in string"""
    result = [letter.isalpha() for letter in quote].count(True)
    return result


def total_vowel_and_consonant_letters(quote: str) -> dict:
    """It`s function get quote and count total vowel and consonant letters in string"""
    VOWEL_EXAMPLE = 'aeiou'
    CONSONANT_EXAMPLE = 'bcdfghjklmnpqrstvwxyz'
    vowel_count = [letter in CONSONANT_EXAMPLE for letter in quote].count(True)
    consonant_count = [consonant in VOWEL_EXAMPLE for consonant in quote].count(True)
    result = {
        'vowels_count': vowel_count,
        'consonant_count': consonant_count
    }
    return result


def total_similar_letter(quote: str) -> dict:
    """It`s function get quote and count total similar letter in string"""
    result = Counter(quote)
    return dict(result)


def average_word_len(quote: str) -> int:
    """It`s function get quote and count average word length in string"""
    clean_quote = re.sub('[^a-zA-Z0-9 \n\.]', '', quote)
    words_list = clean_quote.split()
    result = mean([len(word) for word in words_list])
    return result


def get_top_length_word(quote: str) -> dict:
    """It`s function get quote and return top three words by length"""
    clean_quote = re.sub('[^a-zA-Z0-9 \n\.]', '', quote)
    words_list = clean_quote.split()
    result = enumerate(sorted(words_list, key=len)[::-1][:3], start=1)
    return dict(result)
