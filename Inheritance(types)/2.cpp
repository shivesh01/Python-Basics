// Multiple Inheritance
#include <iostream>
using namespace std;

class Mammal
{
public:
    Mammal()
    {
        cout << "Mammals can give birth." << endl;
    }
};

class wingedanimal
{
public:
    wingedanimal()
    {
        cout << "Winged animal can flap. " << endl;
    }
};

class Bat : public Mammal, public wingedanimal
{
};

int main()
{
    Bat b1;
    return 0;
}
