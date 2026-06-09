EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.
    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    ...
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.
    Parameters:
        number_of_layers (int): the number of layers
    Returns:
        int: the time spent preparing the layers (in minutes)        
    ...
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes:
    Parameters:
        number_of_layers (int): the number of layers
        elapsed_bake_time (int): the elapsed bake time   
    Returns:
        int: the time already spent for preparation and baking     
    ...
    """
    
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)