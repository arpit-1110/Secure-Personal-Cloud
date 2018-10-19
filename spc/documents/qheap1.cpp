#include<iostream>
#include<vector>

using namespace std;

void swap(int &a, int &b){
	int temp=a;
	a=b;
	b=temp;
}

int main(){
	int q;
	cin>>q;
	int heap[100001];
	int size = 0;
	heap[0] = INT_MIN;
	while(q-->0){
		int v;
		cin>>v;
		if (v == 3){
			cout<<heap[1]<<endl;
		}
		else if (v == 1){
			int a;
			cin>>a;
			heap[size+1]=a;
			size++;
			int t=size;
			while(heap[t/2] > heap[t]){
				// cout<<"goes ";
				// cout<<heap[t/2]<<" "<<heap[t]<<endl;
				swap(heap[t/2],heap[t]);
				t=t/2;
			}

			// for (int i = 1; i <= size; ++i)
			// {
			// 	cout<<heap[i]<<" ";
			// }
			// cout<<size<<endl;
		}
		else{
			int a;
			cin>>a;
			int i;

			for (i = 0; i < 100001; ++i)
			{
				if ( heap[i] == a ){
					swap(heap[size],heap[i]);
					size--;
					break;
				}
			}

			int t=i;
			while(heap[t/2] > heap[t]){
				swap(heap[t/2],heap[t]);
				t=t/2;
			}

			while(true){
				if( (2*t > size)||(2*t+1 > size) ){
					break;
				}
				else if(heap[2*t] > heap[t] && heap[2*t+1] > heap[t]){
					break;
				}
				else{
					if(heap[2*t] > heap[t] && heap[2*t+1] < heap[t]){
						swap(heap[t],heap[2*t+1]);
						t=2*t+1;
					}
					else if(heap[2*t] < heap[t] && heap[2*t+1] > heap[t]){
						swap(heap[t],heap[2*t]);
						t=2*t;
					}
					else{
						if(heap[2*t] < heap[2*t+1]){
							swap(heap[t],heap[2*t]);
							t=2*t;
						}
						else{
							swap(heap[t],heap[2*t+1]);
							t=2*t+1;
						}
					}
				}
			}

			// for (int i = 1; i <= size; ++i)
			// {
			// 	cout<<heap[i]<<" ";
			// }
			// cout<<size<<endl;


		}
	}
}