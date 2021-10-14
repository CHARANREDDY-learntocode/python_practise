class Person():
    def __init__(self, name, income):
        self.name = name
        self._income = income
        
    @property
    def income(self):
        print('intiated')
        return self._income

    @income.setter
    def income(self, income):
        if income != int(income): raise TypeError('income should be an integer type')
        try:
            if self._income < income < (self._income*5):
                self._income = int(income)
                print('Updated')
            else: raise ValueError('Salary not in range')
        except AttributeError:
            self._income = int(income)
            print('Updated')


    @income.deleter
    def income(self):
        raise AttributeError('Do not delete this attribute, instead set the value to zero')

obj = Person('charan', 1)
print(obj.income)
obj.income = 4
#del obj.income

