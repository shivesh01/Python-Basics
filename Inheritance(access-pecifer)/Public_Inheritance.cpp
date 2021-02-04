// Public Inheritance
#include <iostream>
using namespace std;

class Base {
    private:
    int pvt =1;

    protected:
    int prot =2;

    public:
    int Pub =3;

    int getPVT(){
        return pvt;

    }
};
class publicDerived : public Base{
    public:

    int getProt(){
        return prot;
    }
};

int main(){
    publicDerived object1;
    cout <<"Private = "<< object1.getPVT()<<endl;
    cout <<"Protected = "<< object1.getProt()<<endl;
    cout <<"Public = "<<object1.Pub<<endl;
    return 0;
}