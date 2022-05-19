from read_data import read_csv_data
import pathlib as pl

def get_data(data):
    """
    Get data from list.
    Gender: Change Male to 0 and Female to 1
    Weight: Place the column in the Kg view given in Pound (1 kg = 2,205 pound).
    Height: Place the column on the list in the cm view given in inches (2.54 cm = 1 inch).
    Args:
        data(list): data split row
    Returns:
        tuple: gender, weight and height

    """
    gender = []
    weight = []
    height = []
    
    # WRITE YOUR CODE HERE
    for i in data[1:]:
        if i[0]=='Male':
            gender.append(0)
        else:
            gender.append(1)
        weight.append(float(i[2]) / 2.205)
        height.append(float(i[1]) * 2.54)

    return gender,weight,height

path = pl.Path('data') / 'weight-height.csv'
data = read_csv_data(path)