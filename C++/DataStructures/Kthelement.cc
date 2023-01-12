#include<iostream>
#include<cstring>
#include <algorithm>

using namespace std;

class KthElementFromArray {
	private:
		int size;
		int *array;
		int filled;
		void resize();
	public:
		KthElementFromArray() {
			size = 2;
			filled= 0;
			array = new int[size];
		}
		void add(int item){
			if(this->filled <this->size)
				this->array[this->filled++] = item;
			else{
				resize();
				this->array[this->filled++] = item;
			}
		}
		void readArray(){
			for(int i=0;i<this->filled;i++)
				cout<<this->array[i]<<" ";
			cout<<endl;
		}
		int Kthsmallest(int k);
		int Kthlargest(int k);

};

void KthElementFromArray::resize() {
	int newsize =2*this->size;
	int *newarray = new int[newsize];
	memcpy(newarray,this->array,this->size*sizeof(int));
	delete [] array;
	this->array = newarray;
	this->size = newsize;
}

int KthElementFromArray::Kthlargest(int k) {
	if(this->filled < k) {
		return -1;
	} else {
		std::sort(this->array, this->array+this->filled);
		return this->array[this->filled-k];
	}
}
int KthElementFromArray::Kthsmallest(int k) {
	if(this->filled < k) {
		return -1;
	} else {
		std::sort(this->array, this->array+this->filled);
		return this->array[k-1];
	}
}
int main() {
	KthElementFromArray ele_array;
	ele_array.add(3);
	ele_array.add(11);
	ele_array.add(6);
	ele_array.add(17);
	ele_array.add(8);
	ele_array.add(15);
	ele_array.readArray();
	cout<<"Kth smallest:"<<ele_array.Kthsmallest(2)<<" for k value:"<<2<<endl;
	cout<<"Kth largest:"<<ele_array.Kthlargest(3)<<" for k value:"<<3<<endl;
	return 0;
}
