# bst_test.py
# 
# Binary Tree (BST) implementation tests
#
# author Lajos Onodi Neto

import sys
import unittest
from bst import Bst

class BstTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(BstTest, self).__init__(*args, **kwargs)
        self.bst = Bst()
    
    def test_insert(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertTrue(self.bst.insert(20))
        self.assertTrue(self.bst.insert(2))
        self.assertTrue(self.bst.insert(12))
        self.assertFalse(self.bst.insert(5))
    
    def test_size_counter(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertEqual(self.bst._size, 3)
        self.assertTrue(self.bst.insert(20))
        self.assertTrue(self.bst.insert(1))
        self.assertEqual(self.bst._size, 5)
    
    def test_display(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        print("\nInorder traversal :")
        self.bst.dfs_inorder()
        print("Preorder traversal :")
        self.bst.dfs_preorder()
        print("Postorder traversal :")
        self.bst.dfs_postorder()
    
    def test_bfs(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(6)
        self.bst.insert(2)
        self.bst.insert(1)
        self.bst.insert(3)
        self.bst.insert(20)
        self.bst.insert(12)
        self.bst.insert(14)
        self.bst.insert(13)
        self.bst.insert(21)
        self.bst.insert(22)
        self.bst.insert(23)
        bfs_order = self.bst.bfs()
        self.assertEqual(bfs_order, [10,5,15,2,6,12,20,1,3,14,21,13,22,23])
    
    def test_node_count(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(6)
        self.assertEqual(self.bst.node_count(), 4)
        self.bst.insert(2)
        self.assertEqual(self.bst.node_count(), 5)
        self.bst.insert(1)
        self.bst.insert(3)
        self.bst.insert(20)
        self.bst.insert(12)
        self.bst.insert(14)
        self.assertEqual(self.bst.node_count(), 10)
        self.bst.insert(13)
        self.bst.insert(21)
        self.assertEqual(self.bst.node_count(), 12)
        self.bst.insert(22)
        self.bst.insert(23)
        self.assertEqual(self.bst.node_count(), 14)
    
    def test_min(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertEqual(self.bst.min(), 5)
        self.bst.insert(20)
        self.bst.insert(12)
        self.bst.insert(14)
        self.assertEqual(self.bst.min(), 5)
        self.bst.insert(13)
        self.bst.insert(21)
        self.assertEqual(self.bst.min(), 5)
        self.bst.insert(22)
        self.bst.insert(23)
        self.bst.insert(6)
        self.assertEqual(self.bst.min(), 5)
        self.bst.insert(2)
        self.assertEqual(self.bst.min(), 2)
        self.bst.insert(1)
        self.assertEqual(self.bst.min(), 1)
        self.bst.insert(3)
        self.assertEqual(self.bst.min(), 1)

    def test_max(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(6)
        self.assertEqual(self.bst.max(), 15)
        self.bst.insert(2)
        self.bst.insert(1)
        self.bst.insert(3)
        self.bst.insert(20)
        self.assertEqual(self.bst.max(), 20)
        self.bst.insert(12)
        self.bst.insert(14)
        self.assertEqual(self.bst.max(), 20)
        self.bst.insert(13)
        self.bst.insert(21)
        self.assertEqual(self.bst.max(), 21)
        self.bst.insert(22)
        self.assertEqual(self.bst.max(), 22)
        self.bst.insert(23)
        self.assertEqual(self.bst.max(), 23)
    
    def test_height(self):
        self.bst.insert(10)
        self.assertEqual(self.bst.height(), 0)
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertEqual(self.bst.height(), 1)
        self.bst.insert(6)
        self.bst.insert(2)
        self.assertEqual(self.bst.height(), 2)
        self.bst.insert(1)
        self.bst.insert(3)
        self.assertEqual(self.bst.height(), 3)
        self.bst.insert(20)
        self.bst.insert(12)
        self.bst.insert(14)
        self.bst.insert(13)
        self.assertEqual(self.bst.height(), 4)
        self.bst.insert(21)
        self.bst.insert(22)
        self.bst.insert(23)
        self.assertEqual(self.bst.height(), 5)
    
    def test_successor(self):
        self.bst.insert(30)
        self.assertEqual(self.bst.successor(30), -1)
        self.bst.insert(15)
        self.assertEqual(self.bst.successor(15), 30)
        self.bst.insert(20)
        self.assertEqual(self.bst.successor(20), 30)
        self.bst.insert(18)
        self.bst.insert(22)
        self.assertEqual(self.bst.successor(20), 22)
        self.assertEqual(self.bst.successor(22), 30)
        self.bst.insert(10)
        self.assertEqual(self.bst.successor(10), 15)
        self.bst.insert(11)
        self.assertEqual(self.bst.successor(11), 15)
        self.bst.insert(6)
        self.assertEqual(self.bst.successor(6), 10)
        self.bst.insert(4)
        self.assertEqual(self.bst.successor(4), 6)
        self.bst.insert(1)
        self.assertEqual(self.bst.successor(1), 4)
        self.bst.insert(5)
        self.assertEqual(self.bst.successor(5), 6)
        self.bst.insert(9)
        self.assertEqual(self.bst.successor(9), 10)
        self.bst.insert(8)
        self.bst.insert(7)
        self.bst.insert(40)
        self.assertEqual(self.bst.successor(30), 40)
        self.assertEqual(self.bst.successor(40), -1)
        self.bst.insert(50)
        self.assertEqual(self.bst.successor(40), 50)
        self.assertEqual(self.bst.successor(50), -1)
        self.bst.insert(70)
        self.assertEqual(self.bst.successor(70), -1)
        self.bst.insert(90)
        self.assertEqual(self.bst.successor(70), 90)
        self.assertEqual(self.bst.successor(90), -1)
        self.bst.insert(60)
        self.bst.insert(65)
        self.assertEqual(self.bst.successor(65), 70)
        self.bst.insert(55)
        self.bst.insert(51)
        self.bst.insert(57)
        self.assertEqual(self.bst.successor(57), 60)

if __name__ == '__main__':
    unittest.main()
    sys.exit(0)