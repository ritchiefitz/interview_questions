public class StripWhitespace {
	
	public static void print(Object words) {
		System.out.println(words);
	}

	public static void main(String[] args) {
		String newString = "\n\nThis \tString\n is nuts   ";
		String[] removeItems = {"\n", "\t"};
		
		print("Original: " + newString);

		for (String removeItem : removeItems) {
			newString = newString.replace(removeItem, "");
		}
		
		print("Stripped: " + newString.trim() + "\n");
	}
}