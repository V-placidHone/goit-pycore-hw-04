# this decorator accomodate error handling for the function it decorates



def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except KeyError:
            return "Contact not found."

        except ValueError as e:
            return str(e) if str(e) else "Invalid input format."

        except IndexError:
            return "Not enough arguments for this command."

    return wrapper

    



if __name__ == "__main__":
    pass