import java.util.*;

class Shivanee
{
  public static void main(String args[])
  {
    int t,n,count,i,j,p,q;
    Scanner sc = new Scanner(System.in);
    Vector <Integer> v = new Vector <Integer>();
    Vector <Integer> soln = new Vector <Integer>(); 
    for(i=0;i<=10000;i++)
    {
      v.add(i); //will store all prime numbers 
      soln.add(0);  //will store number of pairs of solution
    } 
    //remove 0 and 1 because not prime
    v.removeElement(0); 
    v.removeElement(1);
    //using sieve of eratosthenes update list of prime numbers
    for(i=2;i*i<=10000; i++) 
    { 
      if(v.contains(i)) 
      {            
        for(j=i*i;j<=10000;j+=i) 
          v.removeElement(j); //remove if not prime
      } 
    }  
    for(p=0;p<v.size();p++)
    {
      for(q=0;q<v.size();q++)
      {
        int index = v.get(p) + 2*v.get(q);
        if(index<=10000)
        soln.set(index,soln.get(index)+1); //update no of possible soln
      }
    } 
    t = sc.nextInt();
    for(i=0;i<t;i++)
    {
      n = sc.nextInt();
      System.out.println(soln.get(n));
    }
  }
}