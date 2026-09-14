#include <stack>

class MyQueue {
public:
    MyQueue() {
    }
    
    void push(int x) {
        push_stack.push(x);
    }
    
    int pop() {
        if (pop_stack.empty()) { fill_popstack();}    
        int elem = pop_stack.top();
        pop_stack.pop();
        return elem;
    }
    
    int peek() {
        if (pop_stack.empty()) {fill_popstack();}

        return pop_stack.top();
    }
    
    bool empty() {
        return push_stack.empty() && pop_stack.empty();
    }

    void fill_popstack() {
        while (!push_stack.empty()) {
            int elem = push_stack.top();
            pop_stack.push(elem);
            push_stack.pop();
        }
    }

private:
    std::stack<int> pop_stack;
    std::stack<int> push_stack;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */