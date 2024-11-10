# import pawnshop as pw
# import unittest

# class TestPawnshopApp(unittest.TestCase):
#     def setUp(self) -> None:
#         self.data_list = {
#             1:{

#                 'ціна':500,
#                 'назва' : 'годинник'
#             },
#             2:{
#                 'ціна': 300,
#                 'назва' : 'телефон'
#             },
#             3:{
#                 'ціна': 400,
#                 'назва' : 'павербанк'
#             }}
        
#     def test_get_last_id(self):
#         self.assertEqual(pw.get_last_id(self.data_list), 3)

#     def test_get_item(self):
#         self.assertEqual(pw.get_item(self.data_list, 1), {
#                 'ціна':500,
#                 'назва' : 'годинник'
#             })
#         self.assertEqual(pw.get_item(self.data_list, 3), {
#                 'ціна': 400,
#                 'назва' : 'павербанк'
#             })
#         self.assertRaises(KeyError, pw.get_item, self.data_list, -1)

#     def test_add_item(self):
#         self.assertEqual(pw.add_item(self.data_list, {
#                 'ціна':500,
#                 'назва' : 'годинник'
#             }), 4)
#         self.assertEqual(self.data_list[4], {
#                 'ціна':500,
#                 'назва' : 'годинник'
#             })
        
#     def test_update_item(self):
#         self.assertEqual(pw.update_item(self.data_list, 3, {
#                 'ціна': 450,
#                 'назва' : 'павербанк'
#             }), {
#                 'ціна': 450,
#                 'назва' : 'павербанк'
#             })
#         self.assertRaises(KeyError, pw.update_item, self.data_list, -1, {
#                 'ціна': 400,
#                 'назва' : 'павербанк'
#             })
    
#     def test_delete_item(self):
#         lenght = len(self.data_list)
#         self.assertEqual(pw.delete_item(self.data_list, 3), {
#                 'ціна': 400,
#                 'назва' : 'павербанк'
#             })
#         self.assertEqual(lenght-1, len(self.data_list))
#         self.assertRaises(KeyError, pw.delete_item, self.data_list, -1)

#     def test_show_items(self):
#         self.assertEqual(pw.show_items(self.data_list), 3)

#     @unittest.expectedFailure
#     def test_failure(self):
#         self.assertEqual(pw.get_last_id(self.data_list), 0)


# if __name__ == '__main__':
#     unittest.main()