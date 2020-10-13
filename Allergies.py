allergies_dict = {
    "eggs" : 1,
    "peanuts" : 2,
    "shellfish" : 4,
    "strawberries" : 8,
    "tomatoes" : 16,
    "chocolate" : 32,
    "pollen" : 64,
    "cats" : 128,
}
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

        # check for each digit if it is one, if one add the key to the allergies list
        for i, digit in enumerate(binSum):
            if digit == "1":
                allergies_list.append(list(allergies_dict.keys())[i])
        return allergies_list



