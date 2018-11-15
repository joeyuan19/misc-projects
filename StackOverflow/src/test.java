import java.awt.Color;
import java.lang.reflect.Field;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class test {
	public static String getColorName(int r, int g, int b) {
		String[] colorNames = new String[] {
				"BLACK",
				"BLUE",
				"GREEN",
				"CYAN",
				"DARK_GRAY",
				"GRAY",
				"LIGHT_GRAY",
				"MAGENTA",
				"ORANGE",
				"PINK",
				"RED",
				"WHITE",
				"YELLOW"
		};
		Color userProvidedColor = new Color(r,g,b);
		Color color;
		Field field;
		for (String colorName : colorNames) {
			try {
				field = Class.forName("java.awt.Color").getField(colorName);
				color = (Color)field.get(null);
				if (color.equals(userProvidedColor)) {
					return colorName; // Or maybe return colorName.toLowerCase() for aesthetics
				}
			} catch (Exception e) {
				
			}
		}
		Color someOtherCustomDefinedColorMaybePurple = new Color(128,0,128);
		if (someOtherCustomDefinedColorMaybePurple.equals(userProvidedColor)) {
			return "Purple";
		}
		
		return "Undefined";
	}
	public static int findFirstLetterPosition(String input) {
	    for (int i = 0; i < input.length(); i++) {
	        if (Character.isLetter(input.charAt(i))) {
	            return i;
	        }
	    }
	    return -1; // not found
	}
	static int iterat(int m) {
        int afterall=0;  
        int last=1;
        int penultimate=1;
    
        for (int j=3;j<=m;j++) {
    
            int thisone = ((6*j-3)*(last)-(j-2)*(penultimate))/(j+1);
            
            penultimate = last;
            last = thisone;
            afterall=thisone;
    
        }
        return afterall;
    }
	public static int manualDecode(String s) throws NumberFormatException {
        Pattern p = Pattern.compile("\\d+L");
        Matcher m = p.matcher(s);
        if (m.matches()) {
            return Integer.decode(s.substring(0,s.length()-1));
        }
        p = Pattern.compile("(\\d{1,3})_((\\d{3})_)*?(\\d{3})");
        m = p.matcher(s);
        if (m.matches()) {
        	String reformattedString = "";
        	char c;
        	for (int i = 0; i < s.length(); i++) {
        		c = s.charAt(i);
        		if ( c >= '0' && c <= '9') {
        			reformattedString += c;
        		}
        	}
            return Integer.decode(reformattedString);
        }
        throw new NumberFormatException();
    }
	static class Car {
		int n;
		public Car(int n) {
			this.n = n;
		}
		public int getCarNum() { return this.n; }
	}
	public static void printCars(Car[] cars) {
		String out = "";
		for (Car c : cars) {
				out += c != null ? c.getCarNum() + "," : "null,";
		}
		System.out.println(out);
	}
	
	public static void main(String[] args) {
		int CarNum = 1;
		int[] carNums = new int[] {5,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5};
		Car[] cars = new Car[100];
		int index = 0;
		for (int i : carNums) {
			cars[index++] = new Car(i);
		}
		int noOfCars = index;
		System.out.println("Before:");
		System.out.println("Cars: " + noOfCars);
		printCars(cars);
//		for (int i = 0; i < cars.length; i++) {
//		    if (cars[i] != null && cars[i].getCarNum() == CarNum) {
//		        for (int j = i+1; j < cars.length; j++) { // This loop will shift the 
//		            cars[j-1] = cars[j];             // whole list down one when
//		        }                                              // a duplicate is found,
//		                                                       // overwriting it.
//		        i--;              // sets the index back to recheck the shifted list.
//		        noOfCars--;  // You removed one duplicate by overwriting it
//		    }
//		}
		int nextIndex = 0;
		for (int i = 0; i < cars.length; i++) {
		    if (cars[i] != null && cars[i].getCarNum() == CarNum) {
		    } else {
		    	cars[nextIndex++] = cars[i];
		    }
		    if (nextIndex < i) {
		    	cars[i] = null;
		    }
		}
		System.out.println();
		System.out.println("After:");
		System.out.println("Cars: " + noOfCars);
		printCars(cars);
	}
}
