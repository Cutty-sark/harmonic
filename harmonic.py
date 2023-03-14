#ex0 from Comp mod part 1

# Import relevant python modules
import math
import matplotlib.pyplot as pyplot

# Main method
def main():

    # number of data points and error handling input
    while True:
        try:
            n_loop = int(input("enter an positive integer N (granularity and sum): "))
        except ValueError:
            print("N has to be a positive integer")
            continue
        if n_loop <= 0:
            print("N has to be a positive integer")
        else:
            break

    #file name for .dat
    while True:
        try:
            output_name = str(input("Enter the name of the output file: "))
        except ValueError: #don't even know if you can trigger this but
            print("please use a string")
            continue
        else:
            break

    # open output file
    out_file = open(output_name+".dat","w")

    # prepare data lists
    fi_values = []
    x_values = []
    y_values = []
    x = -math.pi
    f = 0
    x_values.append(x)
    y_values.append(f)

    # obtain function values and write them to file
    for k in range(n_loop):
        fi_values = []
        x = 2*k*math.pi/n_loop-math.pi    #this is the range -pi to pi: for i=0 x =-pi, for i=n_loop x =pi
        for i in range(1, n_loop+1):
            fi_values += [(1/((2*i)-1))*math.sin(((2*i)-1)*x)]    #harmonic function
        f = sum(fi_values)


        # append data to lists and output file
        x_values.append(x)
        y_values.append(f)

        out_file.write(str(x) + " " + str(f) + "\n")

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


## thanks to butterflyknife on Stack Exchange for the help with my i  range and clearing fi_values for the next f val. 