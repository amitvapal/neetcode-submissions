class Solution {
public:
    bool isAnagram(string s, string t) {

        unordered_map<char, int> freq;

        for (char c : s){
            freq[c] += 1;
        }

        for(char x : t){
            freq[x] -= 1;
        }

        for(auto pair: freq){
            if(pair.second != 0) return false;
        }

        return true;


        
    }
};
