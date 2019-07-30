/**
 * Student Name: Yinsheng Dong
 * Student Number: 11148648
 * NSID: yid164
 * CMPT317 A2Q4
 */

import java.util.ArrayList;
import static java.lang.Math.abs;

public class a2q4 {

    public static double result;
    public static void random_restart_hill_climbing_search(Problem problem, int restart, int step)
    {

        ArrayList<Operation> best_operation = new ArrayList<>();
        State best_guess = new State(0, best_operation);
        problem.actions(best_guess);
        int t = 0;
        result = 0;
        //System.out.println("The initially guess: " + best_guess +", the result is: "+problem.machine_exec(best_guess.getOperations()));
        while(t<restart)
        {
            a2q3.hill_climbing_search(problem,step);
            if (abs(problem.getTarget() - result) >
                    abs(problem.getTarget() - a2q3.result)) {
                result = a2q3.result;
            }
            t++;
        }

        //System.out.println(result);


    }

    public static void main(String [] args)
    {
        String dir = "/Users/ken/IdeaProjects/CMPT317A2/src/a2_data_simple.txt";
        ArrayList<Problem> problems = ReadFile.readProblemFile(dir);
        int i = 0;
        for(Problem p : problems)
        {

            System.out.println("Test "+i+": ");
            random_restart_hill_climbing_search(p,50,20);
            System.out.println("The Target Number is: "+p.getTarget());
            System.out.println("The Result Number is: "+ result);
            System.out.println();
            i++;
        }
    }
}
