from read_data import read_csv_data
from get_data import get_data
import matplotlib.pyplot as plt

def show(gender, weight, height):
    """
    Show data.
    Args:
        gender(list): 0 and 1
        weight(list): weight
        height(list): height
    Returns:
        None
    """
    w_male = []
    w_female = []
    h_male = []
    h_female = []
    
    #WRITE YOUR CODE HERE
    for i in range(len(gender)):
        if gender[i] == 0:
            w_male.append(weight[i])
            h_male.append(height[i])
        else:
            w_female.append(weight[i])
            h_female.append(height[i])
    plt.scatter(w_female, h_female, c='red',label='Female',alpha=0.5)
    plt.scatter(w_male, h_male, c='black', label='Male',alpha=0.5)
    plt.legend(bbox_to_anchor=(0., 1.1), loc='upper left',ncol=2)
    x=[i / 2.205 for i in range(100,300,50)]; y=[2.54 * i for i in range(55,85,5)]
    plt.xticks(x,labels=['100','150','200','250'])
    plt.yticks(y,labels=['55','60','65','70','75','80'])
    

    plt.show()

data = read_csv_data('data/weight-height.csv')
gender, weight, height = get_data(data)

show(gender, weight, height)