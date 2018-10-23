#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for (int z = 0; z < t ; ++z)
    {
        /* code */
    
    int n,k;
    cin>>n>>k;

    vector<int> arr;
    int lessk=0;
    int maxsum=0;
    for(int i=0;i<n;i++)
    {
        int a;
        cin>>a;
        if(a<=k) 
        {
            lessk++;
            maxsum+=a;
        }
        else
        {
            arr.push_back(a-k);
        }
    }
    if(arr.size() == 0){
    	cout<<maxsum<<endl;
    	return 0;
    }
    maxsum+=((arr.size()-1)*k);

    int maxval=0;
    int maxind=0;

    for(int i=0;i<arr.size();i++)
    {
        if(arr[i]>maxval)
        {
            maxind=i;
            maxval=arr[i];
        }

    }
    arr[maxind]=0;

    int i=0;
    int n = arr.size();

    sort(arr.begin(),arr.end());
    
    while(true){
    	if(i == n-2){
    		maxsum += arr[n-1]-arr[i];
    	}

    	else{
    		
    	}
    }

}}