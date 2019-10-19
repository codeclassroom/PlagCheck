class FibonacciExample1{
	public static void main(String[] args) {
        int n = 10, t1 = 0, t2 = 1;
        System.out.print("First " + n + " terms: ");
        for (int i = 1; i <= n; ++i)
        {
            System.out.print(t1 + " + ");
            int sum = t1 + t2;
            t1 = t2;
            t2 = sum;
        }
    }
	public static void main(String args[]){  
	 int n1=0,n2=1,n3,i,count=10;  
	 System.out.print(n1+" "+n2);//printing 0 and 1  
	  
	 for(i=2;i<count;++i) {//loop starts from 2 because 0 and 1 are already printed  
		  n3=n1+n2;  
		  System.out.print(" "+n3);  
		  n1=n2;  
		  n2=n3;  
	 }  
	}
}