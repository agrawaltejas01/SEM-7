// #include<bits/stdc++.h>
// using namespace std;

// int inv(int a, int m)		// M*d = 1 mod m
// {
// 	/*
// 	M %= m;

// 	for(int i=1; i<m; i++)
// 		if( (M*i)%m == 1 )
// 			return i;
// 	*/

// 	int m0 = m ,t,q;
// 	int x0 = 0, x1 = 1;

// 	if(m == 1)
// 		return 0;

// 	while(a > 1)
// 	{
// 		q = a/m;
		
// 	}

// }

// int main()
// {
// 	int n;
// 	cin>>n;



// 	int a[n],  m[n];
// 	long long int prod = 1;

// 	for(int i=0; i<n; i++)
// 	{
// 		cin>>a[i]>>m[i];
// 		prod *= m[i];
// 	}

// 	cout<<"IGI1\n";
	
// 	int M[n];
// 	for(int i=0; i<n; i++)
// 		M[i] = prod / m[i];

// 	cout<<"IGI2\n";

// 	int t[n];

// 	for(int i=0; i<n; i++)
// 		t[i] = inv(M[i], m[i]);

// 	cout<<"IGI3\n";

// 	int ans = 0;

// 	for(int i=0; i<n; i++)
// 		ans += a[i]*t[i]*M[i];

// 	ans %= prod;
// 	cout<<ans<<"\n";

// }



#include<bits/stdc++.h>
using namespace std;

int inv(int a, int b)
{
	if(a == 0)
		return 0;

	a %= b;

	for(int i=0; i<b ;i++)
		if((a*i)%b == 1)
			return i;
}

int main()
{
	int n;
	cin>>n;

	int a[n], m[n], M[n], t[n], prod = 1;

	for(int i=0; i<n ;i++)
	{
		cin>>a[i]>>m[i];
		prod *= m[i];
	}

	for(int i=0; i<n ;i++)
		M[i] = prod/m[i];

	for(int i=0; i<n ;i++)
		t[i] = inv(M[i], m[i]);

	int ans = 0;
	for(int i=0; i<n ;i++)
		ans += a[i]*t[i]*M[i];

	ans %= prod;
	cout<<ans<<"\n";
}