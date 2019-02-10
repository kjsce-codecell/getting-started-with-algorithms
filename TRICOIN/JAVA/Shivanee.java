import java.util.*;

class Shivanee
{
  public static void main(String args[])
  {
    int t,n;
    Scanner sc = new Scanner(System.in);
    t = sc.nextInt();
    for(int i=0;i<t;i++)
    {
      n = sc.nextInt();
      int lvl = 1;
      //sum of natural numbers = n(n+1)/2
      //find lvl such that the coins required to fill upto that lvl is less or equal to n
      while(((lvl+1)*lvl/2)<=n)
      lvl++;
      System.out.println(--lvl);
    } 
  }
}
