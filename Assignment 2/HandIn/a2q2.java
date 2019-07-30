/**
 * Student Name: Yinsheng Dong
 * Student Number: 11148648
 * NSID: yid164
 * CMPT317 A2Q2
 */

import java.util.ArrayList;
import java.util.Random;

import static java.lang.Math.abs;

/**
 * a2q2 for implement the random search strategy
 */
public class a2q2 {

    /**
     * the result return
     */
    public static double result = 0;


    /**
     * return a neighbour state randomly
     * @param state
     * @param problem
     * @return a random neighbour state
     */
    public static State neighbourState(State state, Problem problem)
    {
        ArrayList<Operation>betterOperation = new ArrayList<>();
        State neighbour = null;
        int random_range = state.getOperations().size();
        Random random = new Random();
        int random_index = random.nextInt(random_range);
        neighbour = new State(0, betterOperation);
        double x = state.getOperations().get(random_index).getOperand();
        for(Operation o : state.getOperations())
        {
            neighbour.addOperation(o);
        }
        neighbour.getOperations().set(random_index, new Operation(problem.getRandomAction(), x));
        if(state == neighbour)
        {
            return neighbourState(state, problem);
        }
        return neighbour;

    }

    /**
     * The random search strategy
     * @param problem
     * @param times
     */
    public static void random_search(Problem problem, int times)
    {
        ArrayList<Operation> best_operation = new ArrayList<>();
        State best_guess = new State(0, best_operation);
        problem.actions(best_guess);

        //System.out.println("The initial best guess is: " + best_guess +", the result is: "+problem.machine_exec(best_guess.getOperations()));
        int i = 0;

        State state = best_guess;
        while (i < times) {
            State neighbour = neighbourState(state,problem);
            if (abs(problem.getTarget() - problem.machine_exec(state.getOperations())) >
                    abs(problem.getTarget() - problem.machine_exec(neighbour.getOperations()))) {
                //System.out.println("Found the better neighbour: "+ neighbour +", the result is: " + problem.machine_exec(neighbour.getOperations()));
                state = neighbour;
            }
            i++;
        }
        best_guess = state;
        result = problem.machine_exec(best_guess.getOperations());



    }

    /**
     * For testing
     * @param arg
     */
    public static void main(String arg[])
    {

        String dir = "/Users/ken/IdeaProjects/CMPT317A2/src/a2_data_simple.txt";
        ArrayList<Problem> problems = ReadFile.readProblemFile(dir);
        int i = 0;
        for(Problem p : problems)
        {

            System.out.println("Test "+i+": ");
            random_search(p, 1000);
            System.out.println("The Target Number is: "+p.getTarget());
            System.out.println("The Result Number is: "+ result);
            System.out.println();
            i++;
        }


    }
}
