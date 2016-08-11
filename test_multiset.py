import unittest
import multiset as m


class TestMultiSet(unittest.TestCase):  # repr is not done it's dun now

    def test_contains(self):
        a = m.MultiSet(1, 2, 3, 4, 5)
        contains = 2 in a
        self.assertEqual(contains, True, "2 is in multiset.")

    def test_not_contain(self):
        a = m.MultiSet(1, 2, 3, 4, 5)
        contains = 56 in a
        self.assertEqual(contains, False, "56 is not in multiset.")

    def test_contain_empty_set(self):
        a = m.MultiSet()
        contains = 56 in a
        self.assertEqual(contains, False, "56 is not in empty multiset.")

    def test_count_one_occurence(self):
        a = m.MultiSet(1, 2, 3, 4, 5)
        number = a.count(3)
        self.assertEqual(number, 1, "1 occurence of 3.")

    def test_count_multiple_occurences(self):
        a = m.MultiSet(1, 2, 3, 3, 4, 5)
        number = a.count(3)
        self.assertEqual(number, 2, "2 occurences of 3.")

    def test_count_no_occurence(self):
        a = m.MultiSet(1, 2, 3, 4, 5)
        number = a.count(67)
        self.assertEqual(number, 0, "There is no 67.")

    def test_count_empty_set(self):
        a = m.MultiSet()
        number = a.count(67)
        self.assertEqual(number, 0, "67 is not in empty multiset.")

    def test_insert_standard(self):
        a = m.MultiSet(1, 2, 3, 4, 5)
        a.insert(6)
        b = m.MultiSet(1, 2, 3, 4, 5, 6)
        self.assertEqual(a, b, "Sets are identical.")

    def test_insert_same_element(self):
        a = m.MultiSet(1, 2, 3, 4, 5)
        a.insert(5)
        b = m.MultiSet(1, 2, 3, 4, 5, 5)
        self.assertEqual(a, b, "Sets are identical.")

    def test_insert_empty_set(self):
        a = m.MultiSet()
        a.insert(5)
        b = m.MultiSet(5)
        self.assertEqual(a, b, "Sets are identical.")

    def test_remove_standard(self):
        a = m.MultiSet(1, 2, 3, 4, 5)
        a.remove(3)
        b = m.MultiSet(1, 2, 4, 5)
        self.assertEqual(a, b, "Sets are identical with 3 removed.")

    def test_remove_from_multiple(self):
        a = m.MultiSet(1, 2, 3, 4, 4, 5)
        a.remove(4)
        b = m.MultiSet(1, 2, 3, 4, 5)
        self.assertEqual(a, b, "Sets are identical with 4 removed.")

    def test_remove_from_single(self):
        a = m.MultiSet(1)
        a.remove(1)
        b = m.MultiSet()
        self.assertEqual(a, b, "Sets are both empty.")

    def test_remove_empty_multiset(self):
        a = m.MultiSet()
        a.remove(5)
        b = m.MultiSet()
        self.assertEqual(a, b, "Sets are both empty.")

    def test_clear_standard(self):
        a = m.MultiSet(1, 2, 3, 4, 5)
        a.clear()
        b = m.MultiSet()
        self.assertEqual(a, b, "Sets both empty.")

    def test_clear_empty_multiset(self):
        a = m.MultiSet()
        a.clear()
        b = m.MultiSet()
        self.assertEqual(a, b, "Sets both empty.")

    def test_clear_multiple_occurrences(self):
        a = m.MultiSet(2, 2, 3, 4, 5, 4, 4)
        a.clear()
        b = m.MultiSet()
        self.assertEqual(a, b, "Sets both empty.")

    def test_len_standard(self):
        a = m.MultiSet(1, 2, 3, 4, 5)
        b = len(a)
        self.assertEqual(b, 5, "Length should be 5.")

    def test_len_multiple_occurrences(self):
        a = m.MultiSet(1, 2, 3, 3, 3, 5, 1)
        b = len(a)
        self.assertEqual(b, 7, "Length should be 7.")

    def test_len_empty_multiset(self):
        a = m.MultiSet()
        b = len(a)
        self.assertEqual(b, 0, "Length should be 0.")

    def test_equals_standard(self):
        a = m.MultiSet(1, 2, 3, 4)
        b = m.MultiSet(4, 3, 2, 1)
        c = (a == b)
        self.assertEqual(c, True, "Multisets should be identical.")

    def test_not_equals_standard(self):
        a = m.MultiSet(1, 2, 3, 4, 6)
        b = m.MultiSet(4, 3, 2, 1, 5)
        c = (a == b)
        self.assertEqual(c, False, "Multisets should not be identical.")

    def test_equals_multiple_occurrences(self):
        a = m.MultiSet(1, 2, 3, 4, 4, 2)
        b = m.MultiSet(4, 3, 2, 1, 4, 2)
        c = (a == b)
        self.assertEqual(c, True, "Multisets should be identical.")

    def test_not_equals_multiple_occurrences(self):
        a = m.MultiSet(1, 2, 3, 4, 4)
        b = m.MultiSet(4, 3, 2, 1, 2)
        c = (a == b)
        self.assertEqual(c, False, "Multisets should not be identical.")

    def test_not_equals_different_lengths(self):
        a = m.MultiSet(1, 2, 3, 4)
        b = m.MultiSet(4, 3, 2, 1, 2)
        c = (a == b)
        self.assertEqual(c, False, "Multisets should not be identical.")

    def test_Le_standard(self):
        a = m.MultiSet(1, 2, 3, 4)
        b = m.MultiSet(4, 3, 2, 1, 5, 6, 7)
        c = (a <= b)
        self.assertEqual(c, True, "a is a subset of b.")

    def test_not_Le_standard(self):
        a = m.MultiSet(1, 2, 3, 4)
        b = m.MultiSet(4, 2, 1, 5, 6, 7)
        c = (a <= b)
        self.assertEqual(c, False, "a not is a subset of b.")

    def test_Le_multiple_instances(self):
        a = m.MultiSet(1, 4, 4, 4)
        b = m.MultiSet(4, 3, 4, 4, 1, 6, 7)
        c = (a <= b)
        self.assertEqual(c, True, "a is a subset of b.")

    def test_not_Le_different_length(self):
        a = m.MultiSet(1, 2, 3, 4)
        b = m.MultiSet(4, 3)
        c = (a <= b)
        self.assertEqual(c, False, "a is not a subset of b.")

    def test_Le_empty_multiset(self):
        a = m.MultiSet()
        b = m.MultiSet(4, 3, 2, 1, 5, 6, 7)
        c = (a <= b)
        self.assertEqual(c, True, "a is a subset of b.")

    def test_subtract_standard(self):
        a = m.MultiSet(1, 2, 3, 4, 5, 6, 7)
        b = m.MultiSet(4, 3, 2, 1, 9, 9, 9)
        c = (a - b)
        expected = m.MultiSet(5, 6, 7)
        self.assertEqual(c, expected, "5, 6, and 7 are not in multiset b.")

    def test_subtract_multiple_occurrences(self):
        a = m.MultiSet(1, 2, 3, 4, 5, 5, 5)
        b = m.MultiSet(4, 1, 5, 6, 9)
        c = (a - b)
        expected = m.MultiSet(5, 2, 3, 5)
        self.assertEqual(c, expected, "5 and 5 are not in multiset b.")

    def test_subtract_shorter_s1(self):
        a = m.MultiSet(1, 2, 3, 4)
        b = m.MultiSet(4, 3, 2, 1, 9, 9, 9)
        c = (a - b)
        expected = m.MultiSet()
        self.assertEqual(c, expected, "Difference should be empty.")

    def test_subtract_empty_set1(self):
        a = m.MultiSet()
        b = m.MultiSet(4, 3, 2, 1, 9, 9, 9)
        c = (a - b)
        expected = m.MultiSet()
        self.assertEqual(c, expected, "Difference should be empty.")

    def test_subtract_empty_set2(self):
        a = m.MultiSet(1, 2, 3, 4)
        b = m.MultiSet()
        c = (a - b)
        expected = m.MultiSet(1, 2, 3, 4)
        self.assertEqual(c, expected, "First set should be returned.")

    def test_Esubtract_standard(self):
        a = m.MultiSet(1, 2, 3, 4, 5, 6, 7)
        b = m.MultiSet(4, 3, 2, 1, 9, 9, 9)
        a.__isub__(b)
        expected = m.MultiSet(5, 6, 7)
        self.assertEqual(a, expected, "5, 6, and 7 are not in multiset b.")

    def test_Esubtract_multiple_occurrences(self):
        a = m.MultiSet(1, 2, 3, 4, 5, 5, 5)
        b = m.MultiSet(4, 1, 5, 6, 9)
        a.__isub__(b)
        expected = m.MultiSet(5, 2, 3, 5)
        self.assertEqual(a, expected, "5 and 5 are not in multiset b.")

    def test_Esubtract_shorter_s1(self):
        a = m.MultiSet(1, 2, 3, 4)
        b = m.MultiSet(4, 3, 2, 1, 9, 9, 9)
        a.__isub__(b)
        expected = m.MultiSet()
        self.assertEqual(a, expected, "Difference should be empty.")

    def test_Esubtract_empty_set1(self):
        a = m.MultiSet()
        b = m.MultiSet(4, 3, 2, 1, 9, 9, 9)
        a.__isub__(b)
        expected = m.MultiSet()
        self.assertEqual(a, expected, "Difference should be empty.")

    def test_Esubtract_empty_set2(self):
        a = m.MultiSet(1, 2, 3, 4)
        b = m.MultiSet()
        a.__isub__(b)
        expected = m.MultiSet(1, 2, 3, 4)
        self.assertEqual(a, expected, "First set should be returned.")

    def test_add_standard(self):
        a = m.MultiSet(1, 2)
        b = m.MultiSet(3, 4)
        c = a + b
        expected = m.MultiSet(1, 2, 3, 4)
        self.assertEqual(c, expected, "Sets are to be joined.")

    def test_add_one_empty(self):
        a = m.MultiSet(1, 2)
        b = m.MultiSet()
        c = a + b
        expected = m.MultiSet(1, 2)
        self.assertEqual(c, expected, "Second set is empty.")

    def test_add_both_empty(self):
        a = m.MultiSet()
        b = m.MultiSet()
        c = a + b
        expected = m.MultiSet()
        self.assertEqual(c, expected, "Both sets are empty.")

    def test_add_repeated_elements(self):
        a = m.MultiSet(1, 2, 2)
        b = m.MultiSet(2, 3, 4)
        c = a + b
        expected = m.MultiSet(1, 2, 2, 2, 3, 4)
        self.assertEqual(c, expected, "Some elements are repeated.")

    def test_add_different_lengths(self):
        a = m.MultiSet(1)
        b = m.MultiSet(2, 3, 4)
        c = a + b
        expected = m.MultiSet(1, 2, 3, 4)
        self.assertEqual(c, expected, "Sets are to be joined.")

    def test_repr_standard(self):
        a = m.MultiSet(1, 2, 3, 4)
        b = a.__repr__()
        expected = "MultiSet([1, 2, 3, 4])"
        self.assertEqual(b, expected, "String represention is wrong.")

    def test_repr_empty(self):
        a = m.MultiSet()
        b = a.__repr__()
        expected = "MultiSet([])"
        self.assertEqual(b, expected, "Set is empty.")

    def test_repr_repeated_elements(self):
        a = m.MultiSet(1, 2, 2, 3, 4)
        b = a.__repr__()
        expected = "MultiSet([1, 2, 2, 3, 4])"
        self.assertEqual(b, expected, "String represention is wrong.")

    def test_Eadd_standard(self):
        a = m.MultiSet(1, 2, 3, 4)
        b = m.MultiSet(5, 6, 7, 8)
        a.__iadd__(b)
        expected = m.MultiSet(1, 2, 3, 4, 5, 6, 7, 8)
        self.assertEqual(a, expected, "a should be updated with set b.")

    def test_Eadd_multiple_occurrences(self):
        a = m.MultiSet(1, 1, 2, 3)
        b = m.MultiSet(2, 3, 4, 4)
        a.__iadd__(b)
        expected = m.MultiSet(1, 1, 2, 2, 3, 3, 4, 4)
        self.assertEqual(a, expected, "a should be updated with set b.")

    def test_Eadd_different_length(self):
        a = m.MultiSet(1, 2)
        b = m.MultiSet(4, 3, 5)
        a.__iadd__(b)
        expected = m.MultiSet(1, 2, 3, 4, 5)
        self.assertEqual(a, expected, "a should be updated with set b.")

    def test_Eadd_empty_set(self):
        a = m.MultiSet()
        b = m.MultiSet(4, 3, 2, 1)
        a.__iadd__(b)
        expected = m.MultiSet(1, 2, 3, 4)
        self.assertEqual(a, expected, "a should be updated with set b.")

    def test_intersection_standard(self):
        a = m.MultiSet(1, 2, 3, 4, 5, 6, 7)
        b = m.MultiSet(5, 6, 7, 8, 9, 10, 11)
        c = a & b
        expected = m.MultiSet(5, 6, 7)
        self.assertEqual(c, expected, "5, 6, and 7 belong to both sets.")

    def test_intersection_multiple_occurrences(self):
        a = m.MultiSet(1, 2, 3, 3)
        b = m.MultiSet(4, 5, 3, 3)
        c = a & b
        expected = m.MultiSet(3, 3)
        self.assertEqual(c, expected, "3 and 3 are in both sets.")

    def test_intersection_different_lengths(self):
        a = m.MultiSet(1, 2, 3, 4)
        b = m.MultiSet(4, 3, 2, 1, 9, 9, 9)
        c = a & b
        expected = m.MultiSet(1, 2, 3, 4)
        self.assertEqual(c, expected, "1, 2, 3, 4 are in both sets.")

    def test_intersection_empty_set(self):
        a = m.MultiSet()
        b = m.MultiSet(4, 3, 2, 1, 9, 9, 9)
        c = a & b
        expected = m.MultiSet()
        self.assertEqual(c, expected, "One set is empty.")

    def test_Eintersection_standard(self):
        a = m.MultiSet(1, 2, 3, 4, 5, 6, 7)
        b = m.MultiSet(5, 6, 7, 8, 9, 10, 11)
        a.__iand__(b)
        expected = m.MultiSet(5, 6, 7)
        self.assertEqual(a, expected, "5, 6, and 7 belong to both sets.")

    def test_Eintersection_multiple_occurrences(self):
        a = m.MultiSet(1, 2, 3, 3)
        b = m.MultiSet(4, 5, 3, 3)
        a.__iand__(b)
        expected = m.MultiSet(3, 3)
        self.assertEqual(a, expected, "3 and 3 are in both sets.")

    def test_intersection_different_lengths(self):
        a = m.MultiSet(1, 2, 3, 4)
        b = m.MultiSet(4, 3, 2, 1, 9, 9, 9)
        a.__iand__(b)
        expected = m.MultiSet(1, 2, 3, 4)
        self.assertEqual(a, expected, "1, 2, 3, 4 are in both sets.")

    def test_intersection_empty_set(self):
        a = m.MultiSet()
        b = m.MultiSet(4, 3, 2, 1, 9, 9, 9)
        a.__iand__(b)
        expected = m.MultiSet()
        self.assertEqual(a, expected, "One set is empty.")

    def test_disjoint_standard_T(self):
        a = m.MultiSet(1, 2, 3, 4, 5, 6, 7)
        b = m.MultiSet(5, 6, 7, 8, 9, 10, 11)
        c = a.isdisjoint(b)
        self.assertEqual(c, False, "5, 6, and 7 belong to both sets.")

    def test_disjoint_standard_F(self):
        a = m.MultiSet(1, 2, 3, 4)
        b = m.MultiSet(5, 6, 7, 8)
        c = a.isdisjoint(b)
        self.assertEqual(c, True, "The sets are disjoint.")

    def test_disjoint_different_lengths_T(self):
        a = m.MultiSet(1, 2, 3, 4)
        b = m.MultiSet(5, 6)
        c = a.isdisjoint(b)
        self.assertEqual(c, True, "Sets are disjoint.")

    def test_disjoint_different_lengths_F(self):
        a = m.MultiSet(1, 2, 3, 5)
        b = m.MultiSet(5, 6)
        c = a.isdisjoint(b)
        self.assertEqual(c, False, "5 belongs to both sets.")

    def test_disjoint_empty_set(self):
        a = m.MultiSet()
        b = m.MultiSet(5, 6)
        c = a.isdisjoint(b)
        self.assertEqual(c, True, "Sets are disjoint, one is empty.")

unittest.main(exit=False)
