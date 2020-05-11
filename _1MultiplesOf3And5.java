
public class _1MultiplesOf3And5 {
	public static void main(String[] args) {
		solve();
	}
	public static void solve() {
		//variable to total result
		int sum = 0;
		
		//loop iterates from 0-999 inclusive
		for (int i = 0; i < 1000 ; i++ ) {
			//increment only if a multiple of 3 or 5
			if ( i % 3 == 0 || i % 5 == 0 ) {
				sum += i;
			}
		}
		System.out.println(sum);
	}
}
