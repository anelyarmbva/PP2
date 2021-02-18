#include <bits/stdc++.h>
using namespace std;

int main(){
    int cnt;
    cnt = 0;
    string s;
    cin >> s;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == " ") {
            cnt++;
        }  
          }
    cout << cnt;
}