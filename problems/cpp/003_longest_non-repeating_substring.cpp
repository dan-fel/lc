#include <string>
#include <iostream>
#include <unordered_map>
#include <cmath>

class Solution
{
public:
    int lengthOfLongestSubstring(std::string s)
    {
        int current_max{0};
        int back_index{0};
        std::unordered_map<char, int> hash_table;

        for (int i = 0; i < s.length(); i++)
        {
            char c = s[i];
            bool char_in_table{hash_table.count(c) > 0};
            if (char_in_table)
            {
                int target_index = hash_table[c];

                while (back_index <= target_index)
                {
                    hash_table.erase(s[back_index]);
                    back_index++;
                }
            }
            hash_table[s[i]] = i;
            current_max = std::max(i - back_index + 1, current_max);

            if (current_max > s.length() - i)
            {
                return current_max;
            }
        }
        return current_max;
    }
};

int main()
{

    Solution sol{};
    std::cout << sol.lengthOfLongestSubstring("abcabcbb") << std::endl;

    return 0;
}