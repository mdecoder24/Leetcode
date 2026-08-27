class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int n=s.size();
        vector<int> c(26);

        for(char x:s)c[x-'a']++;

        int p=-1;

        for(int i=0;i<n;i++){
            int x=target[i]-'a';

            if(c[x]){
                c[x]--;

                for(int j=x+1;j<26;j++){
                    if(c[j]){
                        p=i;
                        break;
                    }
                }
            }else{
                for(int j=x+1;j<26;j++){
                    if(c[j])p=i;
                }
                break;
            }
        }

        if(p==-1)return "";

        c.assign(26,0);
        for(char x:s)c[x-'a']++;

        for(int i=0;i<p;i++)
            c[target[i]-'a']--;

        int x=target[p]-'a';
        int y=x+1;

        while(y<26&&!c[y])y++;

        if(y==26)return "";

        string r=target.substr(0,p);
        r+=char('a'+y);
        c[y]--;

        for(int i=0;i<26;i++){
            while(c[i]){
                r+=char('a'+i);
                c[i]--;
            }
        }

        return r;
    }
};