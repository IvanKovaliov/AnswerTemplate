money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
k_increase = increase + 1

months = 1  # Количество месяцев
while money_capital >= spend:
    money_capital += salary - spend
    months += 1
    spend *= k_increase

print("Количество месяцев, которое можно протянуть без долгов:", months)
