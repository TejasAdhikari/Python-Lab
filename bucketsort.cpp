#include<bits/stdc++.h>
using namespace std;

void bucketsort(float arr[], int n){
    vector<float> v[n];

    for(int i = 0; i < n; i++){
        int bi = n*arr[i];
        v[bi].push_back(arr[i]);
    }

    for(int i = 0; i < n; i++)
        sort(v[i].begin(), v[i].end());

    int index = 0;
    for(int i = 0; i < n; i++)
        for(int j = 0; j < v[i].size(); j++)
            arr[index++] = v[i][j];
}

int main(){
    float arr[] = {0.3, 0.1, 0.2, 0.34, 0.6};
    int n = sizeof(arr)/sizeof(arr[0]);

    bucketsort(arr, n);

    cout << "Sorted array is: ";
    for(int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }

    return 0;
}