import streamlit as st
import pandas as pd

st.set_page_config(page_title='РГР по машинному обучению')
st.title('Интерфейс моделей и анализ данных')
df = pd.read_csv("./data/weatherAUS.csv")

st.subheader('Чему посвящен датасет')
st.markdown('Модели были обучены на наборе данных *Rain in Australia*. Этот набор данных содержит данные ежедневных наблюдений за погодой за 10 лет из многих мест по всей Австралии. Фрагмент датасета представлен ниже.')
st.write(df.head())

st.subheader('Признаки')
select_event = st.selectbox('Выберите набор признаков', ('Местоположение', 'Климатические условия за весь день', 'Климатические условия на промежутках', 'Осадки'))
if select_event == 'Местоположение':
    st.markdown('+ *Date*: дата наблюдения')
    st.markdown('+ *Location*: общее название местоположения метеостанции')
if select_event == 'Климатические условия на промежутках':
    st.markdown('+ *WindDir9am*: направление ветра в 9 утра')
    st.markdown('+ *WindDir3pm*: направление ветра в 3 часа дня')
    st.markdown('+ *WindSpeed9am*: скорость ветра (км/час) в среднем составляла более 10 минут до 9 утра')
    st.markdown('+ *WindSpeed3pm*: скорость ветра (км/час) в среднем за 10 минут до 15:00')
    st.markdown('+ *Humidity9am*: влажность (в процентах) в 9 утра')
    st.markdown('+ *Humidity3pm*: влажность (в процентах) в 3 часа дня')
    st.markdown('+ *Pressure9am*: атмосферное давление (гпа) снизилось до среднего уровня моря в 9 утра')
    st.markdown('+ *Pressure3pm*: атмосферное давление (гпа) снизилось до среднего уровня моря в 3 часа дня')
    st.markdown('+ *Cloud9am*: часть неба, затянутая облаками в 9 утра. Это измеряется в "октах", которые представляют собой единицу измерения, равную восьми.')
    st.markdown('+ *Cloud3pm*: часть неба, закрытая облаками (в "октасе": восьмые доли) в 3 часа дня. Описание значений смотрите в разделе Облачно в 9 утра')
    st.markdown('+ *Temp9am*: температура (градусы по Цельсию) в 9 утра')
    st.markdown('+ *Temp3pm*: температура (градусы по Цельсию) в 3 часа дня')
if select_event == 'Климатические условия за весь день':
    st.markdown('+ *MinTemp*: минимальная температура в градусах Цельсия')
    st.markdown('+ *MaxTemp*: максимальная температура в градусах Цельсия')
    st.markdown('+ *Sunshine*: количество часов яркого солнечного света в течение дня')
    st.markdown('+ *WindGustDir*: направление самого сильного порыва ветра за 24 часа до полуночи')
    st.markdown('+ *WindGustSpeed*: скорость (км/ч) самого сильного порыва ветра за 24 часа до полуночи')
if select_event == 'Осадки':
    st.markdown('+ *Rainfall*: количество осадков, выпавших за день, в мм')
    st.markdown('+ *Evaporation*: испарение в поддоне класса А (мм) за 24 часа до 9 утра')
    st.markdown('+ *RainToday*: логическое значение - 1, если количество осадков (мм) за 24 часа до 9 утра превысит 1 мм, в противном случае 0')
    st.markdown('+ *RainTomorrow*: Количество осадков на следующий день в мм. Используется для создания переменной ответа *Rain Tomorrow*. Своего рода мера "риска".')


st.subheader('Особенности предобработки данных')
st.text('Можно выделить несколько этапов:')
st.markdown('1. Работа со столбцом *Date*. Был разделен на три отдельных признака. После столбец был удален.')
st.markdown('2. Обработка целевого признака *RainTomorrow*, замена категорий логическими значениями.')
st.markdown('3. *One-Hot Encoding* категориальных признаков. В них входят: *WindGustDir*, *WindDir9am*, *WindDir3pm*, *RainToday*.')
st.markdown('4. Заполнение пропущенных значений средним по столбцу.')
st.markdown('5. Приведение всех данных к типу *float*.')
st.markdown('6. Масштабирование признаков.')
st.markdown('7. Балансировка.')
st.markdown('8. Уменьшение признакового пространства со 120 признаков до 15 с помощью ранжирования признаков *Recursive Feature Elimination* через дерево решений *Decision Tree Classifier*.')
df1 = pd.read_csv("./data/weather_data1.csv")

st.text('Фрагмент обработанного датасета для обучения моделей представлен ниже.')
st.write(df1.head())