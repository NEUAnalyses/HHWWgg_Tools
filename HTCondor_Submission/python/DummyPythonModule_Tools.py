"""
25 November 2021
Abraham Tishelman-Charny

The purpose of this python module is to serve as a placeholder for tools which can be accessed when running over HTCondor.
"""

# dummy function 
def MultiplyParameter(inVal):
    print("In MultiplyParameter method")
    print("Input value:",inVal)

    newValue = float(inVal) * 2. 

    return newValue 