import unittest


def remove_duplicates(in_string):
    memory = {}
    pruned_string = []
    for id, char in enumerate(in_string):
        if char not in memory:
            memory[char] = None
            pruned_string.append(char)
    pruned_string = "".join(pruned_string)
    return pruned_string

import re


def normalize_whitespace(in_string):
    in_string = in_string.strip()
    return re.sub(r"\s+", " ", in_string)


class SmileyFinder:
    def __init__(self):
        eyes, nose, mouth = r":;8X=", r"-~’^", r";:()|DP"
        escaped_patterns = map(re.escape, [eyes, nose, mouth])
        self.pattern = "[{}][{}]?[{}]".format(*escaped_patterns)
        self.mf = lambda match: {'start': match.span()[0], 'end': match.span()[1], 'match': match.group()}

    def findall(self, text):
        return list(map(self.mf, list(re.finditer(self.pattern, text))))


def find_smilyes(in_string):
    in_string = in_string.strip()
    matches = re.findall(r"[:;]{1}-?[P\)\(XD*S|Oo]]", in_string)
    match_formatter = lambda x: {'match': x.match}
    return map(match_formatter, matches)


class VowelFinder:
    def __init__(self):
        self.pattern = r"(?=(([qwrtypsdfghjklzxcvbnm])([aeiou]{2,})([qwrtypsdfghjklzxcvbnm])))"
        self.formatter = lambda x: x.group(1)[1:-1]

    def findall(self, text):
        return map(self.formatter, re.finditer(self.pattern, text, re.I))


class TestCases(unittest.TestCase):
    def test_replace_all_duplicates(self):
        self.assertEquals("ab", remove_duplicates("abbababaaaabababbab"))
        self.assertEquals("qwertzuiop", remove_duplicates("qwertzuiopwertz"))
        self.assertEquals("", remove_duplicates(""))

    def test_replace_all_whitespace(self):
        self.assertEquals("abb sac sdc b", normalize_whitespace("abb       sac sdc  b    "))
        self.assertEquals("a b c", normalize_whitespace("a\tb\tc"))
        self.assertEquals("", normalize_whitespace(""))

    def test_find_smileys(self):
        targets = [{'match': ':-)', 'start': 0, 'end': 3},
                   {'match': ':-P', 'start': 3, 'end': 6},
                   {'match': ';)', 'start': 6, 'end': 8},
                   {'match': ';-(', 'start': 8, 'end': 11}]

        smiley_finder = SmileyFinder()
        for target, match in zip(targets, smiley_finder.findall(":-):-P;);-(")):
            self.assertDictEqual(target, match)

    def test_vowels(self):
        targets = [["ee", "Ioo", "Oeo", "eeeee"],
                   ["aa", "aa", "aa"]]

        vf = VowelFinder()
        blah = list(vf.findall("rabcdeefgyYhFjkIoomnpOeorteeeeet"))
        self.assertListEqual(targets[0], list(vf.findall("rabcdeefgyYhFjkIoomnpOeorteeeeet")))
        self.assertListEqual([], list(vf.findall("")))
        self.assertListEqual(targets[1], list(vf.findall("abaabaabaabaae")))
        self.assertListEqual([], list(vf.findall("match a single character not present in the list below")))

