# import streamlit as st

# st.header("Hello Wellcome")
# st.button("click me")
# st.radio("select me", ["option 1", "option 2"])
# st.text_input("Enter here")
# st.toggle("ON")
# # st.balloons()
# st.bar_chart()
# st.checkbox("Check it")

# text_data = "This is my file content"
# st.download_button(label="Download the file",
#     data=text_data,
#     file_name="output.txt",
#     mime="text/plain")




import requests
import streamlit as st

base_url = "http://127.0.0.1:8000/"

res = requests.get(base_url + "/tasks")
data = res.json()
# st.write(data)




# st.header('Taskify')
# st.button('+ Add Task')

@st.dialog('Add Task')
def add_task_popup():
   title = st.text_input('Enter title',placeholder='Enter here')
   status = st.selectbox('status', ['Not started', 'In progress', 'Done'])
   is_c=st.button('Create Task',type='primary',use_container_width=True)
   if is_c:
      d = {'title':title, 'status':status}
      res=requests.post(base_url + '/add/task',json=d)
      st.rerun()

cols = st.columns([1,2,1])

with cols[0]:
    st.subheader('TASKIFY')

with cols[2]:
    is_clicked = st.button("+ Add Task", type='primary',use_container_width=True)
    if is_clicked:
       add_task_popup()

st.divider()

# base_url = "http://127.0.0.1:8000/"


# res = requests.get(base_url + "/tasks")
# data = res.json()

for i,t in enumerate(data):
  with st.container(border=True):
    st.write(f"{t['title']} | {t['status']}")
    st.button('update', key=f"update_{i}")
    st.button('Delete',key=f"delete_{i}")

