/** @file queue.h
* 
* @brief Queue implementation based on linked lists
*
*@author Lajos Onodi Neto
*/

#ifndef PROJECT_QUEUE_H
#define PROJECT_QUEUE_H

typedef struct Node{
    int value;
    struct Node *next;
} Node;

typedef struct Queue{
    Node *head;
    Node *tail;
} Queue;

// Creates a new queue
Queue *new_queue();
// Checks if the queue is empty
int is_empty(Queue *queue);
// Print queue nodes values
void print(Queue *queue);
// Push a new node into the queue
void enqueue(Queue *queue, int value);
// Pop a node form the queue
void dequeue(Queue *queue);

#endif