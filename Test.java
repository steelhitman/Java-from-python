import java.io.*;
import java.util.Random;
class Test
{
	public static void main(String args[]) throws IOException
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		Random rand = new Random();
		int n = rand.nextInt(3);
		String arr[]={"123","123.45","abc"};
		System.out.println(arr[n]);
	}
}