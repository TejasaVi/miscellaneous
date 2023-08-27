#include <iostream>

using namespace std;


struct node{
	int value;
	node *left;
	node *right;
};

class bsttree{
public:
	bsttree();
	~bsttree();

	void insert(int key){
		if(root != NULL){
			_insert(key, root);
    	}else{
        	root = new node;
        	root->value = key;
        	root->left = NULL;
        	root->right = NULL;
    	}
	}
	node *search(int key);

private:
	void _destroy_tree();
	void _insert(key, node*leaf);
	node *root;
};


bsttree::bsttree(){
	root = NULL;
}

void bsttree::_insert(key, node *leaf) {
	int tmp;
	if(key < leaf->value){
	}
	else{
    	leaf->left = new node;
        leaf->left->value = key;
        leaf->left->left = NULL;
        leaf->left->right = NULL;
    }
}

int main() {
	return 0;
}
