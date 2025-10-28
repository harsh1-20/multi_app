import streamlit as st
import calendar
import datetime
import requests
from icalendar import Calendar
from io import BytesIO

def show_calendar():
    st.set_page_config(page_title="🗓️ Indian Holiday Calendar", layout="centered")

    st.title("🗓️ Indian Holiday Calendar")
    st.write("View monthly calendar with public holidays marked in red!")

    # Sidebar to select month & year
    st.sidebar.header("Select Month & Year")
    year = st.sidebar.number_input("Year", min_value=1900, max_value=2100, value=datetime.datetime.now().year)
    month = st.sidebar.selectbox("Month", list(calendar.month_name)[1:], index=datetime.datetime.now().month - 1)

    # Fetch holidays from Google Calendar (India)
    url = "https://calendar.google.com/calendar/ical/en.indian%23holiday%40group.v.calendar.google.com/public/basic.ics"

    try:
        response = requests.get(url)
        cal = Calendar.from_ical(BytesIO(response.content).read())

        holidays = {}
        for event in cal.walk('vevent'):
            summary = str(event.get('summary'))
            date = event.get('dtstart').dt
            if isinstance(date, datetime.date):
                holidays[date] = summary

    except Exception as e:
        st.error(f"⚠️ Could not load holidays: {e}")
        holidays = {}

    # Generate calendar
    st.subheader(f"{month} {year}")
    cal_data = calendar.monthcalendar(year, list(calendar.month_name).index(month))

    # Display in grid
    st.markdown("<style>table, th, td {border:1px solid #555; padding:4px; text-align:center;} th {background:#eee;}</style>", unsafe_allow_html=True)

    table_html = "<table><tr>"
    for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
        table_html += f"<th>{day}</th>"
    table_html += "</tr>"

    for week in cal_data:
        table_html += "<tr>"
        for day in week:
            if day == 0:
                table_html += "<td></td>"
            else:
                date_obj = datetime.date(year, list(calendar.month_name).index(month), day)
                if date_obj in holidays:
                    table_html += f"<td style='color:red;font-weight:bold'>{day}<br><small>{holidays[date_obj]}</small></td>"
                else:
                    table_html += f"<td>{day}</td>"
        table_html += "</tr>"

    table_html += "</table>"
    st.markdown(table_html, unsafe_allow_html=True)
