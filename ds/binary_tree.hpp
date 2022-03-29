#include <cstdint>

class Node
{
public:
    Node(const Node &left, const Node &right, const std::int32_t val) noexcept : left_{left}, right_{right}, val_{val} {}
    Node(Node *parent, const Node &left, const Node &right, const std::int32_t val) noexcept : p_{parent}, left_{left}, right_{right}, val_{val} {}

private:
    Node *p_{nullptr};
    const Node &left_;
    const Node &right_;
    const std::int32_t val_;
};

class BinaryTree
{
public:
    BinaryTree(const Node &root) noexcept : root_{root} {}

    void Find(std::int32_t key) {}
    void Insert(std::int32_t key) {}
    void Remove(std::int32_t key) {}
    void Free() {}

private:
    const Node &root_;
};