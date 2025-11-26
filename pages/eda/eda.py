import streamlit as st
import io

@st.cache_data
def process_eda_page():
    st.header("Общая информация о данных")
    st.write(
        """
        * id - порядковый номер
        * Gender - пол
        * Age - возраст
        * Driving_License - наличие ВУ
        * Region_Code - код региона
        * Previously_Insured - застраховано ли ранее ТС
        * Vehicle_Age - возраст ТС
        * Vehicle_Damage - происходили ли ранее ДТП
        * Annual_Premium - страховая премия
        * Policy_Sales_Channel - идентификатор продавца
        * Vintage - количество дней страхования в компании
        * Response - ответил ли страхователь на предложение
        """
    )

    df = st.session_state["df"]

    st.write(df.head())
    st.write(df.compute().shape)
    st.write(
        """
            **Размер датасета:**
            - 11 504 798 - строк
            - 11 - столбцов
        """
    )

    buffer = io.StringIO()
    df.info(buf=buffer, verbose=True)
    s = buffer.getvalue()
    st.text(s)

    st.text(f"Дубликаты: {df.compute().duplicated().sum()}")

    st.write(
        """
            **Вывод:**
            - 3 object
            - 5 int64
            - 3 float64
            - Пропуски отсутствуют
            - Дубликаты отсутствуют
        """
    )

    st.subheader("Разделение на категории")

    st.code(
        """
            num_columns    = ["Age", "Annual_Premium", "Vintage"] # числовые
            cat_colums     = ["Region_Code", "Vehicle_Age", "Policy_Sales_Channel"] # категориальные
            binary_columns = ["Gender", "Driving_License", "Previously_Insured", "Vehicle_Damage", "Response"] # категориальные-бинарные
        """,
        language="python",
        line_numbers=True,
    )

    st.write(
        """
            **Вывод:**
            - 3 числовых
            - 8 категориальных
        """
    )

if __name__ == "__main__":
    process_eda_page()
