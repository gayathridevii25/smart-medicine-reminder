import streamlit as st
import json
import os
from datetime import datetime, date
from pathlib import Path

st.set_page_config(
    page_title="MediMate",
    page_icon="💊",
    layout="centered"
)

st.title("💊 MediMate")
st.subheader("Smart Medicine Reminder")
st.write("Manage your medicine schedule in one place.")

st.info(
    "Reminder and educational demo only. "
    "Follow your doctor's prescribed instructions."
)

# Store demo data in a local JSON file
DATA_FILE = Path("medicines.json")

def load_medicines():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            return []
    return []

def save_medicines(items):
    DATA_FILE.write_text(json.dumps(items, indent=2))

if "medicines" not in st.session_state:
    st.session_state.medicines = load_medicines()

st.header("➕ Add Medicine Reminder")

with st.form("medicine_form"):
    name = st.text_input("Medicine name")
    dose = st.text_input("Dosage instructions")
    med_date = st.date_input("Start date", value=date.today())
    med_time = st.time_input("Reminder time")
    submitted = st.form_submit_button("Save Reminder")

    if submitted:
        if name.strip() and dose.strip():
            st.session_state.medicines.append({
                "name": name.strip(),
                "dose": dose.strip(),
                "date": med_date.isoformat(),
                "time": med_time.strftime("%H:%M")
            })
            save_medicines(st.session_state.medicines)
            st.success("Reminder added!")
        else:
            st.warning("Please enter medicine name and instructions.")

st.divider()
st.header("📋 My Reminders")

if not st.session_state.medicines:
    st.write("No reminders yet. Add your first medicine above.")

for i, med in enumerate(st.session_state.medicines):
    with st.container(border=True):
        st.markdown(f"**💊 {med['name']}**")
        st.write(f"Instructions: {med['dose']}")
        st.write(f"Start date: {med['date']}")
        st.write(f"Reminder time: {med['time']}")

        if st.button("Delete", key=f"delete_{i}"):
            st.session_state.medicines.pop(i)
            save_medicines(st.session_state.medicines)
            st.rerun()

st.divider()
st.caption(
    "MediMate is an educational prototype, not a medical device. "
    "It does not prescribe medicines or guarantee notifications."
)

import streamlit as st
import json
import os
from datetime import datetime, date
from pathlib import Path

st.set_page_config(
    page_title="MediMate",
    page_icon="💊",
    layout="centered"
)

st.title("💊 MediMate")
st.subheader("Smart Medicine Reminder")
st.write("Manage your medicine schedule in one place.")

st.info(
    "Reminder and educational demo only. "
    "Follow your doctor's prescribed instructions."
)

# Store demo data in a local JSON file
DATA_FILE = Path("medicines.json")

def load_medicines():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            return []
    return []

def save_medicines(items):
    DATA_FILE.write_text(json.dumps(items, indent=2))

if "medicines" not in st.session_state:
    st.session_state.medicines = load_medicines()

st.header("➕ Add Medicine Reminder")

with st.form(key="add_medicine_form_v2"):
    name = st.text_input("Medicine name")
    dose = st.text_input("Dosage instructions")
    med_date = st.date_input("Start date", value=date.today())
    med_time = st.time_input("Reminder time")
    submitted = st.form_submit_button("Save Reminder")

    if submitted:
        if name.strip() and dose.strip():
            st.session_state.medicines.append({
                "name": name.strip(),
                "dose": dose.strip(),
                "date": med_date.isoformat(),
                "time": med_time.strftime("%H:%M")
            })
            save_medicines(st.session_state.medicines)
            st.success("Reminder added!")
        else:
            st.warning("Please enter medicine name and instructions.")

st.divider()
st.header("📋 My Reminders")

if not st.session_state.medicines:
    st.write("No reminders yet. Add your first medicine above.")

for i, med in enumerate(st.session_state.medicines):
    with st.container(border=True):
        st.markdown(f"**💊 {med['name']}**")
        st.write(f"Instructions: {med['dose']}")
        st.write(f"Start date: {med['date']}")
        st.write(f"Reminder time: {med['time']}")

        if st.button("Delete", key=f"delete_{i}"):
            st.session_state.medicines.pop(i)
            save_medicines(st.session_state.medicines)
            st.rerun()

st.divider()
st.caption(
    "MediMate is an educational prototype, not a medical device. "
    "It does not prescribe medicines or guarantee notifications."
)
