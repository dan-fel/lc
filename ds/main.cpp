#include "linked_list.hpp"

int main()
{

    LinkedList list{};

    list.Add(10);
    list.Add(20);
    list.Add(30);

    list.PrintList();

    list.Delete(20);

    list.PrintList();

    return 0;
}