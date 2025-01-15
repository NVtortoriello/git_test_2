import numpy as np

def non_linearity(z_in):
    for idx, i in enumerate(z_in):
        if i<0:
            z_in[idx]=0
        else:
            z_in[idx]=1
    
    return z_in



if __name__ == "__main__":
    x1,x2=list(map(int, input("Enter x1, x2: ").split()))
    x_in = np.array([1, x1, x2])


    #LAYER 1
    W1 = np.array([[0 , 0 , 0], [-0.5 , 1 , -1], [-0.5 , -1 , 1]])

    z = (W1 @ x_in) + np.array([1, 0 , 0])

    #non linearity
    z = non_linearity(z)
    #output 

    V=np.array([-0.5 , 1, 1])
    y = V @ z
    y = 0 if y < 0 else 1

    #Printout 
    print(f"Input: x1={x1} , x2={x2}   XOR = {y}")
