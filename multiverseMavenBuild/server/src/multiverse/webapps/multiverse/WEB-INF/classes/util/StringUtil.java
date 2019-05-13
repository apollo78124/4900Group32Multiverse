
public final class StringUtil {

    public static boolean isNumber(char digit) {
        if (digit >= '0' && digit <= '9') {
            return true;
	}
	return false;
    }

    public static boolean isLetter(char letter) {
        if (letter >= 'a' && letter <= 'z' ||
	    letter >= 'A' && letter <= 'Z') {
            return true;
	}
	return false;
    }
}

