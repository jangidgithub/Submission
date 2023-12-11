import pandas as pd

data_1 = pd.read_csv('datasets/dataset-1.csv')

def generate_car_matrix(data_1)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    car_matrix = data_1.pivot(index='id_1',columns='id_2',values='car').fillna(0)
    

    return car_matrix.round(1)


def get_type_count(data_1)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    data_1['car_type'] = pd.cut(data_1['car'], bins=[-float('inf'), 15, 25, float('inf')],labels=['L', 'M', 'H'], right=False)

    return data_1


def get_bus_indexes(data_1)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    i = f.index.to_list()
    v = f.bus.to_list()
    filterd_data = pd.DataFrame(zip(i,v),columns = ['Index','Values'])

    return filterd_data


def filter_routes(data_1)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here

    return list()


def multiply_matrix(car_matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    modify_data = car_matrix.copy()
    modify_data[modify_data>20]*=0.75
    modify_data[modify_data<=20]*=1.25

    return modify_data.round(1)


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()
