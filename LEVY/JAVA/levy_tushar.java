import java.util.*;
class levy_tushar{
    static int[] ans = new int[10001];
    static ArrayList<Integer> prime;
    public static void main(String arhs[]) {
        Scanner sc= new Scanner(System.in);
       
        //Preprocessing 
        prime =sieve(10000);
        countThem();    
        int t=sc.nextInt();
        

        while(t-->0)    System.out.println(ans[sc.nextInt()]);

            
    }
    // Counting nC2 pairs of primes such that p+2q 
    static void countThem(){
        int sz= prime.size();
        for(int i=0;i<sz;++i){
            for(int j=0;j<sz;++j){
                int val = prime.get(i)+2*prime.get(j);
                if(val<=10000) ans[val]++;
            }
        }
    }

    //Sieve Code for finding primes
    static ArrayList<Integer> sieve(int n){
        ArrayList<Integer> al=new ArrayList<>();
            boolean prime[] = new boolean[n+1];
            for(int i=0;i<n;i++)
                prime[i] = true;
        for(int p = 2; p*p <=n; p++)
          {
             if(prime[p])
              {
                  for(int i = p*2; i <= n; i += p)
                   prime[i] = false;
              }
           }
       for(int i = 2; i <= n; i++)
       {
          if(prime[i] == true) 
              al.add(i);
       }
         return al;
            
       }
}