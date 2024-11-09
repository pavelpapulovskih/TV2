from scipy.stats import poisson
# Данные задачи
n = 5000 # количество лампочек
p = 0.0004 # вероятность перегорания
λ = n * p # параметр λ (среднее число событий)
# Вероятность, что ни одна лампочка не перегорит
probability_no_failures = poisson.pmf(0, λ)
print(f"Вероятность того, что ни одна лампочка не перегорит:{probability_no_failures:.5f}")
# Вероятность, что перегорят ровно две лампочки
probability_two_failures = poisson.pmf(2, λ)
print(f"Вероятность того, что перегорят ровно две лампочки:{probability_two_failures:.5f}")