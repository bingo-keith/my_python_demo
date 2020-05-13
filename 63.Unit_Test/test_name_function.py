import unittest
from name_function import get_formatted_name


class TestNamesCase(unittest.TestCase):
    """测试test_name_function.py"""

    def test_first_last_name(self):
        """能够正确的处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('bingo', 'keith')
        self.assertEqual(formatted_name, 'Bingo Keith')

    def test_first_last_middle_name(self):
        """能够正确地处理像bingo chilly keith这样的姓名吗？"""
        formatted_name = get_formatted_name('bingo', 'keith', 'chilly')
        self.assertEqual(formatted_name, 'Bingo Chilly Keith')


if __name__ == '__main__':
    unittest.main()

# assertEqual(a, b) 核实a == b
# assertNotEqual(a, b) 核实a != b
# assertTrue(x) 核实x 为True
# assertFalse(x) 核实x 为False
# assertIn(item , list ) 核实 item 在 list 中
# assertNotIn(item , list ) 核实 item 不在 list 中
