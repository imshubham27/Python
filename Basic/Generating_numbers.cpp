#include <iostream>

using namespace std;

int main()
{
    int sum;
    cout<<"Enter the sum: ";
    cin>>sum;
    int arr[4];
    int s=0;
    int i=0;
    while(i<4)
    {
        arr[i]=rand()%int((sum/2)+1);
        // cout<<arr[i];
        s=s+arr[i];
        // cout<<" I "<<i;
        // cout<<" S "<<s;
        if(s>sum)
        {
            arr[i]=sum-(s-arr[i]);
            break;
        }
        i=i+1;
    }
    // cout<<"S"<<s;
    if(s<sum)
    {  
        arr[3]=sum-(s-arr[3]);
    }
    
    for(i=0;i<4;i++){
        if(arr[i]>sum){
            arr[i]=0;
        }
        cout<<arr[i];
        cout<<'\n';
    }
    return 0;
}