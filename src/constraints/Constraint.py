class Constraint:
    """ This class is meant to be a base class used to define integrity constraints to check on reports."""

    def __init__(self, name : str):
        self.name = name