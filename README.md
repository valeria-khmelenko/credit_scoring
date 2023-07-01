## Кредитный скоринг

### Цель проекта: по различным характеристикам клиентов спрогнозировать стоит ли выдавать кредит клиенту.


## Входящие данные
Датасет содержит информацию о клиентах некоторого банка.

Целевая переменная – SeriousDlqin2yrs: клиент имел просрочку 90 и более дней

Признаки:

1) RevolvingUtilizationOfUnsecuredLines: общий баланс средств

2) age: возраст заемщика

3) NumberOfTime30-59DaysPastDueNotWorse: сколько раз за последние 2 года наблюдалась просрочка 30-59 дней

4) DebtRatio: ежемесячные расходы (платеж по долгам, алиментам, расходы на проживания) деленные на месячный доход

5) MonthlyIncome: ежемесячный доход

6) NumberOfOpenCreditLinesAndLoans: количество открытых кредитов (напрмер, автокредит или ипотека) и кредитных карт

7) NumberOfTimes90DaysLate: сколько раз наблюдалась просрочка (90 и более дней)

8) RealEstateLoansOrLines: закодированное количество кредитов (в том числе под залог жилья) - чем больше код буквы, тем больше кредитов

9) NumberOfTime60-89DaysPastDueNotWorse: сколько раз за последние 2 года заемщик задержал платеж на 60-89 дней

10) NumberOfDependents: количество иждивенцев на попечении (супруги, дети и др)

11) GroupAge: закодированная возрастная группа - чем больше код, тем больше возраст

## Модель

В качестве финальной модели использовалась модель RandomForestClassifier(подбор гиперпараметров с помощью GridSearchCV).
Балансировка классов производилась с помощью downsampling.

## Метрика
ROC_AUC (0.77 на тестовой выборке)
