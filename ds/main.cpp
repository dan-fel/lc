#include "linked_list.hpp"
#include "hash_table.hpp"

int main()
{

    // LinkedList list{};

    // list.Add(10);
    // list.Add(20);
    // list.Add(30);

    // list.PrintList();

    // list.Delete(20);

    // list.PrintList();

    HashTable ht{100};

    std::string hello = "hello";
    std::string world = "world";

    std::string hello2 = "asdz";
    std::string world2 = "tert";

    ht.InsertItem(hello);
    ht.InsertItem(world);
    ht.InsertItem(hello2);
    ht.InsertItem(world2);

    std::cout << ht.GetItem(hello) << std::endl;
    std::cout << ht.GetItem(world) << std::endl;
    std::cout << ht.GetItem(hello2) << std::endl;
    std::cout << ht.GetItem(world2) << std::endl;

    return 0;
}