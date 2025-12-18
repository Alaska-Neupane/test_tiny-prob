# This program contains function to find the longest prefix in the given list of strings
def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = ""
    for i in range(len(strs[0])):      
        char = strs[0][i]
        for word in strs[1:]:
            if i >= len(word) or word[i] != char:
                return prefix
        prefix += char
    return prefix

if __name__ == "__main__":
    print(longest_common_prefix(['bategory','bateg','bateo']))
