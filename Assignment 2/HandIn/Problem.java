import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import static java.lang.Math.abs;

public class Problem {


    private static String action_add = "ADD ";
    private static String action_sub = "SUB ";
    private static String action_mul = "MUL ";
    private static String action_div = "DIV ";
    private static String action_nop = "NOP ";
    private static ArrayList<String> all_actions;
    private  ArrayList<Double> list_given;



    private double target = 0;


    public Problem(double target, ArrayList<Double> list_given)
    {
        this.target = target;
        this.list_given = list_given;
    }


    public double getTarget() {
        return target;
    }


    public String getRandomAction()
    {
        all_actions = new ArrayList<>();
        all_actions.add(action_add);
        all_actions.add(action_div);
        all_actions.add(action_nop);
        all_actions.add(action_mul);
        all_actions.add(action_sub);
        Random random  = new Random();

        return all_actions.get(random.nextInt(all_actions.size()));
    }




    public void actions(State state){

        int i = 0;
        if(state.getOperations().size() == 0)
        {
            i = 0;
        }
        else
        {
            i = state.getOperations().size();
        }

        while (i < list_given.size())
        {

            state.addOperation(new Operation(getRandomAction(), list_given.get(i)));

            i++;
        }

    }

    public double machine_exec(ArrayList<Operation> operations)
    {
        double register = 0;
        for(Operation operation : operations) {

            String operator = operation.getOperator();
            double operand = operation.getOperand();
            //double register = state.getRegister();

            if (operator == action_add) {
                register += operand;
            } else if (operator == action_sub) {
                register -= operand;
            } else if (operator == action_mul) {
                register *= operand;
            } else if (operator == action_div) {
                register /= operand;
            } else if (operator == action_nop) {
            }
            else{
                System.out.println("Unknown operator" + operator);
            }
        }


        return register;

    }


}
