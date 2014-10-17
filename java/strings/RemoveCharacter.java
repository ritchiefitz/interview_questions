public class RemoveCharacter {
	
	public static void print(Object words) {
		System.out.println(words);
	}

	public static void main(String[] args) {
		print("Original: " + args[1]);
		print("Reversed: " + args[1].replace(args[0], "") + "\n");
	}
}