import math

class Kolejka:
    def __init__(self):
        # ogólne -----------------------------------------
        self.lambda_val = 0
        self.mju = 0  # μ ogólna zdolność obsługi
        self.rho = 0  # ρ ogólny współczynnik wykorzystania systemu
        self.m = 0
        self.N = 0
        self.r = 0
        self.c1 = 0
        self.c2 = 0
        # END ogólne -------------------------------------

        # Które wynikają z ogólnych ----------------------
        self.p_0 = 0  # Prawdopodobieństwo że kolejka jest pusta
        self.listaPrawdopodopienstw = []
        self.p_odmowy = 0  # Prawdopodobieństwo odmowy
        self.q = 0  # Względna zdolność obsługi
        self.A = 0  # Bezwzględna zdolność obsługi
        self.m0 = 0  # Średnia ilość zajętych kanałów obsługi
        self.v = 0  # średnia ilość zgłoszeń w kolejce
        self.n = 0  # Średnia liczba zgłoszeń w systemie
        self.tf = 0  # Średni czas oczekiwania zgłoszenia w kolejce
        self.ts = 0  # Średni czas przebywania zgłoszenia

    def obliczTs(self):
        # TODO: 12.06.2023 trzeba sprawdzić, czy pobierane prawdopodobieństwo jest dobre (indeksowanie itp)
        skladnikDodawania1, skladnikDodawania2, licznik2, mianownik2 = 0, 0, 0, 0
        skladnikDodawania1 = self.v / self.lambda_val
        licznik2 = self.rho * (1 - self.listaPrawdopodopienstw[self.m + self.N - 1])
        mianownik2 = self.mju
        skladnikDodawania2 = licznik2 / mianownik2
        return skladnikDodawania1 + skladnikDodawania2

    def obliczTf(self):
        if self.rho == self.m:
            licznik, mianownik, tf = 0, 0, 0
            licznik = math.pow(self.m, self.m) * self.N * (self.N - 1) * self.p_0
            mianownik = self.lambda_val * self.silnia(self.m) * 2
            tf = licznik / mianownik
            return tf
        else:
            licznik, mianownik, tf = 0, 0, 0
            licznik = math.pow(self.rho, self.m + 1) * (1 - math.pow((self.rho / self.m), self.N)) * (
                        self.N * (1 - self.rho / self.m) + 1) * self.p_0
            mianownik = self.lambda_val * self.silnia(self.m - 1) * math.pow(self.m - self.rho, 2)
            tf = licznik / mianownik
            return tf

    def obliczN(self):
        return self.v + self.m0

    def obliczV(self):
        if self.rho != self.m:
            v = 0
            czlon1, licznik1, mianownik1, czlon2, licznik2, mianownik2 = 0, 0, 0, 0, 0, 0
            licznik1 = math.pow(self.rho, self.m + 1) * self.p_0
            mianownik1 = self.silnia(self.m - 1)
            czlon1 = licznik1 / mianownik1

            licznik2 = 1 - math.pow((self.rho / self.m), self.N) * (self.N * (1 - self.rho / self.m) + 1)
            mianownik2 = math.pow(self.m - self.rho, 2)
            czlon2 = licznik2 / mianownik2

            v = czlon1 * czlon2
            return v
        else:
            v = 0
            czlon1, licznik, mianownik = 0, 0, 0
            licznik = math.pow(self.m, self.m) * self.N * (self.N + 1) * self.p_0
            mianownik = self.silnia(self.m) * 2
            v = licznik / mianownik
            return v

    def obliczM0(self):
        return self.A / self.mju

    def obliczA(self):
        return self.lambda_val * self.q

    def obliczQ(self):
        return 1 - self.p_odmowy

    def obliczP_0(self):
        # q1 - iloraz ciągu geometrycznego
        q1 = self.rho / self.m
        if q1 == 0:
            suma = 0
            skladnikDodawania1, skladnikDodawania2, licznik1, licznik2, mianownik1, mianownik2 = 0, 0, 0, 0, 0, 0
            for k in range(0, self.m):
                licznik1 = math.pow(self.rho, k)
                mianownik1 = self.silnia(k)

                licznik2 = math.pow(self.rho, self.m) * (self.N + 1)
                mianownik2 = self.silnia(self.m)

                skladnikDodawania1 = licznik1 / mianownik1
                skladnikDodawania2 = licznik2 / mianownik2
                suma += skladnikDodawania1 + skladnikDodawania2
            suma = math.pow(suma, -1)
            return suma
        else:
            suma = 0
            skladnikDodawania1, skladnikDodawania2, licznik1, licznik2, mianownik1, mianownik2 = 0, 0, 0, 0, 0, 0
            for k in range(0, self.m):
                licznik1 = math.pow(self.rho, k)
                mianownik1 = self.silnia(k)

                licznik2 = math.pow(self.rho, self.m) * (1 - math.pow(self.rho / self.m, self.N + 1))
                mianownik2 = self.silnia(self.m) * (1 - self.rho / self.m)

                skladnikDodawania1 = licznik1 / mianownik1
                skladnikDodawania2 = licznik2 / mianownik2
                suma += skladnikDodawania1 + skladnikDodawania2
            suma = math.pow(suma, -1)
            return suma

    def obliczPrawdopodobienstwa(self):
        listaPrawdopodobienstwToReturn = []
        # dla przedziału: 1 <= k <= m - 1 -----------------------------
        for k in range(1, self.m):
            prawdopodobienstwo_k, licznik, mianownik = 0, 0, 0
            licznik = math.pow(self.rho, k) * self.p_0
            mianownik = self.silnia(k)
            prawdopodobienstwo_k = licznik / mianownik
            # TODO: 12.06.2023 można tutaj zaokrąglić wynik przed dodaniem
            listaPrawdopodobienstwToReturn.append(prawdopodobienstwo_k)

        # dla przedziału: m <= j <= m + N -----------------------------
        for j in range(self.m, self.m + self.N):
            prawdopodobienstwo_j, licznik, mianownik = 0, 0, 0
            licznik = math.pow(self.rho, j) * self.p_0
            mianownik = math.pow(self.m, j - self.m) * self.silnia(self.m)
            prawdopodobienstwo_j = licznik / mianownik
            # TODO: 12.06.2023 można tutaj zaokrąglić wynik przed dodaniem
            listaPrawdopodobienstwToReturn.append(prawdopodobienstwo_j)

        return listaPrawdopodobienstwToReturn

    def obliczRho(self):
        return self.lambda_val / self.mju

    def obliczP_odmowy(self):
        ulamek, licznik, mianownik = 0, 0, 0
        licznik = math.pow(self.rho, self.m + self.N) * self.p_0
        mianownik = math.pow(self.m, self.N) * self.silnia(self.m)
        ulamek = licznik / mianownik
        return ulamek

    @staticmethod
    def silnia(x):
        if x == 0:
            return 1
        factorial = 1
        for i in range(2, x + 1):
            factorial *= i
        return factorial

    def __init__(self, lambda_val, mju, m, N):
        self.lambda_val = lambda_val
        self.mju = mju
        self.m = m
        self.N = N

        self.rho = self.obliczRho()
        self.p_0 = self.obliczP_0()
        self.listaPrawdopodopienstw = self.obliczPrawdopodobienstwa()
        self.p_odmowy = self.obliczP_odmowy()
        self.q = self.obliczQ()
        self.A = self.obliczA()
        self.m0 = self.obliczM0()
        self.v = self.obliczV()
        self.n = self.obliczN()
        self.tf = self.obliczTf()
        self.ts = self.obliczTs()

    # Konstruktor do funkcji celu
    def __init__(self, lambda_val, mju, r, c1, c2):
        self.lambda_val = lambda_val
        self.mju = mju
        self.r = r
        self.c1 = c1
        self.c2 = c2

        self.rho = self.obliczRho()
        # TODO: 12.06.2023 do wykminienia
