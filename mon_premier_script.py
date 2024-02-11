import unittest
from typing import List

#Count names with more than seven letters

class NamesCounter:
    def count_names(prenoms: List[str]) -> int:
        more_than_seven_count: int = 0
        for prenom in prenoms:
            if len(prenom) > 7:
                more_than_seven_count += 1
                print("Prenom supérieur à 7 : " + prenom)
            else:
                print("Prenom inférieur ou égal à 7 : " + prenom)
        return more_than_seven_count

class TestNamesCounter(unittest.TestCase):
    def test_names_count(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven_count = NamesCounter.count_names(prenoms=prenoms)
        self.assertEqual(more_than_seven_count, 4)

if __name__ == '__main__':
    unittest.main()
