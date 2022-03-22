#include <iostream>

struct Data
{
    Data *next;
    int value;
};

class LinkedList
{
public:
    LinkedList()
    {
    }

    ~LinkedList()
    {
        Data *curr{front_};
        while (curr != nullptr)
        {
            Data *temp{curr->next};
            delete (curr);
            curr = temp;
        }
    }

    void Add(int val)
    {

        Data *data = new Data();
        data->value = val;

        if (front_ == nullptr)
        {
            front_ = data;
            current_ = data;
        }
        else
        {
            current_->next = data;
            current_ = data;
        }
    }

    void PrintList()
    {
        Data *curr{front_};
        while (curr != nullptr)
        {
            std::cout << curr->value << std::endl;
            curr = curr->next;
        }
    }

    void Delete(int val)
    {
        Data *curr{front_};
        Data *prev;
        while (curr->value != val)
        {
            prev = curr;
            curr = curr->next;
        }

        prev->next = curr->next;
        delete (curr);
    }

    void Get()
    {
    }

    Data *front_{nullptr};
    Data *current_{nullptr};
    Data *back_{nullptr};
};