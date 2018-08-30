import unittest


def encode(input):
    if not input: return ""
    prev = input[0]
    count = 0
    output = []
    for c in input:
        if c != prev:
            output += [str(count), prev]
            prev = c
            count = 1
        else:
            count += 1
    output += [str(count), prev]
    return "".join(output)

class Tester(unittest.TestCase):
    def tests(self):
        self.assertEquals("3A4B1N1A", encode("AAABBBBNA"))
        self.assertEquals("1A2B3C4D", encode("ABBCCCDDDD"))
        self.assertEquals("1A1B1C1D", encode("ABCD"))