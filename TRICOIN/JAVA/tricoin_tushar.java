import java.util.*;
class tricoin_tushar{
    public static void main(String arsg[]){
        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int num=sc.nextInt();
            //  lowest postive integer near positve of root of quadratic equation (-b + sqrt( b^2 - 4ac )/2a is the answer ! 
            int ans=(int)((-1.0+Math.sqrt(1+8.0*num))/2.0);
            System.out.println(ans);
        }
    }
}
