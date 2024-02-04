from antlr4 import *
from Gen.JavaParser import JavaParser
from Gen.JavaLexer import JavaLexer
from Code.HalsteadSoftwareMetrics import HalsteadSoftwareMetricsListener
from Code.McCabeCyclomaticComplexityMetrics import McCabeCyclomaticComplexityMetricsCustomListener
from Code.EjioguMetrics import EjioguMetricsListener
from Code.HenryKafuraInformationMetrics import InformationMetricsListener
from Code.ReliabilityMetrics import ReliabilityMetrics
from Code.ReadabilityMetrics import count_lines_of_code, calculate_readability_metric
from Code.COCOMOModel import calculateCOCOMO
from Code.AlbrechtFunctionPointsMetrics import AlbrechtsFunctionPoints

def walkWithLisetnerAndInputExpression(input_expression, listener):
    # Create a lexer that feeds off the input expression
    lexer = JavaLexer(InputStream(input_expression))

    # Create a stream of tokens using the lexer
    token_stream = CommonTokenStream(lexer)

    # Create a parser that feeds off the token stream
    parser = JavaParser(token_stream)

    # Obtain the parse tree by invoking the parser's entry point
    parse_tree = parser.compilationUnit()

    # Walk the parse tree with the custom listener
    walker = ParseTreeWalker()
    walker.walk(listener, parse_tree)

def main():
    file_path = ".\input.java"
    # file_path = ".\input2.java"
    with open(file_path, 'r') as file:
        input_expression = file.read()

    walkWithLisetnerAndInputExpression(input_expression, HalsteadSoftwareMetricsListener())
    walkWithLisetnerAndInputExpression(input_expression, McCabeCyclomaticComplexityMetricsCustomListener())
    walkWithLisetnerAndInputExpression(input_expression, EjioguMetricsListener())
    walkWithLisetnerAndInputExpression(input_expression, InformationMetricsListener())

    # Albrecht’s Function Points Metrics
    print("Albrecht’s Function Points Metrics:")
    # Replace these values with the actual counts for each component and characteristic scores
    components_counts = {
        'external_input': {'low': 2, 'average': 3, 'high': 1},
        'external_output': {'low': 1, 'average': 2, 'high': 3},
        'logical_internal_file': {'low': 4, 'average': 2, 'high': 1},
        'external_interface_file': {'low': 2, 'average': 1, 'high': 4},
        'external_inquiry': {'low': 3, 'average': 1, 'high': 2},
    }
    characteristic_scores = {
        'data_communication': 3,
        'distributed_function': 2,
        'heavily_used_configuration': 4,
        'transaction_rate': 3,
        'online_data_entry': 4,
        'end_user_efficiency': 5,
        'online_update': 3,
        'complex_processing': 2,
        'reusability': 4,
        'installation_ease': 5,
        'operational_ease': 3,
        'multiple_sites': 2,
        'facilitation_of_change': 4,
    }
    albrechts_fp = AlbrechtsFunctionPoints(components_counts, characteristic_scores)
    function_points = albrechts_fp.calculate_function_points()
    print(f"Function Points: {function_points}")
    
    # ReliabilityMetrics
    print("------------------------------------------------------------")
    print("Reliability Metrics:")
    reliability_metrics = ReliabilityMetrics()

    # Simulate failures and repairs
    reliability_metrics.record_failure()  # Record a failure
    reliability_metrics.record_execution_time(100)  # Record execution time
    reliability_metrics.record_failure()  # Record another failure
    reliability_metrics.record_execution_time(200)  # Record more execution time

    # Calculate metrics
    metrics_result = reliability_metrics.calculate_metrics()

    # Print results
    print(f"MTBF: {metrics_result['MTBF']} units of time")
    print(f"Availability: {metrics_result['Availability']}%")
    print(f"Failure Rate: {metrics_result['FailureRate']} failures per unit of time")

    # Readability metrics
    print("------------------------------------------------------------")
    print("Readability Metrics:")
    lines_of_code = count_lines_of_code(file_path) # Replace with the actual number of lines of code in your project
    readability_metric = calculate_readability_metric(lines_of_code)

    print(f"Number of lines of code: {lines_of_code}")
    print(f"Readability metric (number of document pages): {readability_metric}")

    ### COCOMO Model
    lexer = JavaLexer(InputStream(input_expression))
    calculateCOCOMO(lexer)
    ###



# Call the main function
if __name__ == '__main__':
    main()
