/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        std::unordered_map<Node*, Node*> oldToCopy;
        oldToCopy[NULL] = NULL;
        Node* temp = head;

        while (temp != NULL) {
            oldToCopy[temp] = new Node(temp->val);
            temp = temp->next;
        }

        temp = head;
        while (temp != NULL) {
            Node* copy = oldToCopy[temp];
            copy->next = oldToCopy[temp->next];
            copy->random = oldToCopy[temp->random];
            temp = temp->next;
        }

        return oldToCopy[head];
    }
};
