/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Sangram
{
 public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    int t=sc.nextInt();
  while(t-->0)
  {
    int n,h,s=0,l=1,r=0,mid=0,max=0;
      n=sc.nextInt();
      h=sc.nextInt();
    int a[]=new int[n];
    for(int i=0;i<n;i++)
    {
      a[i]=sc.nextInt();//inpute
      if(a[i]>max)
        max=a[i];
    }
  r=max;
    while(true)
    {
      mid=(int)Math.ceil(((double)(l+r))/2);
       int sum=0; 
     for(int i=0;i<n;i++)
     {
        sum+=(int)Math.ceil((double)a[i]/mid);//hr total by mid
        if(sum>h)
        {
          break;
        }
     }
     if(l>=r)
     {
       System.out.println(l);break;
     }
     if(sum>h)
     {
       l=mid;
     }
     else{
         s=0;
         for(int i=0;i<n;i++)
         {
            s+=(int)Math.ceil((double)a[i]/(mid-1));
         }
         if(s>h)
         {
           System.out.println(mid);
           break;
         }
         else{
           r=mid;
         }
     }
      
    }
   
    }
  
  }  
}