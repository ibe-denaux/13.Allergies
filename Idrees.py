class Allergies:

    def __init__(self, score):
        self.lst = []

        # ignore non-listergen numbers
        score = score % 256

        if score >= 128:
            self.lst.append('cats')
        if score >= 64:
            self.lst.append('pollen')
            score -= 64
        if score >= 32:
            self.lst.append('chocolate')
            score -= 32
        if score >= 16:
            self.lst.append('tomatoes')
            score -= 16
        if score >= 8:
            self.lst.append('strawberries')
            score -= 8
        if score >= 4:
            self.lst.append('shellfish')
            score -= 4
        if score >= 2:
            self.lst.append('peanuts')
            score -= 2
        if score >= 1:
            self.lst.append('eggs')

        self.lst.reverse()

    def is_allergic_to(self, item):
        if item in self.lst:
            allergic = True
        else:
            allergic = False

        return allergic

