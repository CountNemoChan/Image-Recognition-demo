import concurrent.futures
import time
from model.counting_num_of_staff import counting_num_of_staff
from model.show_live_video import show_live_video
# Define two example functions
function1 = counting_num_of_staff()

function2 = show_live_video()

# Run functions in parallel using ThreadPoolExecutor
def run_parallel():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(function1)
        future2 = executor.submit(function2)

        # Optionally, wait for the results if needed
        concurrent.futures.wait([future1, future2])

if __name__ == "__main__":
    run_parallel()