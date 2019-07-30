/**
 * Student Name: Yinsheng Dong
 * Student Number: 11148648
 * NSID: yid164
 * CMPT317 A2Q3
 */

import java.util.ArrayList;
import static java.lang.Math.abs;

/**
 * A2Q3 for implementation of hill_climbing search algorithm
 */
public class a2q3 {

    /**
     * the result number out put the best one
     */
    public static double result = 0;

    /**
     *
     * @param state
     * @param problem
     * @return best neighbour state
     */
    public static State bestNeighbourState(State state, Problem problem)
    {
        ArrayList<Operation> betterOperation =  new ArrayList<>();
        State best = new State(0, betterOperation);
        for (Operation o : state.getOperations())
        {
            best.addOperation(o);
        }

        int count_start = 0;
        int count_end = state.getOperations().size();

        while (count_start < count_end)
        {

            double x = best.getOperations().get(count_start).getOperand();

            Operation operation = new Operation(problem.getRandomAction(),x);
            best.getOperations().set(count_start, operation);

            if (abs(problem.getTarget() - problem.machine_exec(state.getOperations())) >
                    abs(problem.getTarget() - problem.machine_exec(best.getOperations()))) {
                state = best;
                //System.out.println(best);
            }

            count_start++;
        }


        return state;

    }

    /**
     * The hill_climbing search algorithm
     * @param problem
     * @param times
     */
    public static void hill_climbing_search(Problem problem, int times) {
        ArrayList<Operation> best_operation = new ArrayList<>();
        State best_guess = new State(0, best_operation);
        problem.actions(best_guess);

        int i = 0;
        State state = best_guess;
        while (i<times)
        {

            State bestNeighbourState = bestNeighbourState(best_guess,problem);
            if (abs(problem.getTarget() - problem.machine_exec(state.getOperations())) >
                    abs(problem.getTarget() - problem.machine_exec(bestNeighbourState.getOperations()))) {
                //System.out.println("Find the better one: "+ bestNeighbourState + ", the result is: " + problem.machine_exec(bestNeighbourState.getOperations()));
                state = bestNeighbourState;

            }

            else if (abs(problem.getTarget() - problem.machine_exec(state.getOperations())) <=
                    abs(problem.getTarget() - problem.machine_exec(bestNeighbourState.getOperations()))) {
                state = state;
            }
            i++;
        }
        best_guess = state;
        result = problem.machine_exec(best_guess.getOperations());
    }

    /**
     * Main function for testing
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
            hill_climbing_search(p, 1000);
            System.out.println("The Target Number is: "+p.getTarget());
            System.out.println("The Result Number is: "+ result);
            System.out.println();
            i++;
        }
    }

}
