import streamlit as st
import matplotlib.pyplot as plt
from threading import RLock

_lock = RLock()


@st.cache_data
def process_target_page():
    st.header("Анализ целевой переменной")

    df = st.session_state["df"]
    response_counts = df["Response"].compute().value_counts().sort_index()
    total_count = len(df)
    percentages = (response_counts / total_count) * 100

    col1, col2, col3 = st.columns(3)

    with col2:
        with _lock:
            fig = plt.figure(figsize=(2, 5))
            plt.bar(percentages.index.astype(str), percentages.values)
            plt.title("Гистограмма распределения целевой переменной")
            plt.xlabel("Ответил ли страхователь на предложение")
            plt.ylabel("Процент, %")
            plt.xticks(percentages.index, ["Нет", "Да"])
            plt.grid(axis="y", alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig)

    st.write(
        """
            **Вывод:**
            Сильный дисбаланс классов: 85% клиентов отвечают «Нет», 15% — «Да».
            Это может привести к смещению модели в сторону "Нет", если не использовать правильные метрики и методы балансировки.
            Модель должна быть обучена не на точности (accuracy), а на способности находить редкие положительные случаи.
        """
    )


if __name__ == "__main__":
    process_target_page()
