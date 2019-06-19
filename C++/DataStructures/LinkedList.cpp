#include<iostream>

using namespace std;

typedef struct Node {
	int data;
	struct Node *next;
}Node;

class LinkedList {
	Node *head, *tail;
	int cntr;
	public:
		LinkedList() {
			head = NULL;
			tail = NULL;
			cntr = 0;
		}
		int getCntr(){return this->cntr;};
		void incCntr(){this->cntr = this->cntr+1;};
		void decCntr(){this->cntr = this->cntr-1;};
		void add_node(int item);
		void delete_node(int pos);
		void print_list();
};

void LinkedList::delete_node(int pos) {
	if (pos > this->getCntr() || pos < 1) {
		cout<<"Invalid input"<<endl;
		return;
	}
	Node *tmp=this->head;
	if(pos == 1){
		head = head->next;
		delete tmp;
		this->decCntr();
	}
	else if(pos == getCntr()){
		while(tmp->next != tail) {
			tmp = tmp->next;
		}
		tmp->next = NULL;
		delete tail;
		tail = tmp;
		this->decCntr();
	}/*
	else{
		for(int i = 1;i < pos-1;i++)
			tmp = tmp->next;
	}
	*/
}

void LinkedList::add_node(int item){
	Node *tmp = new Node;
	tmp->data = item;
	tmp->next = NULL;
	if (this->head == NULL) {
		head = tmp;
		tail = tmp;
	}else {
		tail->next = tmp;
		tail = tmp;
	}
	this->incCntr();
}
void LinkedList::print_list(){
	Node *tmp=this->head;
	cout<<"["<<this->getCntr()<<"]"<<"[ ";
	while(tmp != NULL) {
		cout<<tmp->data<<" ";
		tmp = tmp->next;
	}
	cout<<"]"<<endl;
}



int main(void) {
	LinkedList l;
	l.add_node(1);
	l.add_node(2);
	l.add_node(3);
	l.add_node(4);
	l.print_list();
	l.delete_node(4);
	l.print_list();
	return 0;
}
