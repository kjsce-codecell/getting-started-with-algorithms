import java.util.*;
class Sangram{
    static boolean[] prime=new boolean[10001];    
    static int ans[]=new int[10001];//count array 
    public static void make(){
        /*prime calculation*/
        int len=prime.length;
        for(int i=0;i<len;i++){
          prime[i]=true;
        }
        for(int i=2;i<prime.length;i++){
          if(prime[i]){
            for(int j=i*i;j<prime.length;j=j+i){
              prime[j]=false;
            }
          }
        }
        /*prime calculation*/
        for(int p=2;p<len;p++){
          for(int q=2;q<len;q++){
            //if p and q both are prime and the condition is true add count
            if (prime[p] && prime[q] && (p+2*q)<len) 
              ans[p+2*q]++;
          } 
        }
    }
  public static void main(String args[]){
    Scanner sc=new Scanner(System.in);
    make();
    int t=sc.nextInt();
    while(t-->0){
    System.out.println(ans[sc.nextInt()]);
    }
  }
}