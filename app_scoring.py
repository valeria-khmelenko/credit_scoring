import streamlit as st
import pandas as pd
import pickle
import sklearn
from PIL import Image

with open('model_RF_scoring.pickle', 'rb') as md:
    model = pickle.load(md)


st.title("Прогноз платежеспособности клиента банка")

st.header("Проверьте, стоит ли выдавать клиенту банка новый кредит")


img = Image.open('images/main_image.jpeg')
st.image(img, width=400)

with st.sidebar:
    age = st.slider('Выберете возраст клиента', min_value=18, max_value=100, step=1)

    depends = st.slider('Выберете количество иждивенцев на попечении клиента', min_value=0, max_value=30, step=1)

    monthly_income = st.number_input('Введите сумму ежемесячного дохода клиента', min_value=0.0001)

    monthly_expenses = st.number_input('Введите сумму ежемесячных расходов клиента', min_value=0.0)

    balance = st.number_input('Введите общий баланс средств клиента на всех картах', min_value=0.0)

    loans_number = st.number_input('Введите количество открытых кредитов клиента, включая кредитные карты', min_value=0)

    impairment_loans = st.slider('Выберете, сколько раз за последние 2 года клиент задержал платеж от 30 до 89 дней', min_value=0)

    npl = st.slider('Выберете, сколько раз наблюдалась просрочка клиента на 90 дней и более', min_value=0)

    debt_ratio = monthly_expenses / monthly_income

    overdue_ratio = npl * loans_number

    net_balance = monthly_income - monthly_expenses + balance

    run_button = st.button('Построить прогноз')

if run_button:
    params = {
        'RevolvingUtilizationOfUnsecuredLines': [balance],
        'age': [age],
        'DebtRatio': [debt_ratio],
        'MonthlyIncome': [monthly_income],
        'NumberOfOpenCreditLinesAndLoans': [loans_number],
        'NumberOfDependents': [depends],
        'NumberOfTime30-89DaysPastDueNotWorse': [impairment_loans],
        'MonthlyExpenses': [monthly_expenses],
        'NetBalance': [net_balance],
        'OverdueRatio': [overdue_ratio]
    }
    df = pd.DataFrame.from_dict(params)
    rjt = model.predict(df)[0]
    
    st.header('Результат')
    
    if rjt:
        st.error('Рекомендуется отказать клиенту в новом кредите')
        img = Image.open('images/rejected.png')
        st.image(img, width=50)
    else:
        st.success('Новый кредит может бьть выдан клиенту')
        img = Image.open('images/approved.jpg')
        st.image(img, width=50)
