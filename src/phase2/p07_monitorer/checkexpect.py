import sys
import traceback


def custom_excepthook(exc_type, exc_value, exc_traceback):
    # Open a log file in append mode
    with open('errors_derniersrecours.log', 'a') as f:
        # Write the exception details to the log file
        f.write(f"Exception type: {exc_type.__name__}n")
        f.write(f"Exception value: {exc_value}n")
        f.write("Traceback:n")
        traceback.print_tb(exc_traceback, file=f)
        f.write("n")

    # Optionally, print to console for immediate feedback
    print(f"An error occurred: {exc_value}")


# Assign the custom excepthook
sys.excepthook = custom_excepthook





# -------------------


def cause_exception():
    raise ValueError("An example exception")
# This will call the custom excepthook


cause_exception()

