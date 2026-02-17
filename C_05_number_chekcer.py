# Function go here...
def num_checker(question):
    """Checks users enter an integer between two values"""

    error = "Oops - please enter an integer more than zero."

    while True:

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)
