import pandas as pd
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import dask.dataframe as dd

data_file_path = "https://media.githubusercontent.com/media/taysumova/urfu_ml/refs/heads/main/data_sources/train.csv"
# data_file_path = "./data_sources/train.csv"
pd.set_option("display.float_format", lambda x: f"{x:,.2f}")


@st.cache_data
def load_dataset():
    df = dd.read_csv(data_file_path)
    st.session_state.df = df.set_index("id")

    return df


def show_main_page():
    st.set_page_config(
        layout="wide",
        initial_sidebar_state="auto",
        page_title="Бинарная классификация перекрёстных продаж страхования",
    )

    st.write(
        """
        ## Бинарная классификация перекрёстных продаж страхования (Кейс 10)
        """
    )


def process_pages():
    pages = {
        "О команде": [st.Page("pages/about.py", title="Общая информация")],
        "EDA": [
            st.Page("pages/eda/eda.py", title="Общая информация о данных"),
            st.Page("pages/eda/target.py", title="Целевая переменная"),
            st.Page("pages/eda/features.py", title="Категориальные признаки"),
        ],
        "Model": [
            st.Page("pages/model/model.py", title="Baseline model"),
        ],
        "Итоги": [st.Page("pages/summary/summary.py", title="Выводы")],
    }

    pg = st.navigation(pages)
    pg.run()


def process_main_page():
    show_main_page()
    load_dataset()
    process_pages()


if __name__ == "__main__":
    process_main_page()
