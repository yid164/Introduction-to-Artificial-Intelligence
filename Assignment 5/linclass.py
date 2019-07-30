# CMPT 317 Assignment 5
# A module containing 2 classes, to express the linear classification 
# task in terms of AIMA Ch 3,4.  

import math as math

class Line(object):
    """ A line object is the State for a linear classifier.
        A line is represented by a list of coefficients called ws
        the line is defined by the equation
        w*x = 0
        where w is the list of coefficients, and x is a list of 
        coordinates in N dimensions, and the product is the dot product.
        
        We need a few behaviours:
            linear_model(x) -- calculate w*x for the given x
            f(x) -- given [x0, ..., x(n-1)] return the value of xn
                 -- it's used mostly for plotting and visualization
            mxb() -- return a string that looks like what we learned in high school.
        """
        
    def __init__(self, coeffs):
        """
            coeffs: a list of numeric values [w0, w1, ..., wn]
        """
        self.ws = coeffs

    def linear_model(self, xs):
        """ Calculate the output of a linear model.
            ws: a list of coefficients
            return: the pairwise product of ws*xs
        """
        return sum([x*w for x,w in zip(xs,self.ws)])

    def __str__(self):
        """ Return a string that represents the line.
            Uses the linear algebra style of w.x = 0
        """
        result = []
        for i in range(len(self.ws)):
            result.append("{0:3.1f} x{1:d}".format(self.ws[i], i))
        return "+".join(result)

    def mxb(self):
        """ An alternate string representation, using the more intuitive
            y = mx + b form.
        """
        result = 'y = {0:3.1f}x + {1:3.1f}'.format(-self.ws[1], -self.ws[0])
        return result

    def f(self, xs):
        """ For plotting, we give values [x0, ..., x(n-1)], and 
            get back the dependent value xn.
            In 2D, we have x2 = mx1 + b.
        """
        if self.ws[2] != 0:
            return -self.linear_model(xs+[0])/self.ws[-1]


class LinearClassifier(object):
    """ Uses a linear model, to try to find a line that separates two classes.
        When the data is 2D, it's a line.  In 3D or more, it's a linear subspace.
        The line defines a step function to classify a data point.
    """
    
    def __init__(self):
        pass
        
    def classify(self, line, xs):
        """ 
            The classifier for linear models.  
            Class 0 is on or below the line.  Class 1 is above the line.
            xs: a list of coordinates
            line: a Line object (state)
            Return the class for the given point xs.
        """
        if line.linear_model(xs) <= 0:
            return 0
        else:
            return 1

    def best_step(self, line, alpha, pt):
        """ Apply the update formula for a given data point.
            line: a Line object, the state
            alpha: the learning rate
            pt: one datapoint with the class label: (x1, x2, y)
            Returns the new line
        """
        # set up some local variables
        x1, x2, y = pt
        x0 = 1

        # here we translate to the linear model representation
        xs = [x0, x1, x2]

        # apply the learning rule
        # hval remembers what the current line says about xs
        hval = self.classify(line, xs)
        
        # calculate small adjustments to each coefficient 
        deltas = [alpha * x * (y - hval) for x in xs[:-1]]
        
        # apply the small adjustment to create a new line
        new_coeffs = [w + dw for w,dw in zip(line.ws[:-1], deltas)]
        return Line(new_coeffs + [1])


    def tabulate_class(self, data, line):
        """ Output a table to show how the linear classifier works.
            data: a list of 2D datapoints (x1, x2, y)
            m: a number representing the slope of a line
            b: a number representing the y-intercept of a line
        """
    
        # display the headings of a formatted table
        print('   {0:5s}{1:5s}{2:5s}{3:5s}{4:5s}'.format('x1','x2','LM','Pred','Class'))

        # display each datapoint in data as a row in the table
        for x1, x2, y in data:
            xs = [1, x1, x2]
            lin_model_out = line.linear_model(xs)
            pred_class = self.classify(line, xs)
            print('{0:5.1f}{1:5.1f}{2:5.1f}{3:4d}{4:5d}'.format(
                x1,x2,lin_model_out,pred_class,y), end='')
            if pred_class != y: 
                print(' ** Classification error')
            else:
                print()


class LogisticClassifier(object):
    """ Uses a linear model, to try to find a line that separates two classes.
        When the data is 2D, it's a line.  In 3D or more, it's a linear subspace.
        The line orients a signmoid surface to classify a data point.
    """

    def __init__(self):
        pass
        
    def classify(self, line, xs):
        """ 
            The classifier for logistic models. returning a floating point
            number in the range [0, 1], which describes how far away the 
            point is from the line.  
            Class 0 is on or below the line.  Class 1 is above the line.
            xs: a list of coordinates
            line: a Line object (state)
            Return a floating point value for the given point xs.
        """
        return 1.0/(1.0 + math.exp(-1 * line.linear_model(xs)))

    def best_step(self, line, alpha, pt):
        """ Apply the update formula for a given data point.
            line: a Line object, the state
            alpha: the learning rate
            pt: one datapoint with the class label: (x1, x2, y)
            Returns the new line
        """
        # set up some local variables
        x1, x2, y = pt
        x0 = 1

        # here we translate to the linear model representation
        xs = [x0, x1, x2]

        # apply the learning rule
        # hval remembers what the current line says about xs
        hval = self.classify(line, xs)
        
        # calculate small adjustments to each coefficient 
        deltas = [alpha * x * (y - hval)*hval*(1-hval) for x in xs[:-1]]
#         print(deltas)
        
        # apply the small adjustment to create a new line
        new_coeffs = [w + dw for w,dw in zip(line.ws[:-1], deltas)]
        return Line(new_coeffs + [1])


    def tabulate_class(self, data, line):
        """ Output a table to show how the linear classifier works.
            data: a list of 2D datapoints (x1, x2, y)
            m: a number representing the slope of a line
            b: a number representing the y-intercept of a line
        """
    
        # display the headings of a formatted table
        print('  {0:5s}{1:5s}{2:5s}{3:5s}{4:5s}'.format('x1','x2','LM','Pred','Class'))

        # display each datapoint in data as a row in the table
        for x1, x2, y in data:
            xs = [1, x1, x2]
            lin_model_out = line.linear_model(xs)
            pred_class = self.classify(line, xs)
            print('{0:5.1f}{1:5.1f}{2:5.1f}{3:5.1f}{4:5d}'.format(
                x1,x2,lin_model_out,pred_class,y), end='')
            if abs(y - pred_class) > 0.5: 
                print(' ** Classification error')
            else:
                print()
