import pandas as pd
import streamlit as st

df = pd.DataFrame({
    'sales': [100, 150, 200, 250],
    'month': ['Jan', 'Feb', 'Mar', 'Apr']
})


def process_main_page():
    show_main_page()
    process_tabs()


def show_main_page():
    st.set_page_config(
        layout="wide",
        initial_sidebar_state="auto",
        page_title="Бинарная классификация перекрёстных продаж страхования"
    )

    st.write(
        """
        # Бинарная классификация перекрёстных продаж страхования
        """
    )


def process_tabs():
    tab1, tab2, tab3, tab4 = st.tabs(["О команде", "EDA", "Model", "Итоги"])
    members = ['Мартынов Дмитрий', 'Осипов Роман', 'Иванков Дмитрий', 'Плахотин Андрей', 'Максим Макаров', 'Тайсумова Луиза']

    with tab1:
        st.header("Команда \"Страховщики\"")

        for i in members:
            st.markdown("- " + i)

    with tab2:
        st.header("Tab 2")
        st.write("This is the content of tab 2")
        st.header("Raw Data")

    with tab3:
        st.write("Coming soon")

    with tab4:
        st.write("Coming soon")

if __name__ == "__main__":
    process_main_page()