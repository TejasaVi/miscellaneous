CC= cc
CFLAGS= -Wall -c
DEBUG= -g

BIN_OBJS= bst bin_tree
BASE_OBJS= bin_tree.c  bin_tree.h
LIB_OBJ= bin_tree.o
all: bst bin_tree

bst: BST_Wrapper.c bin_tree.o
	$(CC) BST_Wrapper.c $(LIB_OBJ) -o $@

bin_tree: BinaryTree.c bin_tree.o
	$(CC) BinaryTree.c $(LIB_OBJ) -o $@

bin_tree.o: bin_tree.c  bin_tree.h
	$(CC) $(BASE_OBJS) $(CFLAGS)

clean:
	rm -rf $(BIN_OBJS) $(LIB_OBJ)
