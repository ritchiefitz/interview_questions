public class RemoveDuplicate {

	public static String removeDuplicates(String original) {
		String unique = "";

		for (char c : original.toCharArray()) {
			if (unique.indexOf(c) == -1) {
				unique = unique + c;
			}
		}

		return unique;
	}
	
	public static void print(Object words) {
		System.out.println(words);
	}

	public static void main(String[] args) {
		for (String arg : args) {
			print("Original: " + arg);
			String removed = removeDuplicates(arg);
			print("Removed Duplicates: " + removed + "\n");	
		}
	}
}