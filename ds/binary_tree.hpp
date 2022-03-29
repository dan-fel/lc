#include <cstdint>
#include <iostream>

class Node
{
public:
    Node(Node *left, Node *right, const std::int32_t val) noexcept : p_{nullptr}, left_{left}, right_{right}, val_{val} {}
    Node(Node *parent, Node *left, Node *right, const std::int32_t val) noexcept : p_{parent}, left_{left}, right_{right}, val_{val} {}

    Node *p_;
    Node *left_;
    Node *right_;
    const std::int32_t val_;

private:
};

class BinaryTree
{
public:
    BinaryTree(Node *root) noexcept : root_{root} {}

    Node *CreateNode(Node *parent, std::int32_t val)
    {
        return new Node(parent, nullptr, nullptr, val);
    }
    void DestroyNode()
    {
    }
    void Find(std::int32_t val) {}
    void Insert(std::int32_t val)
    {
        // Use non-recursive iteration.

        bool left{false};
        bool right{false};

        Node *current{root_};
        Node *prev{root_};

        while (current != nullptr)
        {
            left = false;
            right = false;
            if (current->val_ <= val)
            {

                prev = current;
                current = current->right_;
                right = true;
            }
            else
            {

                prev = current;
                current = current->left_;
                left = true;
            }
        }

        if (right)
        {
            prev->right_ = CreateNode(prev, val);
        }
        else
        {
            prev->left_ = CreateNode(prev, val);
        }
    }
    void Remove(std::int32_t key) {}
    void PrintTree(Node *node)
    {
        // Print recursively

        if (node == nullptr)
        {
            return;
        }

        std::cout << node->val_ << std::endl;
        PrintTree(node->left_);
        PrintTree(node->right_);
    }

private:
    Node *root_;
};