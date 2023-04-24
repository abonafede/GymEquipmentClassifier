import streamlit as st
import pandas as pd
import json
from datetime import date

WORKOUTS_FILE_PATH = 'db/workouts.json'

with open(WORKOUTS_FILE_PATH, 'r') as f:
    workout_data = json.load(f)

def get_previous_workouts(username):
    if username in workout_data:
        dfs = []
        for i in range(len(workout_data[username])):
            df = pd.DataFrame.from_dict(workout_data[username][i], orient='index')
            dfs.append(df)
        history = pd.concat(dfs)
        return history
    else:
        return "You have no workouts with saved with us"

def recommend():
    df = st.session_state.df
    workout = { str(date.today()): { "Excersise1": df['Title'].sample().values[0], "Sets1":5, "Reps1":[5,5,3,3,1],"Weights1":[135,185,225,225,225], "Excersise2": df['Title'].sample().values[0], "Sets2":5, "Reps2":[5,5,3,3,1],"Weights2":["BW","BW","BW","BW","BW"]} }
    return workout


def save_workout(username,workout):
    if username not in workout_data:
        workout_data[username] = workout
        with open(WORKOUTS_FILE_PATH, 'w') as f:
            json.dump(workout_data, f)
        st.success("Workout Saved!")
    else:
        workout_data[username].append(workout)
        with open(WORKOUTS_FILE_PATH, 'w') as f:
            json.dump(workout_data, f)
        st.success("Workout Added!")


def workouts():
    st.title("Recommended Workouts")
    st.markdown("---")
    if not st.session_state.equipment:
        st.markdown("Please upload photos of your equipment to get a recommended workout")
    else:
        workout = recommend()
        st.write(pd.DataFrame.from_dict(workout,orient='index'))
        rating = st.slider("Please rate this workout",
                            min_value=1,
                            max_value=5,
                            value=None,
                            step=1)
        submit = st.button('submit')
        if submit:
            workout[str(date.today())]['Rating'] = rating
            save_workout(st.session_state.username,workout)

    st.header("Previous Workouts")
    if not st.session_state.is_logged_in:
        st.markdown("Please sign in to see previous workouts")
    else:
        workouts = get_previous_workouts(st.session_state.username)
        st.write(workouts)

if __name__ == '__main__':
    workouts()