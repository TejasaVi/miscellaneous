#include<iostream>



using namespace std;

class Singleton{
    private:
        static bool InstanceFlag ;
        static Singleton* single;
        Singleton(){
            cout<<"Inside Constructor\n";
        }
    public:
        static Singleton* GetInstance();
        ~Singleton(){
            cout<<"Inside Destructor\n";
            InstanceFlag = false;
        }
        void method(){
            cout<<"Inside Method\n";
        }

};


bool Singleton::InstanceFlag =false;
Singleton* Singleton::single = NULL;

Singleton* Singleton::GetInstance(){
    if (!InstanceFlag){
        single = new Singleton();
        InstanceFlag = true;
        return single;
    }
    else{
        return single;
    }
}

int main()
{
    Singleton *s;
    Singleton::GetInstance();
    s->method();
    delete s;
    return 0;
}
