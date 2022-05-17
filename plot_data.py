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

    plt.show()

data = read_csv_data('data/weight-height.csv')
gender, weight, height = get_data(data)

show(gender, weight, height)