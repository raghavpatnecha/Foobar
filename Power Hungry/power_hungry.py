import operator
def answer(xs):
    try:
        if len(xs) == 0 and len(xs) > 50:
            raise Exception
        positive_values = []
        negative_values = []
        maxPower = 999
        if xs[0] == 0:
            maxPower = 0
        else:

            for index, value in enumerate(xs):
                if xs[index] > 0:
                    positive_values.append(value)

                if xs[index] < 0:
                    negative_values.append(value)

            negative_valuesLength = len(negative_values)
            positive_valuesLength = len(positive_values)
            if negative_valuesLength == 1:
                if positive_valuesLength > 0:
                    maxPower = reduce(operator.mul, positive_values)
                else:
                    maxPower = negative_values[0]
            else:

                if (positive_valuesLength > 0) and (negative_valuesLength > 1):
                    if negative_valuesLength % 2 != 0:
                        del negative_values[negative_values.index(max([n for n in xs if n < 0]))]
                    maxPower = reduce(operator.mul, positive_values + negative_values)
                elif negative_valuesLength > 1:
                    if negative_valuesLength % 2 != 0:
                        del negative_values[negative_values.index(max([n for n in xs if n < 0]))]
                    maxPower = reduce(operator.mul, negative_values)
                elif positive_valuesLength > 0:
                    maxPower = reduce(operator.mul, positive_values)
                else:
                    maxPower = 0

        return str(maxPower)

    except Exception:
        return "Invalid"



