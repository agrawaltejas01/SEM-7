// #include<bits/stdc++.h>
// using namespace std;

// #define lli long long int

// lli gcd(lli a, lli b)
// {
// 	lli temp;

// 	while(1)
// 	{
// 		temp = b%a;

// 		if(!temp)
// 			return b;

// 		a = b;
// 		b = temp;
// 	}

// }

// lli fpow(lli m, lli p, lli mod)
// {
// 	lli res = 1;

// 	m %= mod;

// 	while(p)
// 	{
// 		if(p & 1)
// 			res = res * m % mod;

// 		p /=2 ;

// 		m = m*m%mod;
// 	}

// 	return res;
// }

// int main()
// {
// 	lli p,q;
// 	p = 101, q = 97;

// 	lli n = p*q;

// 	lli phi = (p-1)*(q-1);

// 	lli e = 2;

// 	while( e < phi )
// 	{
// 		if(gcd(e,phi) == 1)
// 			break;

// 		e++;
// 	}

// 	lli k = 1;

// 	while( (1 + k*phi) % e != 0 )
// 		k++;

// 	lli d = (1 + k*phi)/e;

// 	lli msg = 450;

// 	lli c = fpow(msg, e, n);
// 	cout<<c<<"\n";

// 	lli ans = fpow(c, d, n);
// 	cout<<ans<<"\n";

// }

// #include<bits/stdc++.h>
// using namespace std;
// #define lli long long int 

// lli gcd(lli e, lli phi)
// {
// 	lli temp ;

// 	while(1)
// 	{
// 		temp = e % phi;

// 		if(temp == 0)
// 			return phi;

// 		e = phi;
// 		phi = temp;
// 	}

// 	return e;
// }

// lli fpow(lli msg, lli pow, lli mod)
// {
// 	lli res = 1;

// 	msg %= mod;

// 	while(pow)
// 	{
// 		if(pow & 1)
// 			res = res * msg % mod;

// 		pow /= 2;

// 		msg = msg * msg % mod;
// 	}

// 	return res;
// }

// int main()
// {
// 	lli p=13, q=11;
// 	lli n = p*q;

// 	lli phi = (p-1)*(q-1);

// 	lli e = 2;

// 	while( e < phi )
// 	{
// 		if(gcd(e,phi) == 1)
// 			break;

// 		e++;
// 	}

// 	lli k = 1;

// 	while( (1 + k*phi)%e != 0 )
// 		k++;

// 	lli d = (1 + k*phi) / e;

// 	lli msg = 24;

// 	lli encrypt = fpow(msg, e, n);
// 	cout<<encrypt<<"\n";

// 	lli decrypt = fpow(encrypt, d, n);
// 	cout<<decrypt<<"\n";

// }




#include<bits/stdc++.h>
using namespace std;

int gcd(int a,int b)
{
	int temp = 1;
	while(1)
	{
		temp = a%b;

		if(temp == 0)
			return b;

		a = b;
		b = temp;
	}
}

int fpow(int msg, int pow, int mod)
{
	int res = 1;

	msg %= mod;

	while(pow)
	{
		if(pow & 1)
			res = res * msg % mod;

		pow /= 2;

		msg = msg * msg % mod;
	}

	return res;

}

int main()
{
	int p=11, q = 13;
	int n = p*q;
	int phi = (p-1)*(q-1);

	int e = 2;

	while(1)
	{
		if(gcd(e,phi) == 1)
			break;

		e++;
	}

	int k = 1;
	while((1+k*phi)%e != 0)
		k++;

	int d = (1+k*phi)/e;

	int msg = 15;

	int encrypt = fpow(msg, e, n);
	int decrypt = fpow(encrypt, d, n);

	cout<<msg<<endl<<encrypt<<endl<<decrypt<<endl;
}