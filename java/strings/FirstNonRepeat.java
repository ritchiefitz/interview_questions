public class FirstNonRepeat {
	
	public static char nonRepeat(String word) {
		int countChar = 0;
		int i = 0;

		while(countChar != 1) {
			countChar = word.length() - word.replace(Character.toString(word.charAt(i)), "").length();
			
			if (countChar == 1) {
				break;
			}
			else if (i == word.length() - 1) {
				break;
			}

			i++;
		}

		return word.charAt(i);
	}

	public static void print(Object words) {
		System.out.println(words);
	}

	public static void main(String[] args) {
		for (String arg : args) {
			print("Original: " + arg);
			char firstChar = nonRepeat(arg);
			print("First Non Repeat: " + firstChar + "\n");	
		}
	}
}