allergies_types = [
    "eggs",
    "peanuts",
    "shellfish",
    "strawberries",
    "tomatoes",
    "chocolate",
    "pollen",
    "cats",
]
class Allergies:
    def __init__(self, sum):
        while sum > 256:
            sum -= 256
        self.lst = self.prepareList(sum)


    def is_allergic_to(self, input_string):
        if input_string in self.lst:
            return True
        else:
            return False

    def prepareList(self, sum):
        allergies_list = []
        # make sure the binary representation contains only 0 and 1 and 2^0 is at the first index
        binSum = bin(sum)
        binSum = binSum[2:]
        binSum = binSum[::-1]

        # check for each digit if it is "1". If so, add the key to the allergies list
        for i, digit in enumerate(binSum):
            if digit == "1":
                allergies_list.append(allergies_types[i])
        return allergies_list



