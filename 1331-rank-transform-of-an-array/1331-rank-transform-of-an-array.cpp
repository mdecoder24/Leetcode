class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        vector<int> sortedUnique = arr;
        sort(sortedUnique.begin(), sortedUnique.end());
        sortedUnique.erase(unique(sortedUnique.begin(), sortedUnique.end()), 
                          sortedUnique.end());
        vector<int> ranks;
        for (int element : arr) {
            int rank = upper_bound(sortedUnique.begin(), sortedUnique.end(), element) 
                       - sortedUnique.begin();
            ranks.push_back(rank);
        }
      
        return ranks;
    }
};