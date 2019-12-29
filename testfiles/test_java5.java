public class computeFibonacci {
 
	public static void main(String[] args) 
	{
		 int maxNr = 10; 
		 int previousNumber = 0;
		 int nextNumber = 1;
		 
	        System.out.print("Fibonacci Series of "+maxNr+" numbers:");
 
	        for (int i = 1; i <= maxNr; ++i)
	        {
	            System.out.print(previousNumber+" ");
	            int sum = previousNumber + nextNumber;
	            previousNumber = nextNumber;
	            nextNumber = sum;
	        }
 
	}
 
}