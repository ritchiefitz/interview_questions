public class ReverseString {

	// Long Way
	// public static String reverse(String original) {
	// 	int size = original.length() - 1;
	// 	String reversed = "";

	// 	for (int i = size; i >= 0; i--) {
	// 		reversed += original.charAt(i);
	// 	}

	// 	return reversed;
	// }
	
	public static void print(Object words) {
		System.out.println(words);
	}

	public static void main(String[] args) {
		for (String arg : args) {
			print("Original: " + arg);
			print("Reversed: " + new StringBuilder(arg).reverse() + "\n");	
		}
	}
}