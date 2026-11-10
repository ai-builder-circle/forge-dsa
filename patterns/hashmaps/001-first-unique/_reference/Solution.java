import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String s = in.readLine();
        if (s == null) s = "";
        s = s.trim();
        Map<Character, Integer> counts = new HashMap<>();
        for (char c : s.toCharArray()) counts.merge(c, 1, Integer::sum);
        int answer = -1;
        for (int i = 0; i < s.length(); i++) {
            if (counts.get(s.charAt(i)) == 1) { answer = i; break; }
        }
        System.out.println(answer);
    }
}
