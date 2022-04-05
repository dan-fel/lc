#include <iostream>

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    void swap(TreeNode *node)
    {
        TreeNode *temp = node->left;
        node->left = node->right;
        node->right = temp;
    }

    TreeNode *invertTree(TreeNode *root)
    {
        if (root == nullptr)
            return root;

        invertTree(root->left);
        invertTree(root->right);

        swap(root);
        return root;
    }

    void PrintInOrder(TreeNode *root)
    {
        if (root == nullptr)
            return;

        std::cout << root->val << std::endl;

        PrintInOrder(root->left);
        PrintInOrder(root->right);
    }
};

int main()
{

    TreeNode left_23{6};
    TreeNode right_24{9};

    TreeNode left_21{1};
    TreeNode right_22{3};

    TreeNode left_1{2, &left_21, &right_22};
    TreeNode right_1{7, &left_23, &right_24};
    TreeNode tree{4, &left_1, &right_1};

    TreeNode *root_copy = &tree;
    Solution sol{};

    sol.PrintInOrder(&tree);
    std::cout << "-------------------------------" << std::endl;
    TreeNode *inverted_tree = sol.invertTree(&tree);
    sol.PrintInOrder(inverted_tree);

    return 0;
}