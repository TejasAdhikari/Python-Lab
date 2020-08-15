#include<bits/stdc++.h>
using namespace std;

int main(){
    vector <int> a={2,4,3,5,3,1,9,6,5,8,4};
    int len=a.size();
    int count[10]={0};
    int store[len];
    for(int i=0; i<len; i++){
        count[a[i]]++;
    }
    for(int m=1; m<10; m++){
        count[m]+=count[m-1];
    }
    for(int j=len-1; j>0; j--){
        store[count[a[j]]-1]=a[j];
        count[a[j]]--;
    }
    for(int k=0; k<len; k++){
        a[k]=store[k];
    }
    for(int l=0; l<len; l++){
        cout<<a[l]<<" ";
    }
}
