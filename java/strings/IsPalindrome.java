public class IsPalindrome {

	public static String isPalindrome(String original) {
		return ((original.equals(new StringBuilder(original).reverse())) ? "True" : "False");
	}
	
	public static void print(Object words) {
		System.out.println(words);
	}

	public static void main(String[] args) {
		for (String arg : args) {
			print("Original: " + arg);
			print("Reversed: " + new StringBuilder(arg).reverse());
			print("Palindrome: " + isPalindrome(arg) + "\n");
		}
	}
}