/** @file main.c
* 
* @brief Binary Tree implementation
*
*@author Lajos Onodi Neto
*/

#include "bintree.h"
#include <stdio.h>

int main(){

    BinTree *binTree = new_bintree();
    put(binTree, 20);
    
    printf("\n\n");
    return 0;
}