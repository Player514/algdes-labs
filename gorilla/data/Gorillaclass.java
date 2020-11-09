import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Gorillaclass {

    HashMap<String, Integer> chars;
    int[][] blosum;
    int matrixSize;
    String[] names = new String[14];
    String[] seqs = new String[14];
    HashMap<String, Integer> nameIndex = new HashMap<>();
    String[][] path;

    HashMap<String, String[]> testMap = new HashMap<>();
    HashMap<String, String[]> resultMap = new HashMap<>();

    public static void main(String[] args) throws Exception {

        Gorillaclass gorilla = new Gorillaclass();
        gorilla.parseBlosum();
        gorilla.parseTest();
        // gorilla.runToy();
        gorilla.runReal();
        gorilla.runTest();
    }

    public void parseBlosum() throws Exception {

        InputStream stream = ClassLoader.getSystemResourceAsStream("BLOSUM62.txt");
        BufferedReader in = new BufferedReader(new InputStreamReader(stream));
        String columns = in.readLine();
        String[] charArray = columns.trim().split("\\s+");

        chars = new HashMap<>();
        matrixSize = charArray.length;
        blosum = new int[matrixSize][matrixSize];

        // make map for string/arrayindex
        for (int i = 0; i < matrixSize; i++) {
            chars.put(charArray[i], i);
        }

        // fill matrix
        for (int i = 0; i < matrixSize; i++) {
            String row = in.readLine();
            String[] rowArray = row.trim().split("\\s+");

            for (int j = 1; j < rowArray.length; j++) {
                blosum[i][j - 1] = Integer.parseInt(rowArray[j]);
            }
        }
        in.close();
    }

    void runToy() throws Exception {
        InputStream stream = ClassLoader.getSystemResourceAsStream("Toy_FASTAs-in.txt");
        BufferedReader in = new BufferedReader(new InputStreamReader(stream));

        // split names and seqs
        String name1 = in.readLine();
        String s1 = "!" + in.readLine();
        String name2 = in.readLine();
        String s2 = "!" + in.readLine();
        String name3 = in.readLine();
        String s3 = "!" + in.readLine();

        in.close();

        align(s1, s3, name1, name3);
        align(s1, s2, name1, name2);
        align(s3, s2, name3, name2);
    }

    void runReal() throws Exception {

        names = new String[14];
        seqs = new String[14];
        nameIndex = new HashMap<>();

        InputStream stream = ClassLoader.getSystemResourceAsStream("HbB_FASTAs-in.txt");
        BufferedReader in = new BufferedReader(new InputStreamReader(stream));

        // split names and seqs, add "!" in seqs for array alignment
        for (int i = 1; i < 14; i++) {
            String[] firstLine = in.readLine().trim().split("\\s+");
            String seq = "!" + in.readLine() + in.readLine() + in.readLine();

            nameIndex.put(firstLine[0].substring(1), i);
            names[i] = firstLine[0];
            seqs[i] = seq;
        }

        in.close();
       // assess("Human", "Spider");

        for (Map.Entry<String, String[]> map : testMap.entrySet())
        {
            String[] names = map.getKey().trim().split("--");
            assess(names[0], names[1]);
        }
    }

    void assess(String s1, String s2) {

        align(seqs[nameIndex.get(s1)], seqs[nameIndex.get(s2)], s1, s2);
    }

    void align(String s1, String s2, String name1, String name2) {

        int m = s1.length() - 1;
        int n = s2.length() - 1;
        int delta = -4;
        String[] s1Arr = s1.split("");
        String[] s2Arr = s2.split("");

        // Opt array A, and solution array path
        int[][] A = new int[m + 1][n + 1];
        path = new String[m + 1][n + 1];

        // fill arrays
        for (int i = 0; i < m + 1; i++)
        {
            A[i][0] = i * delta;
            path[i][0] = "down";
        }
        for (int j = 0; j < n + 1; j++)
        {
            A[0][j] = j * delta;
            path[0][j] = "left";
        }

        // find score
        for (int j = 1; j <= n; j++)
            for (int i = 1; i <= m; i++) {

                int s1Gap = delta + A[i - 1][j];
                int s2Gap = delta + A[i][j - 1];
                int penalty = penalty(s1Arr[i], s2Arr[j]) + A[i - 1][j - 1];

                // case s1Gap
                if (s1Gap >= Math.max(penalty, s2Gap))
                {
                    A[i][j] = s1Gap;
                    path[i][j] = "down";
                }

                // case s2Gap
                if (s2Gap >= Math.max(penalty, s1Gap))
                {
                    A[i][j] = s2Gap;
                    path[i][j] = "left";
                }

                // case penalty
                if ((penalty >= Math.max(s1Gap, s2Gap)))
                {
                    A[i][j] = penalty;
                    path[i][j] = "diag";
                }
            }
        System.out.println(name1 + " / " + name2 + ", Score: " + A[m][n]);

        //testTing
        String[] results = new String[3];
        String testNames = name1 + "--" + name2;
        results[0] = Integer.toString(A[m][n]);
        resultMap.put(testNames, results);
        //

        // String[] shortestString = s1Arr.length < s2Arr.length ? s1Arr : s2Arr;

        findSolution(testNames, s1Arr, s2Arr, m, n, s1Arr.length - 1, s2Arr.length -1,"", "");
    }

    void findSolution(String testNames, String[] seq1, String[] seq2, int i, int j, int seq1Index, int seq2Index, String solution1, String solution2) {

        if (i == 0 && j == 0)
        {
            // resultMap.get(testNames)[1] = solution;
            System.out.println("seq1: " + solution1);
            System.out.println("seq2: " + solution2);
			if(i == 0){
				for (int x = j; x < 0; i--) {
					solution1 = seq1[seq1Index] + solution1;
                    solution2 = seq2[seq2Index] + solution2;
				}
			}				
        }
        else
            {
            switch (path[i][j]) {
                case "diag":
                    solution1 = seq1[seq1Index] + solution1;
                    solution2 = seq2[seq2Index] + solution2;
                    findSolution(testNames, seq1, seq2, i - 1, j - 1, seq1Index - 1, seq2Index -1, solution1, solution2);
                    break;

                case "left":
                    solution1 = "-" + solution1;
                    solution2 = seq2[seq2Index] + solution2;
                    findSolution(testNames, seq1,seq2, i, j - 1, seq1Index, seq2Index-1,solution1, solution2);
                    break;

                case "down":
                    solution2 = "-" + solution2;
                    solution1 = seq1[seq1Index] + solution1;
                    findSolution(testNames, seq1, seq2, i - 1, j, seq1Index-1, seq2Index, solution1, solution2);
                    break;
            }
        }

    }

    int penalty(String a, String b) {
        return blosum[chars.get(a)][chars.get(b)];
    }

    void parseTest() throws Exception {

        InputStream stream = ClassLoader.getSystemResourceAsStream("HbB_FASTAs-out.txt");
        BufferedReader in = new BufferedReader(new InputStreamReader(stream));

        for (int i = 1; i < 79; i++) {
            String testArr[] = new String[3];

            String[] nameAndScore = in.readLine().trim().split(": ");

            testArr[0] = nameAndScore[1];
            testArr[1]= in.readLine();
            testArr[2] = in.readLine();

            testMap.put(nameAndScore[0], testArr);
        }
        in.close();
    }

    void runTest()
    {
        // problemer med sea-cucumber, lamprey og deer/gull.. ?
        for (Map.Entry<String, String[]> map : testMap.entrySet())
        {
            String testNames = map.getKey();
            String testScore = map.getValue()[0];
            String testSeq1 = map.getValue()[1];
            String testSeq2 = map.getValue()[2];
            String score = resultMap.get(testNames)[0];
            String seq = resultMap.get(testNames)[1];

            System.out.println(testNames);
            System.out.println("Score: " + (testScore.equals(score) ? "OK" : "Nope: " + testScore + "/" + score));
            System.out.println("Seq: " + ((testSeq1.equals(seq) || testSeq2.equals(seq)) ? "OK" : "Nope : \n" +
                    "testSeq 1: " + testSeq1 + "\n" + "testSeq2: " + testSeq2 + "\n" + "resultSeq: " + seq));
        }
    }
}