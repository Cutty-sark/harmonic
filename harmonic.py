
#ex0 from Comp mod part 1


# Import relevant python modules
import math
import matplotlib.pyplot as pyplot

# Define the cosine function
#def harmonic(x):
 #   return math.sin(x)

# Main method
def main():
    
    # number of data points
 
    while True:
        try:
            n_loop = int(input("enter an positive integer N to sum to:"))
        except ValueError:
            print("N has to be a positive integer")
            continue
        if n_loop <= 0:
            print("N has to be a positive integer")
        else:
            break

    while True:
        try:
            output_name = str(input("Enter the name of the outpute file"))
        except ValueError:
            print("please use a string")
            continue
        else:
            break

            

    #output_name = input("Enter the name of the output file")
    #output_namestr = str(output_name)
    
                


    # open output file
    out_file = open(output_name+".dat","w")
    #

    f = 0

    # prepare data lists
    x_values = []
    y_values = []

    # obtain function values and write them to file
    for i in range(n_loop):
        x = 2*math.pi*(i)/n_loop - math.pi
       # x = np.
         #this is the range -pi to pi: for i=0 x =-pi, for i=nloop x =pi
        f = f + (1/(2*i-1))*math.sin((2*i-1)*x)
       
        # append data to lists and output file
        x_values.append(x)
        y_values.append(f)
    
        out_file.write(str(x) + "xddddd " + str(f) + "\n")

    # close output file
    out_file.close()

    # plot result
    pyplot.plot(x_values,y_values)
    pyplot.suptitle('Plotting the Harmonic function')
    pyplot.xlabel('X')
    pyplot.ylabel('Y')
    pyplot.show()


# Execute main method
if __name__ == "__main__": main()