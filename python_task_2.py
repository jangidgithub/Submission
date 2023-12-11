import pandas as pd

df = pd.read_csv(r'datasets/dataset-3.csv')

def calculate_distance_matrix(df)->pd.DataFrame():
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # Write your logic here
    unique_ids = sorted(list(set(df['id_start'].unique()) | set(df['id_end'].unique())))

    # Creating an empty DataFrame to store the distance matrix
    distance_matrix = pd.DataFrame(index=unique_ids, columns=unique_ids)
    distance_matrix = distance_matrix.fillna(0)  # Filling with zeros initially

    # Filling the distance matrix with cumulative distances
    for index, row in df.iterrows():
        id_start, id_end, distance = row['id_start'], row['id_end'], row['distance']
        distance_matrix.at[id_start, id_end] += distance
        distance_matrix.at[id_end, id_start] += distance

    # Calculating cumulative distances for indirect paths (A to C via B)
    for i in unique_ids:
        for j in unique_ids:
            for k in unique_ids:
                if distance_matrix.at[i, k] == 0 and i != k and j != k and distance_matrix.at[i, j] != 0 and distance_matrix.at[j, k] != 0:
                    distance_matrix.at[i, k] = distance_matrix.at[i, j] + distance_matrix.at[j, k]
                    distance_matrix.at[k, i] = distance_matrix.at[i, k]

    # Setting diagonal values to 0
    np.fill_diagonal(distance_matrix.values, 0)

    return distance_matrix


def unroll_distance_matrix(distance_matrix)->pd.DataFrame():
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # Write your logic here
    unrolled_distances = []
    
    # Iterate over the rows and columns of the distance matrix
    for id_start in distance_matrix.index:
        for id_end in distance_matrix.columns:
            # Exclude same id_start and id_end combinations
            if id_start != id_end:
                distance = distance_matrix.at[id_start, id_end]
                unrolled_distances.append({'id_start': id_start, 'id_end': id_end, 'distance': distance})
    
    # Create a DataFrame from the unrolled distances
    unrolled_df = pd.DataFrame(unrolled_distances)

    return unrolled_df


def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Write your logic here

    return df


def calculate_toll_rate(df)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Wrie your logic here
        rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }
    
    # Calculate toll rates for each vehicle type
    for vehicle_type, rate in rate_coefficients.items():
        df[vehicle_type] = df['distance'] * rate

    return df


def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here

    return df
