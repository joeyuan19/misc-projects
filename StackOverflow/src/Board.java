
import java.io.*;

public class Board<T extends Cell<TT>, TT> {
	T cells;
	public Board(T cells) {
		this.cells = cells;
	}
	public static String intersections(String line) {
        String out = "", buf = "";
        int idx = line.lastIndexOf(";"), i, j, last = idx + 1;
        for (i = 0; i < idx; i++) {
            if (line.charAt(i) == ',') {
                for (j = last; j < line.length()-buf.length(); j++) {
                    if (line.substring(j,j+buf.length()).equals(buf)) {
                        out += buf + ",";
                        last = j+buf.length();
                        break;
                    }
                }
                buf = "";
            } else {
                buf += line.charAt(i);
            }
        }
        for (j = idx+1; j < line.length()-buf.length(); j++) {
            if (line.substring(j,j+buf.length()).equals(buf)) {
                out += buf + ",";
            }
        }
        if (out.length() > 0) {
            out = out.substring(0,out.length()-1);
        }
        return out;
    }
	public static void main(String[] args) {
		String s = "abcdefghijklmnop";
		System.out.println(s.substring(1, 1+2));
	}
}