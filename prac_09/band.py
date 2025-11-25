class Band:
    """Represent a band with a name and a list of musicians."""

    def __init__(self, name=""):
        """Initialise a band with a name and a list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band and musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician."""
        self.musicians.append(musician)

    def play(self):
        """Inform each musician to play their instrument."""
        for musician in self.musicians:
            musician.play()