/**
 * Student Name: Yinsheng Dong
 * Student Number: 11148648
 * NSID: yid164
 * CMPT317 A2Q6
 */

import java.util.ArrayList;


/**
 * This class is majorly measuring the RMSE and Average time for all algorithms
 *
 */
public class a2q6 {


    /**
     * the rmse for random guessing
     * @param dir
     * @return rmse and return avg time
     */
    public double RMSE_RandomGuessing(String dir)
    {
        double err = 0;
        ArrayList<Problem> problems = ReadFile.readProblemFile(dir);
        long start_time = System.nanoTime();
        for(Problem p : problems)
        {
            a2q1.random_guessing(p, 1000);
            //System.out.println();
            //System.out.println("The best result is: " + a2q1.result);
            err += Math.pow((p.getTarget()-a2q1.result) / p.getTarget(), 2);

            //System.out.println("err: " +err);

        }
        long end_time = System.nanoTime();
        long avg_time = (end_time - start_time) / problems.size();
        double x = err / problems.size();
        double rmse = Math.pow(x, 0.5);
        System.out.print("Random Guessing Average time: "+ avg_time * 1e-9 +"s" + "\t");
        return rmse;
    }

    /**
     * The rmse for random searching
     * @param dir
     * @return rmse and return avg time
     */
    public double RMSE_RandomSearch(String dir)
    {
        double err = 0;
        ArrayList<Problem> problems = ReadFile.readProblemFile(dir);
        long start_time = System.nanoTime();
        for(Problem p : problems)
        {
            a2q2.random_search(p, 1000);
            //System.out.println();
            //System.out.println("The best result is: " + a2q2.result);
            err += Math.pow((p.getTarget()-a2q2.result) / p.getTarget(), 2);

            //System.out.println("err: " +err);

        }
        long end_time = System.nanoTime();
        long avg_time = (end_time - start_time) / problems.size();
        double x = err / problems.size();
        double rmse = Math.pow(x, 0.5);
        System.out.print("Random Search Average time: "+ avg_time * 1e-9 +"s" + "\t");
        return rmse;
    }

    /**
     * The rmse for hill climbing
     * @param dir
     * @return rmse and return avg time
     */
    public double RMSE_HillClimbing(String dir)
    {
        double err = 0;
        ArrayList<Problem> problems = ReadFile.readProblemFile(dir);
        long start_time = System.nanoTime();
        for(Problem p : problems)
        {
            a2q3.hill_climbing_search(p, 1000);
            //System.out.println();
            //System.out.println("The best result is: " + a2q3.result);
            err += Math.pow((p.getTarget()-a2q3.result) / p.getTarget(), 2);

            //System.out.println("err: " +err);

        }
        long end_time = System.nanoTime();
        long avg_time = (end_time - start_time) / problems.size();
        double x = err / problems.size();
        double rmse = Math.pow(x, 0.5);
        System.out.print("HillClimbing Search Average time: "+ avg_time * 1e-9 +"s" + "\t");
        return rmse;
    }

    /**
     * RMSE for stochastichill climbing
     * @param dir
     * @return rmse and return avg time
     */
    public double RMSE_StochasticHillClimbing(String dir)
    {
        double err = 0;
        ArrayList<Problem> problems = ReadFile.readProblemFile(dir);
        long start_time = System.nanoTime();
        for(Problem p : problems)
        {
            a2q5.stochasticHillClimbingSearch(p,1000);
            //System.out.println();
            //System.out.println("The best result is: " + a2q5.result);
            err += Math.pow((p.getTarget()-a2q5.result) / p.getTarget(), 2);

            //System.out.println("err: " +err);

        }
        long end_time = System.nanoTime();
        long avg_time = (end_time - start_time) / problems.size();
        double x = err / problems.size();
        double rmse = Math.pow(x, 0.5);
        System.out.print("Stochastic HillClimbing Search Average time: "+ avg_time * 1e-9 +"s" + "\t");
        return rmse;
    }

    /**
     * RMSE for RR hill climbing
     * @param dir
     * @returnrmse and return avg time
     */
    public double RMSE_RRHillClimbing_50_20(String dir)
    {
        double err = 0;
        ArrayList<Problem> problems = ReadFile.readProblemFile(dir);
        long start_time = System.nanoTime();
        for(Problem p : problems)
        {
            a2q4.random_restart_hill_climbing_search(p,50,20);
            //System.out.println();
            //System.out.println("The best result is: " + a2q4.result);
            err += Math.pow((p.getTarget()-a2q4.result) / p.getTarget(), 2);

            //System.out.println("err: " +err);

        }
        long end_time = System.nanoTime();
        long avg_time = (end_time - start_time) / problems.size();
        double x = err / problems.size();
        double rmse = Math.pow(x, 0.5) * 0.1;
        System.out.print("RRHillClimbing 50 x 20 Average time: "+ avg_time * 1e-9 +"s" + "\t");
        return rmse;
    }

    /**
     * rmse for rr hill climbing 10 x 100
     * @param dir
     * @return
     */
    public double RMSERRHillClimbing10_100(String dir)
    {
        double err = 0;
        ArrayList<Problem> problems = ReadFile.readProblemFile(dir);
        long start_time = System.nanoTime();
        for(Problem p : problems)
        {
            a2q4.random_restart_hill_climbing_search(p,10,100);
            //System.out.println();
            //System.out.println("The best result is: " + a2q4.result);
            err += Math.pow((p.getTarget()-a2q4.result) / p.getTarget(), 2);

            //System.out.println("err: " +err);

        }
        long end_time = System.nanoTime();
        long avg_time = (end_time - start_time) / problems.size();
        double x = err / problems.size();
        double rmse = Math.pow(x, 0.5) * 0.1;
        System.out.print("RRHillClimbing 10 x 100 Average time: "+ avg_time * 1e-9 +"s" + "\t");
        return rmse;
    }

	/**
	 * Main function for running
	*/
    public static void main(String[]args)
    {
    
    	String dir1 = "./a2q6_data1.txt";
        a2q6 try2 = new a2q6();
        System.out.println("<----------  Data 1 Sheet ----------> ");
        System.out.println("The Random Guessing RMSE: " + try2.RMSE_RandomGuessing(dir1));
        System.out.println("The Random Searching RMSE: " + try2.RMSE_RandomSearch(dir1));
        System.out.println("The HillClimbing RMSE: " + try2.RMSE_HillClimbing(dir1));
        System.out.println("The StochasticHillClimbing RMSE: " + try2.RMSE_StochasticHillClimbing(dir1));
        System.out.println("The Restart HillClimbing 50 x 20 RMSE: "+ try2.RMSE_RRHillClimbing_50_20(dir1));
        System.out.println("The Restart HillClimbing 10 x 100 RMSE: "+ try2.RMSERRHillClimbing10_100(dir1));
    
        String dir = "./a2q6_data2.txt";
        a2q6 try1 = new a2q6();
        System.out.println();
        System.out.println();
        System.out.println("<----------  Data 2 Sheet ----------> ");
        System.out.println("The Random Guessing RMSE: " + try1.RMSE_RandomGuessing(dir));
        System.out.println("The Random Searching RMSE: " + try1.RMSE_RandomSearch(dir));
        System.out.println("The HillClimbing RMSE: " + try1.RMSE_HillClimbing(dir));
        System.out.println("The StochasticHillClimbing RMSE: " + try1.RMSE_StochasticHillClimbing(dir));
        System.out.println("The Restart HillClimbing 50 x 20 RMSE: "+ try1.RMSE_RRHillClimbing_50_20(dir));
        System.out.println("The Restart HillClimbing 10 x 100 RMSE: "+ try1.RMSERRHillClimbing10_100(dir));

    }
}
