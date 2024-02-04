def calculate_readability_metric(lines_of_code):
    """
    Calculate readability metric based on Walston and Felix's formula.

    Parameters:
    - lines_of_code: Number of lines of code (L)

    Returns:
    - Number of document pages (D)
    """
    D = 49 * (lines_of_code / 1000) ** 1.01
    return D

def count_lines_of_code(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)