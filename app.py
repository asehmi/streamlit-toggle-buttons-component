import streamlit as st
from datetime import datetime

from frontend import component_toggle_buttons

if 'counter' not in st.session_state:
    st.session_state.counter = 0

def main():
    def run_component(props):
        value = component_toggle_buttons(key='toggle_buttons', **props)
        return value
    def handle_event(value):
        st.header('Streamlit')
        st.write('Received from component: ', value)

    st.title('Toggle Buttons Component Demo')
    st.session_state.counter = st.session_state.counter + 1
    props = {
        'initial_state': {
            'group_1_header': 'Choose an option from group 1',
            'group_2_header': 'Choose an option from group 2'
        },
        'counter': st.session_state.counter,
        'datetime': str(datetime.now().strftime("%H:%M:%S, %d %b %Y"))
    }

    handle_event(run_component(props))   

if __name__ == '__main__':
    main()
