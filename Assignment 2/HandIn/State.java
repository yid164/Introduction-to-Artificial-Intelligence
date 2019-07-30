import java.util.ArrayList;

public class State {

    private double register;
    private ArrayList<Operation> operations;


    public State(double register, ArrayList<Operation> operations) {
        this.register = register;
        this.operations = operations;

    }

    public void addOperation(Operation operation)
    {
        this.operations.add(operation);
    }

    public double getRegister() {
        return register;
    }

    public ArrayList<Operation> getOperations()
    {
        return this.operations;
    }

    @Override
    public String toString()
    {
        return "Operations: " + operations;

    }

}
