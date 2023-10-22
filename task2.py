salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
k_increase = increase + 1

res = 0  # Подушка безопасности
for _ in range(months):
    res += spend - salary
    spend *= k_increase

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {res:.02f}")
