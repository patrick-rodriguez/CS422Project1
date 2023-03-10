"""
File Name: course.py
Program Name: Easy A
File purpose: This file contains the class Course and its methods. It is used primarily by
    database_functions.py to create and adjust a list of Course objects which will then be used
    by plots.py to create appropriate plots given a user's specifications.
Creation date: Jan 15, 2023
Initial Authors: Patrick Rodriguez
"""
class Course:
    """Initially class was named 'Professor' but realized I could use the functions when filtering by class level.
    Therefore renamed to Course.py"""
    def __init__(self, name, aperc, bperc, cperc, dperc, fperc):
        """Course class object initialization. Used when a user is filtering data by instructor or class level."""
        self.name = name  # Instructor's name OR Course Level
        self.aperc = aperc  # Average percentage of A distribution
        self.bperc = bperc  # Average percentage of B distribution
        self.cperc = cperc  # Average percentage of C distribution
        self.dperc = dperc  # Average percentage of D distribution
        self.fperc = fperc  # Average percentage of F distribution
        self.count = 1  # Amount of times professor has taught a class.

    def adjust_percentages(self, new_aperc, new_bperc, new_cperc, new_dperc, new_fperc):
        """Adjusts the average letter grade distribution if a professor is found more than once within a data
        set."""
        self.count += 1
        self.aperc = (self.aperc + new_aperc) / 2
        self.bperc = (self.bperc + new_bperc) / 2
        self.cperc = (self.cperc + new_cperc) / 2
        self.dperc = (self.dperc + new_dperc) / 2
        self.fperc = (self.fperc + new_fperc) / 2
