#include <algorithm>
#include <iostream>
#include <vector>
#include <stack>


int PUSH(std::stack <char>* st, char x) {
    (*st).push(x);
    return 0;
}

struct stct
{
    int code;
    char chr;
    stct(int co, char ch) {
        this->code = co;
        this->chr = ch;
    }
};

stct POP(std::stack <char>* st) {
    if ((*st).size() == 0) {
        return stct(1, '\0');
    }
    else {
        char c = (*st).top();
        (*st).pop();
        return stct(0, c);
    }
}

void checkInput() {
    std::cout << "Enter a string:\n";
    std::string str;
    std::cin >> str;
    std::stack <char> st;
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == '(') {
            PUSH(&st, '(');
        }
        else {
            if (str[i] == ')') {
                stct s1 = POP(&st);
                if (s1.code == 1) {
                    std::cout << "Error stack is empty";
                    return;
                }
            }
        }
    }
    if (st.size() != 0) {
        std::cout << "Error: stack is still not empty";
    }
    else {
        std::cout << "All is ok";
    }
}
double recur(int n)
{
    if (n == 0)
        return 0.5;
    return 3.0 / n* recur(n-1);
}
int main()
{

    checkInput();
    /*int n;
    std::cout << "Enter n: " << std::endl;
    std::cin >> n;
    double an = recur(n);
    std::cout << an;*/
    return 0;
}