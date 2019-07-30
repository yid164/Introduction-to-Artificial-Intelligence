public class Operation {
    private String operator;
    private double operand;
    public Operation(String operator, double operand)
    {
        this.operator = operator;
        this.operand = operand;
    }

    public String getOperator() {
        return operator;
    }

    public double getOperand()
    {
        return operand;
    }

    public boolean isNull()
    {
        return this.operator == null && this.operand == 0;
    }

    @Override
    public String toString()
    {
        return "(" + operator + " " + operand +")";
    }
}
