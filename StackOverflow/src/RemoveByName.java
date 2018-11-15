import java.util.ArrayList;


public class RemoveByName {
	public static void main(String args[]) {
		ArrayList<String> arr = new ArrayList<String>();
		arr.add("Bob");
		System.out.println(arr.size());
		arr.remove("Bob");
		System.out.println(arr.size());
	}
}
