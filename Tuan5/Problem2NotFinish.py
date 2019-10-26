class StringExp:

    def __init__(self, exp):
        self.exp = exp

    def couple(self, stackCharAndExpChar):
        if stackCharAndExpChar == '()' or stackCharAndExpChar == '[]' or \
        stackCharAndExpChar == '{}':
            return True
        else:
            return False


    def isValid(self):
        stack = []
        for e in self.exp:
            if e in '([{':
                stack.append(e)
            elif e in ')]}':
                if len(stack) == 0 or not self.couple(stack[-1] + e):
                    return False
                else:
                    stack.pop()
        if len(stack) != 0:
            return False
        return True


class WellNetExp(StringExp):
