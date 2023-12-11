from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""
        for s in strs:
            encoded_string += s
            encoded_string += ":;"            
        return encoded_string

    def decode(self, encoded_str):
        i = 0
        curr = ""
        decoded_str = []
        while i < len(encoded_str):
            if encoded_str[i] == ':' and encoded_str[i+1] == ';':
                decoded_str.append(curr)
                curr = ""
                i += 2
            else:                           
                curr += encoded_str[i]
                i += 1

        return decoded_str
                



sol = Solution()

res = sol.encode(["lint", "code", ":", "you"])
print(res)
res_list = sol.decode(res)
print(res_list)
#print(sol.encode(["lint", "code", ":", "you"]))