#include "linked_list.hpp"
#include "hash_table.hpp"
#include "binary_tree.hpp"

int main()
{
    Node *root{new Node(nullptr, nullptr, nullptr, 5)};

    BinaryTree bst{root};

    bst.Insert(10);
    bst.Insert(11);
    bst.Insert(12);

    bst.Insert(1);
    bst.Insert(2);
    bst.Insert(3);
    bst.PrintTree(root);

    return 0;
}