/*import java.util.*;
import java.math.*;
import java.security.*;

public class SHA_test
{

	public static String encrypt(String input)
	{
		try
		{
			MessageDigest md = MessageDigest.getInstance("SHA-1");
			byte[] msgdigest = md.digest(input.getBytes());

			BigInteger big = new BigInteger(1, msgdigest);

			String hash = big.toString(16);

			while(hash.length() < 32)
			{
				hash = "0" + hash;
			}
			return  hash;
		}

		catch(NoSuchAlgorithmException e)
		{
			throw new RuntimeException(e);
		}
	}

	public static void main(String Args[]) throws NoSuchAlgorithmException
	{
		Scanner in = new Scanner(System.in);
		System.out.println("Enter a String to Encode : ");

		String input = in.next();
		System.out.println("\n" + "Encrypted string is : " + encrypt(input));
	}
}
*/

// import java.util.*;
// import java.security.*;
// import java.math.*;

// public class SHA_test
// {
// 	public static String encrypt(String input)
// 	{
// 		try
// 		{
// 			MessageDigest md = MessageDigest.getInstance("SHA-1");
// 			byte[] message_digest = md.digest(input.getBytes());

// 			BigInteger no = new BigInteger(1, message_digest);

// 			String hash = no.toString(16);

// 			while(hash.length() < 16)
// 				hash = "0" + hash;

// 			return hash;
// 		}

// 		catch(NoSuchAlgorithmException e)
// 		{
// 			throw new RuntimeException(e);
// 		}
// 	}

// 	public static void main(String Args[]) throws NoSuchAlgorithmException
// 	{
// 		Scanner in = new Scanner(System.in);
// 		System.out.println("Enter a String : ");

// 		String input = in.next();
// 		System.out.println("Encrypted string is : " + encrypt(input));

// 	}
// }

import java.util.*;
import java.security.*;
import java.math.*;

public class SHA_test
{

	public static String encrypt(String input)
	{
		try
		{
			MessageDigest md = MessageDigest.getInstance("SHA-1");
			byte[] message_digest = md.digest(input.getBytes());

			BigInteger no = new BigInteger(1, message_digest);

			String hash = no.toString(16);

			while(hash.length() < 32)
				hash = "0" + hash;

			return hash; 
		}

		catch(NoSuchAlgorithmException e)
		{
			throw new RuntimeException(e);
		}
	}

	public static void main(String Ards[])	throws NoSuchAlgorithmException
	{
		Scanner in = new Scanner(System.in);
		System.out.println("String : ");

		String input = in.next();
		System.out.println(encrypt(input));
	}
}