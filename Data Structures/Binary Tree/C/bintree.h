/** @file bintree.h
* 
* @brief Binary Tree implementation
*
*@author Lajos Onodi Neto
*/

#ifndef PROJECT_BINTREE_H
#define PROJECT_BINTREE_H

typedef struct Node{
    int key;
    struct Node *left;
    struct Node *right;
} Node;

typedef struct BinTree{
    Node *root;
} BinTree;

// Creates a new binary tree
BinTree *new_bintree();
// Add a new node into the tree if not inserted already
void put(BinTree *binTree, int value);
// Inorder(Left/Root/Right) print of the binary tree
void print_inorder(Node *root);
// Preorder(Root/Left/Right) print of the binary tree
void print_preorder(Node *root);
// Postorder(Left/Right/Root)
void print_postorder(Node *root);
// Prints all nodes values in increasing order
void print_increase_order(Node *root);

#endif