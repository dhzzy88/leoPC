#include<iostream>
#include<algorithm>
#include<fstream>
int main1()
{
	using namespace std;
	int a =10;
	int *np =&a;
        cout<<a<<"\n"<<np<<'\n'<<*np<<'\n';
	cout<<"yinyongleixing\n";
	int& a1=a;
	a =18;
        cout<<a1<<'\n';
	fstream outfile("a.out",ios::out);
	if (!outfile){
		cout<<"can't open file:a.out\n"<<endl;
		return 0;
	}
	outfile<<"file"<<endl;
	outfile<<endl;
        cout<<"----------------------------------------"<<endl;
	char ch;
	ch ='A';
        cout<<ch<<endl;
	cout<<"-----------------selection sort-----------------------"<<endl;
        int numbers1[10]={1,3,2,4,5,8,5,6,9,0};
	for(int i=0;i<10;i++){
		int j=i;
		for(int k=i+1;k<10;k++){
			if(numbers1[j]>numbers1[k]){
				j=k;
				swap(numbers1[i],numbers1[j]);
			}
		} 
	}
	for(int i=0;i<10;i++){
		cout<<numbers1[i]<<" ";
	}
	cout<<"\n"<<"------------------------------bisearch---------"<<endl;
	int left=0;
	int right=10-1;
	int x=4;
	int numbers2[10]={1,3,2,4,5,8,5,6,9,0};
	while (left<right){
		int middle =(left+right)/2;
		if(x<numbers2[middle]){
			right =middle-1;
		}else if(x>numbers2[middle]){
			left =middle+1;
		}else{
			break;
		}
	}
	cout<<"-------\n";
        for(int i=0;i<10;i++){
			cout<<numbers2[i]<<" ";
		}
	return 0;
}

int numbers[10]={1,3,2,6};
int iterative(int *a,const int x,const int left,const int right){
	std::cout<<"-------------------recursive----------------"<<std::endl;
	if(left<right){
		int middle=(left+right)/2;
		if(x<middle) return iterative(a,x,left,middle-1);
		else if(x>middle) return iterative(a,x,middle+1,right);
		else return middle;
	}
	return 1;
}
        
void  Permutations(int *a,const int k,const int m){
	if(k==m){
		for(int i=0;i<=m;i++) std::cout<<a[i]<<" ";
		std::cout<<std::endl;
	}
	else{
		for(int i =k;i<=m;i++){
			std::swap(a[k],a[i]);
		        Permutations(a,k+1,m);
			std::swap(a[k],a[i]);
		}
	}
}







int main(){
     using namespace std;
                                              

}




