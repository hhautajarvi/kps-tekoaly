class ConsoleIO:
    """ Tekstikäyttöliittymä
    """

    def read(self, prompt):
        return input(prompt)

    def write(self, value):
        print(value)
