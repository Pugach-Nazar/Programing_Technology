import grades_management as gm
import unittest

class TestGradesManagement(unittest.TestCase):

    def setUp(self):
        self.data_list = {
            ('8-A', 'Soroka I.I.'): {'Math': [12, 10, 8, 9],
                                     'Ukr literature': [9, 7],
                                     'Chemistry': [6, 8, 7],
                                     'Physics': [11, 12, 11, 12],
                                     'PE': [10, 10, 10, 10]},
            ('8-A', 'Nikson A.V.'): {'Math': [12, 11, 10, 7],
                                     'Ukr literature': [10, 11],
                                     'Chemistry': [9, 8, 10],
                                     'Physics': [10, 10, 7, 6],
                                     'PE': [7, 8, 9, 10]},
            ('5-C', 'Kozak A.S.'): {'Math': [9, 10, 10, 10],
                                    'Ukr literature': [9, 10],
                                    'History': [6, 10, 11, 8],
                                    'English': [5, 12, 10, 11],
                                    'PE': [9, 8, 6, 4]},
            ('5-B', 'Moliga T.P.'): {'Math': [11, 11, 11, 10],
                                     'Ukr literature': [12, 10, 11],
                                     'History': [10, 10, 11, 12],
                                     'English': [11, 10, 12, 10, 11],
                                     'PE': [10, 10, 10, 10]},
            ('5-C', 'Vinnichenko D.R.'): {'Math': [10, 10, 10, 10],
                                          'Ukr literature': [11, 10],
                                          'History': [9, 10, 11, 12],
                                          'English': [11, 12, 7, 9, 10],
                                          'PE': [5, 5, 8, 9]}
        }

    def test_add_child(self):
        a = len(self.data_list)
        result = gm.add_child(self.data_list, ('6-B', 'Random D.R.'))
        self.assertEqual(result, a + 1)
        self.assertIn(('6-B', 'Random D.R.'), self.data_list)
        self.assertRaises(ValueError, gm.add_child, self.data_list,('5-C', 'Kozak A.S.'))


    def test_add_child_subjects(self):
        child = ('5-C', 'Kozak A.S.')
        new_subjects = ['Biology', 'Art']
        result = gm.add_child_subjects(self.data_list, child, new_subjects)
        self.assertEqual(result, len(self.data_list[child]))
        self.assertIn('Biology', self.data_list[child])
        self.assertIn('Art', self.data_list[child])
        with self.assertRaises(ValueError):
            gm.add_child_subjects(self.data_list, child, ['Math'])


    def test_add_child_grades(self):
        child = ('8-A', 'Soroka I.I.')
        subject1 = 'Math'
        subject2 = 'Geography'
        new_grades = [12, 11]
        result = gm.add_child_grades(self.data_list, child, subject1, new_grades)
        self.assertEqual(result, len(self.data_list[child][subject1]))
        self.assertEqual(self.data_list[child][subject1], [12, 10, 8, 9, 12, 11])

        result = gm.add_child_grades(self.data_list, child, subject2, new_grades)
        self.assertEqual(result, len(self.data_list[child][subject2]))
        self.assertEqual(self.data_list[child][subject2], [12, 11])
        
        with self.assertRaises(ValueError):
            gm.add_child_grades(self.data_list, ('7-A', 'Nonexistent P.P.'), 'Math', [10, 8])


if __name__ == '__main__':
    unittest.main()
