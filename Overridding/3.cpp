// Call Overridden Function From Derived Class

#include <iostream>
using namespace std;

class Base
{
public:
    void print()
    {
        cout << "Base Function" << endl;
    }
};

class Derived : public Base
{
public:
    void print()
    {
        cout << "Derived Function" << endl;
        // calling overridden function from Derived class
        Base::print();
    }
};

int main()
{
    Derived derived1;
    derived1.print();
    return 0;
}