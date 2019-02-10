import java.util.*;

class Shivanee
{
  public static void main(String args[])
  {
    int t,n,h,k;
    Vector <Integer> a = new Vector <Integer> ();
    Scanner sc = new Scanner(System.in);
    t = sc.nextInt();
    for(int i=0;i<t;i++)
    {
      a.clear(); //clear previous input
      int start=1,end;
      k=-1;
      n = sc.nextInt();
      h = sc.nextInt();
      for(int j=0;j<n;j++)
        a.add(sc.nextInt());
      end = 1000000001; //max val
      while(start<end) //find k using binary search
      {
        int mid = (start+end)/2;
        if(isSoln(a,mid,h)) //check if k = mid satisfies or not 
        end = mid;
        else
        start = mid+1;
      }
      if(isSoln(a,start,h))
      k = start;
      System.out.println(k);
    }
  }
  public static boolean isSoln(Vector <Integer> v,int k,int h)
  {
    int sum =0; //time required to eat
    for(int i=0;i<v.size();i++)
    {
      sum += (int)Math.ceil((double)v.get(i)/k); //ceil for upper limit
    }
    if (sum <=h)
    return true; //possible
    else
    return false; 
  } 
}