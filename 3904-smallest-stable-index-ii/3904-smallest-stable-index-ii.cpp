class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int>prefix_max(n,0);
        vector<int>suffix_min(n,0);

        prefix_max[0] = nums[0];
        
        for(int i=1;i<n;i++){
            prefix_max[i] = max(prefix_max[i-1],nums[i]); 
        }

        suffix_min[n-1] = nums[n-1];
        for(int i=n-2;i>=0;i--){
            suffix_min[i] = min(suffix_min[i+1],nums[i]);
        }

        int index = -1;

        for(int i=0;i<n;i++){
            int diff = 0;
            diff = prefix_max[i] - suffix_min[i];
            if(diff <= k){
                index = i;
                break;
            }
        }
        
        return index;
    }
};