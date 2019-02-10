import java.util.*;
class mineat{
    static int n,h,t;
    static int[] arr;
    public static void main(String args[]){
        Scanner sc= new Scanner(System.in);
       
       // Input Here
        t=sc.nextInt();
        while(t-->0){
        n=sc.nextInt();h=sc.nextInt();
        arr=new int[n];
        for(int i=0;i<n;++i) arr[i]= sc.nextInt();
        
        //Output here
        //Doing binary search on K 
        System.out.println(bs());

        }
    }

    static int bs(){
    // Copy pasted Binary Search
    int e= (int)1e9+1,s=1;
    int m=(s+e)/2;
    while(s<e){
      
        m=(s+e)/2;
        if(check(m)) e=m;
        else s=m+1;
    }

    if(check(s)) return s;
    return -1;
    }
    
    static boolean check(int eatingCapacity){
        //Checking if given eatingCapcity works or not 
        int hoursReq = 0;
        for(int i=0;i<n;++i){
            int extra= arr[i]%eatingCapacity>0?1:0;
            hoursReq += arr[i]/eatingCapacity + extra;   
        }
       
        return hoursReq<=h;
    }
}