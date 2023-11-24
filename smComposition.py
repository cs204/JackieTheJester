# Use sm.R, sm.Gain, sm.Cascade, sm.FeedbackAdd and sm.FeedbackSubtract
# to construct the state machines
import sm

def accumulator(init):
    """
    @param init: ввод до первого вывода
    @return: вывод которого в момент n равен сумме вводов до момента n включительно.
    Таким образом, выход в момент 0 представляет собой сумму init и ввода в момент 0.
    """
    return sm.FeedbackAdd(sm.Gain(1), sm.R(init))

def accumulatorDelay(init):
    """
    @param init: вывод в момент времени 0
    @return:  вывод в момент n равен сумме вводов до момента n-1 включительно
    """
    return sm.FeedbackAdd(sm.R(init), sm.Gain(1)) # Здесь должен быть ваш код

def accumulatorDelayScaled(s, init):
    """
    @param s: константа умножения
    @param init: вывод в момент 0
    """
    return sm.Cascade(sm.Gain(s), sm.FeedbackAdd(sm.R(init), sm.Gain(1)))

# Для проверки раскомментируйте  нужные строки
def test():
    print("accumulator(1).transduce([1,2,3]): ", accumulator(1).transduce([1, 2, 3]))
    print("accumulatorDelay(2).transduce([1, 2, 3]):", accumulatorDelay(2).transduce([1, 2, 3]))
    print("accumulatorDelayScaled(0.1, 1).transduce([1, 2, 3]):", accumulatorDelayScaled(0.1, 1).transduce([1, 2, 3]))
    pass

if __name__ == "__main__":
    test()

