/** @file bintree.c
* 
* @brief Binary Tree implementation
*
*@author Lajos Onodi Neto
*/

#include "bintree.h"
#include <stdlib.h>
#include <stdio.h>

BinTree *new_bintree(){
    
    BinTree *binTree = malloc(sizeof(BinTree));
    binTree->root = NULL;
    return binTree;
}

Node *new_node(int value){
    
    Node *new_node = malloc(sizeof(Node));
    new_node->key = value;
    new_node->left = NULL;
    new_node->right = NULL;
    return new_node;
}

Node *put_aux(Node *root, int value){

    if (root == NULL) return new_node(value);
    else if(value < root->key) root->left = put_aux(root->left, value);
    else if(value > root->key) root-> right = put_aux(root->right,value);
    else root->key = value;

    return root;
}

void put(BinTree *binTree, int value){ 

    binTree->root = put_aux(binTree->root, value);
}

void print_inorder(Node *node){
    
    if(node == NULL) {
        return;
    }
    print_inorder(node->left);
    printf("%d ", node->key);
    print_inorder(node->right);
}

void print_preorder(Node *node){

    if(node == NULL){
        return;
    }
    printf("%d ", node->key);
    print_preorder(node->left);
    print_preorder(node->right);
}

void print_postorder(Node *node){
    
    if(node == NULL){
        return;
    }
    print_postorder(node->left);
    print_postorder(node->right);
    printf("%d ", node->key);
}

void print_increase_order(Node *root){
    print_inorder(root);
}

int min_value(Node *root){
    int min = 0;
    if(root->left == NULL){
        return root->key;
    }
    min = min_value(root->left);
    return min;
}

int max_value(Node *root){
    int max = 0;
    if(root->right == NULL){
        return root->key;
    }
    max = max_value(root->right);
    return max;
}

int check_value(Node *root, int value){
    
    if(root == NULL){
        return 0;
    }
    if(value > root->key) return check_value(root->right, value);
    else if(value < root->key) return check_value(root->left, value);
    return 1;
}

Node *get_node(Node *root, int value){

    if(root == NULL) return NULL;
    if(root->key == value) return root;
    
    if(value > root->key) return get_node(root->right, value);
    if(value < root->key) return get_node(root->left, value);
}

// Checks if the binary tree root is the given node. In this case, there is no
// parent node for the root. Than It is always checked if one of the current node
// children is the value we are looking for, if so, the current node is returned as the
// parent. If the value is not within the current node children, we move forward 
// deeper in the tree until we return NULL if the value is not found.
Node *get_parent(Node *root, int value){

    if(root->key == value) return root;
    if(root->left == NULL && root->right == NULL) return NULL;
    if(root->left && root->left->key == value) return root;
    if(root->right && root->right->key == value) return root;
    if(root->right && value > root->key) return get_parent(root->right, value);
    if(root->left && value < root->key) return get_parent(root->left, value);
}

// Returns the sucessor fo a given node.
// First we check if the given node key is the biggest one within the tree.
// Then we check if the given node has a right child, if so, the sucessor is the minimum 
// key from the given node right subtree. If the last case is not true, then we need to look
// to the node's parent. We take the current node parent and check if the current node is the left
// child of its parent, if so, the parent is the sucessor. If not, we keep on walking up the
// tree until we find the first node that is the left child of its parent.
Node *get_sucessor(Node *binTreeRoot, Node *node){

    if(node->key == max_value(binTreeRoot)){
        return node;
    }

    if(node->right){
        int sucessor_key = min_value(node->right);
        return get_node(binTreeRoot, sucessor_key);
    }

    Node *parent = get_parent(binTreeRoot, node->key);
    while(parent!=NULL && node == parent->right){
        node = parent;
        parent = get_parent(binTreeRoot, node->key);
    }
    return parent;
}

int node_count(Node *root){

    int count = 1;
    if(root->left) count += node_count(root->left);
    if(root->right) count += node_count(root->right);
    return count;
}


int check_depth(Node *root){

    if(root == NULL) return 0;

    int left_size = check_depth(root->left);
    int right_size = check_depth(root->right);

    if(left_size>right_size) return left_size+1;
    else return right_size+1;
}