import pandas as pd
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
# import matplotlib.pyplot as plt

data_file_path = "https://media.githubusercontent.com/media/taysumova/urfu_ml/refs/heads/main/data_sources/train.csv"
chunksize = 10000


@st.cache_data
def load_large_dataset():
    chunks = []

    try:
        with st.spinner("Loading dataset..."):
            for chunk in pd.read_csv(data_file_path, chunksize=chunksize, index_col="id"):
                chunks.append(chunk)
            st.success("Dataset is successfully loaded")
    except Exception as e:
        print(f"An error occurred: {e}")

    return pd.concat(chunks, ignore_index=True)


def process_main_page():
    show_main_page()
    process_tabs()


def show_main_page():
    st.set_page_config(
        layout="wide",
        initial_sidebar_state="auto",
        page_title="Бинарная классификация перекрёстных продаж страхования",
    )

    st.write(
        """
        # Бинарная классификация перекрёстных продаж страхования
        """
    )


def process_tabs():
    tab1, tab2, tab3, tab4 = st.tabs(["О команде", "EDA", "Model", "Итоги"])
    members = [
        "Мартынов Дмитрий",
        "Осипов Роман",
        "Иванков Дмитрий",
        "Плахотин Андрей",
        "Максим Макаров",
        "Тайсумова Луиза",
    ]

    with tab1:
        st.header('Команда "Страховщики"')
        for i in members:
            st.markdown("- " + i)

    with tab2:
        pd.set_option("display.float_format", lambda x: f"{x:,.2f}")
        st.header("1. Общая информация о данных")
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

        # df = load_large_dataset()
        # st.write(df.head())
        # st.write(df.shape)
        st.write(
            """
                 **Размер датасета:**
                - 11 504 798 - строк
                - 11 - столбцов
            """
        )
        # st.write(df.info(verbose=True, show_counts=True))
        st.write(
            """
                 **Вывод:**
                - 3 object
                - 5 int64
                - 3 float64
                - Пропуски отсутствуют
            """
        )
        st.subheader("Разделение на категории")
        num_columns = ["Age", "Annual_Premium", "Vintage"]  # числовые
        cat_colums = [
            "Region_Code",
            "Vehicle_Age",
            "Policy_Sales_Channel",
        ]  # категориальные
        binary_columns = [
            "Gender",
            "Driving_License",
            "Previously_Insured",
            "Vehicle_Damage",
            "Response",
        ]  # категориальные-бинарные

        # @TODO - make automated count not like that hardcoded
        st.write(
            """
                - 3 числовых
                - 8 категориальных
            """
        )

    with tab3:
        st.write("Coming soon")

    with tab4:
        st.write("Coming soon")


if __name__ == "__main__":
    process_main_page()
