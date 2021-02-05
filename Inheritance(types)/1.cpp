// Multilevel Inheritance
#include <iostream>
using namespace std;

class A
{
public:
    void display()
    {
        cout << "Base class content " << endl;
    }
};

class B : public A
{
};
class c : public B
{
};

int main()
{
    c obj;
    obj.display();
    return 0;
}