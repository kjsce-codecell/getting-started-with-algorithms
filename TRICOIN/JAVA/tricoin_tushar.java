import java.util.*;
class tricoin_tushar{
    public static void main(String arsg[]){
        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int num=sc.nextInt();
            int ans=(int)((-1.0+Math.sqrt(1+8.0*num))/2.0);
            System.out.println(ans);
        }
    }
}