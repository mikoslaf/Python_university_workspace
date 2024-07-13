import pytest

def get_trigrams(word: str) -> list[str]:
    
    word = "".join(["  ", word.strip(), " "])
    return ["".join([word[x+y] for y in range(3) if x+y < len(word)]) for x in range(len(word) - 2)]

    # word = "".join(["  ", word.strip(), " "])
    # result = []
    # for x in range(len(word) - 2):
    #     local_result = [word[x+y] for y in range(3) if x+y < len(word)]
    #     result.append("".join(local_result))
    # return result

def simple_trigram_similarity(word1: str, word2: str) -> float:
    return set(word1) & set(word2)
    

def test():
    print(get_trigrams('ab') == ['  a', ' ab', 'ab '])
    print(get_trigrams('aaa') == ['  a', ' aa', 'aaa', 'aa '])
    print(get_trigrams('abc') == ['  a', ' ab', 'abc', 'bc '])
    print(get_trigrams('abcde') == ['  a', ' ab', 'abc', 'bcd', 'cde', 'de '])
    print(get_trigrams('hello') == ['  h', ' he', 'hel', 'ell', 'llo', 'lo '])
    print(get_trigrams(' abc') == ['  a', ' ab', 'abc', 'bc '])
    print(get_trigrams('  abc') == ['  a', ' ab', 'abc', 'bc '])
    print(get_trigrams('abc    ') == ['  a', ' ab', 'abc', 'bc '])

if __name__ == '__main__':
    print(get_trigrams("abcdefghi"))
    test()
    print(simple_trigram_similarity('aabc', 'aabcd'))