#include <bits/stdc++.h>
using namespace std;
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>
// using namespace __gnu_pbds;
// #define p(x,y) pair<x,y>
// #define oset(x) tree<x, null_type, less<x>, rb_tree_tag, tree_order_statistics_node_update>
// #define all(x) (x).begin(),(x).end()
// #define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define ll long long
// #define int ll
#define scan(a)      \
  for (auto &it : a) \
    cin >> it;
#define print(a)         \
  {                      \
    for (auto it : a)    \
      cout << it << " "; \
    cout << endl;        \
  }
#define finish(a)      \
  {                    \
    cout << a << "\n"; \
    return;            \
  }
#define out(a)         \
  {                    \
    cout << a << "\n"; \
  }
#define fr(i, n) for (int i = 0; i < n; i++)
#define fr_(i, j, n) for (int i = j; i < n; i++)
void swp(int *a, int *b)
{
  *a += *b;
  *b = *a - *b;
  *a -= *b;
}

void solve(int tc)
{
  int n=9;
  // cin>>n;
  vector<int> dp(n+1,0);
  dp[1]=1;
  for(int i=1;i<=n;i++)
    for(int j=i+1;j<=n;j++)
      if(j%(j-i)==0)
        dp[j]+=dp[i]; 
  for(int i=1;i<=n;i++)
    cout<<i<<"\t";
  cout<<"\n";  
  for(int i=1;i<=n;i++)
    cout<<dp[i]<<"\t";
  // return dp[n];
  
  vector<int> dp2(n+1,0);
  dp2[n]=1;
  for(int i=n-1;i>=1;i--)
    for(int j=i+1;j<=n;j++)
      if(j%(j-i)==0)
        dp2[i]+=dp2[j];
  cout<<"\n";  
  for(int i=1;i<=n;i++)
    cout<<dp2[i]<<"\t";
  // return dp2[1];
}

int32_t main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int t = 1;
  //init();
  // cin >> t;
  for (int z = 0; z < t; z++)
  {
    solve(z + 1);
  }
  return 0;
}