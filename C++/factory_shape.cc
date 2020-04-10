#include<iostream>
#include<string>

using namespace std;

class Shape{
    public:
        virtual void draw() = 0;
};

class Circle: public Shape{
    public:
        void draw() override {
            cout<<"This is a Circle"<<endl;
        };
};

class Rectangle: public Shape{
    public:
        void draw() override {
            cout<<"This is a Rectangle"<<endl;
        };
};

class ShapeFactory{
    public:
        Shape * get_shape(string name) {
            if(!name.compare("circle")){
                return new Circle();
            } else if(!name.compare("rectangle")){
                return new Rectangle();
            } else {
                return NULL;
            }
        }
};


int main() {
    ShapeFactory sf;
    Shape* s = sf.get_shape("circle");
    s.draw()
    return 0;
}
