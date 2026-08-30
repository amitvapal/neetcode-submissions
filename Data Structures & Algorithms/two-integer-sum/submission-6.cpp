class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int, int> seen;

        for(int i = 0; i < nums.size(); i++){

            int numero = target - nums[i];


            if(seen.find(numero) != seen.end()){
                return {seen[numero], i};
            }

            seen[nums[i]] = i;


        }

        return {};

        
        
    }
};
