class Polynomial:

    def __init__(self, *coefficients):
        self._id = 0
        cfs = []
        if not len(coefficients):
            cfs = [0]
        else:
            cfs = coefficients[0]
        if isinstance(cfs, Polynomial):
            self.coeffs = cfs.coeffs
        elif isinstance(cfs, list):
            self.coeffs = cfs
        elif isinstance(cfs, dict):
            cf = list(cfs.keys())
            self.coeffs = [0]*(cf[-1] + 1)
            for n in range(len(cf)):
                self.coeffs[cf[n]] = cfs[cf[n]]
        elif isinstance(coefficients, tuple):
            self.coeffs = list(coefficients)
            if len(coefficients) == 0:
                self.coefficients = [0]

    def __str__(self):
        string = ""
        first = False
        for n in range(len(self.coeffs)):
            n_coeff = str(abs(self.coeffs[n]))

            if self.coeffs.count(0) <= len(self.coeffs) - 2 and self.coeffs[n - 1] != 0 and first:
                if self.coeffs[n] != 0:
                    string = f" + {string}" if self.coeffs[n - 1] > 0 else f" - {string}"
                else:
                    string = f" - {string}" if self.coeffs[n - 1] < 0 else f"{string}"
            if n_coeff != "0":
                first = True

            if n > 1:
                if n_coeff == "1":
                    string = f"x^{str(n)}{string}"
                elif n_coeff != "0":
                    string = f"{n_coeff}x^{str(n)}{string}"
            elif n == 1:
                if n_coeff == "1":
                    string = f"x{string}"
                elif n_coeff != "0":
                    string = f"{n_coeff}x{string}"
            elif n_coeff != "0":
                string = n_coeff
            elif len(self.coeffs) <= 1 or len(self.coeffs) == self.coeffs.count(0):
                string = "0"
        else:
            if self.coeffs[-1] < 0:
                string = f"- {string}"
        return string

    def __repr__(self):
        return "Polynomial " + str(self.coeffs)

    def __eq__(self, other):
        if not isinstance(other, Polynomial):
            raise TypeError("Right isn't polynom.\n")
        flag = False
        if len(self.coeffs) == len(other.coeffs):
            flag = True
            for _ in range(len(self.coeffs)):
                if self.coeffs[_] != other.coeffs[_]:
                    flag = False
                    break
        return flag

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other_):
        if not isinstance(other_, (Polynomial, int)):
            raise TypeError("Right side isn't polynom or number.\n")
        other = Polynomial(other_) if isinstance(other_, int) else other_
        new_len = max(len(self.coeffs), len(other.coeffs))
        new_coeffs = [0] * new_len
        new_self_coeffs = [0] * new_len
        new_other_coeffs = [0] * new_len
        for _ in range(len(self.coeffs)):
            new_self_coeffs[_] = self.coeffs[_]
        for _ in range(len(other.coeffs)):
            new_other_coeffs[_] = other.coeffs[_]
        for _ in range(new_len):
            new_coeffs[_] = new_self_coeffs[_] + new_other_coeffs[_]
        return Polynomial(new_coeffs)

    def __radd__(self, other):
        return other.__add__(self)

    def __sub__(self, other):
        return self.__add__(other.__neg__())

    def __rsub__(self, other):
        return self.__neg__().__radd__(other)

    def __mul__(self, other_):
        if not isinstance(other_, (Polynomial, float, int)):
            raise TypeError("Right side isn't polynom or number.\n")
        other = Polynomial(other_) if isinstance(other_, int) else other_
        new_len = len(self.coeffs) + len(other.coeffs) - 1
        new_coeffs = [0] * new_len
        for _ in range(len(self.coeffs)):
            for __ in range(len(other.coeffs)):
                new_coeffs[(_ + __)] += self.coeffs[_] * other.coeffs[__]
        return Polynomial(new_coeffs)

    def __rmul__(self, other):
        return other.__mul__(self)

    def __neg__(self):
        self.coeffs = list(map(lambda x: -x, self.coeffs))
        return self

    def __call__(self, x):
        value = 0
        for _ in range(len(self.coeffs)):
            value += self.coeffs[_] * (x ** _)
        return value

    def degree(self):
        return len(self.coeffs) - 1

    def der(self, d=1):
        if d == 0:
            return self
        new_len = len(self.coeffs) - 1
        new_coeffs = [0] * new_len
        for _ in range(1, new_len + 1):
            new_coeffs[_ - 1] = self.coeffs[_] * _
        return Polynomial(new_coeffs).der(d - 1)

    def __iter__(self):
        return self

    def __next__(self):
        self._id += 1
        if self._id > len(self.coeffs):
            raise StopIteration("Out of range")
        return f"({self._id - 1}, {self.coeffs[self._id - 1]})"
        
        
pol1 = Polynomial(0)
print(pol1)


pol2 = Polynomial(1,2,3)
print(pol2.__repr__())
print(pol2.__str__())
pol2

pol2 = Polynomial({0:6, 3:5, 4:6})
print(pol2)



pol3 = Polynomial([1, 2, 3, 4, 0, 7])
pol4 = Polynomial(pol3) * 2
print(pol3, pol4)
print(pol3 + pol4)
print(pol3 - pol4)
print(pol3 * pol4)


pol5 = Polynomial([1,2,3])
pol6 = Polynomial([6,5,6])
print(pol5 * pol6)
print(pol5(1))
print(pol4.degree())
print(pol3.der(2))

for k in pol4:
  print(k)


pol8 = Polynomial(1,2,3,4,5)
pol9 = Polynomial(pol8) 
print(pol8 == pol9)
pol9 *=2
print(pol8 == pol9)


pol10 = Polynomial([1,2,3])
print(pol10 - 5)
