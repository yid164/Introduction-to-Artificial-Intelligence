import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class ReadFile {
    //ArrayList<Problem> problems;

    public static ArrayList<Problem> readProblemFile(String dir)
    {
        ArrayList<Double> given_list = null;
        double target = 0;
        ArrayList<Problem> problems = new ArrayList<>();

        File file = new File(dir);
        Scanner scanner = null;

        try{
            scanner = new Scanner(file);
            while(scanner.hasNext())
            {
                given_list = new ArrayList<>();
                String words [] = scanner.nextLine().split(" ");
                target = Double.parseDouble(words[0]);
                for ( int i = 1; i< words.length; i++)
                {
                    given_list.add(Double.parseDouble(words[i]));
                }
                problems.add(new Problem(target, given_list));

            }

        }catch (FileNotFoundException fe)
        {
            System.out.println(fe.fillInStackTrace());
        }

        return problems;

    }
}
