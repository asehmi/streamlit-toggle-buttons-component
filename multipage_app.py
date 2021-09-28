import streamlit as st

from frontend_multipage_app import component_multipage_app

class MultiPage:
    def __init__(self):
        self.apps = []
        self.app_names = []

    def add_app(self, title, func, *args, **kwargs):
        self.app_names.append(title)
        self.apps.append({
            "title": title,
            "function": func,
            "args":args,
            "kwargs": kwargs
        })

    def run(self, label='Go To'):
        def run_component(props):
            value = component_multipage_app(key='multipage_app', **props)
            return value
        def handle_event(value):
            # st.header('Streamlit')
            # st.write('Received from component: ', value)
            app_choice = value['choice']['state']['action'] if value else self.app_names[0]
            app_choice_status = value['choice']['state']['value'] if value else False
            if app_choice_status == True:
                # run the selected app
                app = self.apps[self.app_names.index(app_choice)]
                app['function'](app['title'], *app['args'], **app['kwargs'])
            else:
                st.write('Awaiting selection')

        props = {
            'initial_state': {
                'group_1_header': label
            }
        }
        handle_event(run_component(props))

def app1(title, info=None):
    st.title(title)
    st.write(info)
def app2(title, info=None):
    st.title(title)
    st.write(info)
def app3(title, info=None):
    st.title(title)
    st.write(info)

def main():
    mp = MultiPage()
    mp.add_app('Application 1', app1, info='Hello from App 1')
    mp.add_app('Application 2', app2, info='Hello from App 2')
    mp.add_app('Application 3', app3, info='Hello from App 3')
    mp.run('Launch Application')

if __name__ == '__main__':
    main()
