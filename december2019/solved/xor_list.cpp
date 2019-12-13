#include <iostream>
#include <string>
using namespace std;

// This problem was asked by Google.

// An XOR linked list is a more memory efficient doubly linked list.
// Instead of each node holding next and prev fields, it holds a field
// named both, which is an XOR of the next node and the previous node.
// Implement an XOR linked list; it has an add(element) which adds the
// element to the end, and a get(index) which returns the node at index.

// If using a language that has no pointers (such as Python), you can
// assume you have access to get_pointer and dereference_pointer functions
// that converts between nodes and memory addresses.

/*
    NOTE:  If we do XOR of curr->both and prev, we get the address of next node.

    I ended up using the internet for help on this one. Super cool problem, it was fun
    to solve.
*/

struct Node;

/* returns XORed value of the node addresses 
    From geeksforgeeks https://www.geeksforgeeks.org/xor-linked-list-a-memory-efficient-doubly-linked-list-set-2/
*/
Node *XOR(Node *a, Node *b)
{
    return (Node *)((uintptr_t)(a) ^ (uintptr_t)(b));
}

struct Node
{
    string value;
    Node *both;
    /* Next helper function. Found here https://stackoverflow.com/questions/51599273/xor-linked-list-with-c */
    Node *next(Node *prev)
    {
        return XOR(prev, both);
    }
};

class XORlist
{
public:
    XORlist()
    {
        head = nullptr;
        size = 0;
    }

    ~XORlist()
    {
        if (head != nullptr)
        {
            Node *temp = head;
            Node *prev = nullptr;
            Node *next;
            while (temp != nullptr)
            {
                next = temp->next(prev);
                prev = temp;
                temp = next;
                delete prev;
            }
        }
        head = nullptr;
    }

    void printList()
    {
        Node *current = head;
        Node *prev = nullptr;
        Node *next;
        while (current != nullptr)
        {
            cout << current->value << endl;
            next = current->next(prev);
            prev = current;
            current = next;
        }
    }

    // append node to the end of the linked list
    void appendNode(string value)
    {
        if (head == nullptr)
        {
            Node *newNode = new Node;
            newNode->value = value;
            head = newNode;
            head->both = XOR(nullptr, nullptr);
            size++;
        }
        else
        {
            Node *newNode = new Node;
            Node *current = head;
            Node *prev = nullptr;
            Node *next;
            while (current->next(prev) != nullptr)
            {
                next = current->next(prev);
                prev = current;
                current = next;
            }
            newNode->value = value;
            newNode->both = XOR(current, nullptr);
            current->both = XOR(prev, newNode);
            size++;
        }
    }

    // return a pointer to the node if found. return nullptr if invalid index
    Node *getNode(int index)
    {
        if (index < size && index >= 0)
        {
            Node *retNode = head;
            Node *prev = nullptr;
            Node *next;
            for (int i = 0; i < index; i++)
            {
                next = retNode->next(prev);
                prev = retNode;
                retNode = next;
            }

            return retNode;
        }
        else
        {
            return nullptr;
        }
    }

private:
    Node *head;
    int size;
};

int main()
{
    XORlist testcase;
    testcase.appendNode("Jacob");
    testcase.appendNode("Mike");
    testcase.appendNode("Ryan");
    testcase.appendNode("Jon");
    testcase.appendNode("Sam");
    testcase.printList();

    cout << "\n";

    int index = 2;
    Node *found = testcase.getNode(index);
    if (found != nullptr)
    {
        cout << "Node at index " << index << ": " << found->value << endl;
    }
    else
    {
        cout << "Index '" << index << "' does not exist" << endl;
    }
    return 0;
}