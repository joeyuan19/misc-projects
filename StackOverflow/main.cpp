
#include <iostream>
using namespace std;


int main(){
	/*
	vector<int> = {1,2,3,4};
	vector<int> = {5,6,7,8};
	
	arrPtr[0] = arr;
	arrPtr[1] = arr2;

	for (int * a : arrPtr ){
		for (int i : a){
			cout << i << endl;
		}
	}
	*/
	vector<int> vec;
	vec.push_back( 1 );
	vec.push_back( 2 );
	 
	for (int& i : vec ) 
	{
		    i++; // increments the value in the vector
	}
	for (int i : vec )
	{
		    // show that the values are updated
			cout << i << endl;
		}
}


