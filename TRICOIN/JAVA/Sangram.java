/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Sangram
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
    Scanner sc=new Scanner(System.in);
    int t=sc.nextInt();
    while(t-->0){
      int n=sc.nextInt();
      int h=1;
      while((h*(h+1))/2<=n){
        h++;
      }
      System.out.println(h-1);
    }
	}
}