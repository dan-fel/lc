#include <cstdint>
#include <string>
#include <vector>

class HashTable
{
public:
    using KeyValue = std::string;

    HashTable(int table_size)
    {
        table_.resize(table_size);
    }
    ~HashTable() {}

    void InsertItem(std::string value)
    {
        int index{HashStrToInt(value)};
        table_[index] = value;
    }

    std::string GetItem(std::string key)
    {
        int index{HashStrToInt(key)};
        return table_[index];
    }

private:
    int HashStrToInt(KeyValue key)
    {
        unsigned long hash{5381};
        for (auto &c : key)
        {
            hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
        }
        return (hash % table_.size());
    }

    std::vector<std::string> table_;
};