/**
 * Student Name: Yinsheng Dong
 * Student Number: 11148648
 * NSID: yid164
 * CMPT317 A2Q1
 */

import java.util.ArrayList;

import static java.lang.Math.abs;

/**
 * A2Q1 for random_guessing algorithm
 */
public class a2q1 {


    /**
     * variable for return the final result
     */
    public static double result = 0;

    /**
     * Random guessing algorithm
     * @param problem
     * @param times
     */
    public static void random_guessing(Problem problem, int times)
    {

        ArrayList<Operation> best_operations = new ArrayList<>();
        State best_guess = new State(0,best_operations);
        problem.actions(best_guess);
        //System.out.println("The Initially best guess is: "+best_guess+", the result is: " + problem.machine_exec(best_guess.getOperations()));

        while(times!=0)
        {
            ArrayList<Operation> operations = new ArrayList<>();
            State guess = new State(0, operations);
            problem.actions(guess);

            if(abs(problem.getTarget()-problem.machine_exec(best_guess.getOperations())) >=
            abs(problem.getTarget()-problem.machine_exec(guess.getOperations())))
            {
                //System.out.println("The new guess: " +guess +" is better than best, and the result is: " +problem.machine_exec(guess.getOperations()));
                best_guess = guess;
            }
            times--;
        }


        result = problem.machine_exec(best_guess.getOperations());
    }


    /**
     * main function for testing
     * @param args
     */
    public static void main(String[] args)
    {
        String dir = "/Users/ken/IdeaProjects/CMPT317A2/src/a2_data_simple.txt";
        ArrayList<Problem> problems = ReadFile.readProblemFile(dir);
        for(Problem p : problems)
        {

            random_guessing(p, 1000);
            System.out.println("The Target Number is: "+p.getTarget());
            System.out.println("The Result Number is: "+result);
            System.out.println();
            System.out.println();
        }


    }
}
