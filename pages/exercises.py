import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    modify = st.checkbox("Add additional filters")

    if not modify:
        return df
    df = df.copy()

    # Try to convert datetimes into a standard format (datetime, no timezone)
    for col in df.columns:
        if is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            # Treat columns with < 10 unique values as categorical
            if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                df = df[df[column].isin(user_cat_input)]
            elif is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Values for {column}",
                    min_value=_min,
                    max_value=_max,
                    value=(_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            elif is_datetime64_any_dtype(df[column]):
                user_date_input = right.date_input(
                    f"Values for {column}",
                    value=(
                        df[column].min(),
                        df[column].max(),
                    ),
                )
                if len(user_date_input) == 2:
                    user_date_input = tuple(map(pd.to_datetime, user_date_input))
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            else:
                user_text_input = right.text_input(
                    f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = df[df[column].astype(str).str.contains(user_text_input)]
    return df

def match(array):
    new = []
    for i in array:
        if i == 'dumbell':
            new.append('Dumbbell')
        elif i == 'barbell':
            new.append('Barbell')
        elif i =='kettlebell':
            new.append('Kettlebells')
        else:
            new.append(i)
    return new
        
def display_exercises():
    st.title("Exercise List")
    if st.session_state.equipment:
        if st.button('Recommended Workout'):
            switch_page('recommendations')
    st.markdown("---")
    
    if 'df' not in st.session_state:
        df = pd.read_csv('exercises.csv')
        df = df.drop('Unnamed: 0',axis=1)
        st.session_state.df = df

    df = st.session_state.df

    if st.session_state['equipment'] is not None:
        equip = match(st.session_state['equipment'])
        key = '|'.join(equip)
        df = df[df['Equipment'].astype(str).str.contains(key)] 
        df = filter_dataframe(df)
        st.markdown(df.to_html(render_links=True),unsafe_allow_html=True)
    else:
        st.markdown("Please upload photos on the homepage to view exercises based on your available equipment.")
        st.markdown("---")
        df = filter_dataframe(df)
        st.markdown(df.to_html(render_links=True),unsafe_allow_html=True)

if __name__ == '__main__':
    display_exercises()