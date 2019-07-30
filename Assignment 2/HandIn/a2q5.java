/**
 * Student Name: Yinsheng Dong
 * Student Number: 11148648
 * NSID: yid164
 * CMPT317 A2Q6
 */


import java.util.ArrayList;

import static java.lang.Math.abs;


public class a2q5 {


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

        State state1 = state;
        while (count_start < count_end)
        {

            double x = best.getOperations().get(count_start).getOperand();

            Operation operation = new Operation(problem.getRandomAction(),x);
            best.getOperations().set(count_start, operation);

            if (abs(problem.getTarget() - problem.machine_exec(state.getOperations())) >
                    abs(problem.getTarget() - problem.machine_exec(best.getOperations()))) {
                state1 = best;
                //System.out.println("GG");
                return state1;
                //System.out.println(best);
            }

            count_start++;
        }
        state = state1;


        return state;

    }

    public static double result;
    public static void stochasticHillClimbingSearch(Problem problem, int times)
    {
        ArrayList<Operation> best_operation = new ArrayList<>();
        State best_guess = new State(0, best_operation);
        problem.actions(best_guess);

        int i = 0;
        State state = best_guess;
        while (i<times)
        {

            State bestNeighbourState = bestNeighbourState(state,problem);
            if (abs(problem.getTarget() - problem.machine_exec(state.getOperations())) >
                    abs(problem.getTarget() - problem.machine_exec(bestNeighbourState.getOperations()))) {
                //System.out.println("Find the better one: "+ bestNeighbourState + ", the result is: " + problem.machine_exec(bestNeighbourState.getOperations()));
                state = bestNeighbourState;

            }

            i++;
        }
        best_guess = state;
        result = problem.machine_exec(best_guess.getOperations());


    }

    public static void main(String[]args)
    {
        String dir = "/Users/ken/IdeaProjects/CMPT317A2/src/a2_data_simple.txt";
        ArrayList<Problem> problems = ReadFile.readProblemFile(dir);
        int i = 0;
        for(Problem p : problems)
        {

            System.out.println("Test "+i+": ");
            stochasticHillClimbingSearch(p,1000);
            System.out.println("The Target Number is: "+p.getTarget());
            System.out.println("The Result Number is: "+ result);
            System.out.println();
            i++;
        }
    }
}
