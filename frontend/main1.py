import requests
import streamlit as st

base_url = "http://127.0.0.1:8000"

res = requests.get(base_url + "/contacts")
data = res.json()
# st.write(data)



@st.dialog('Add Task')
def add_task_popup():
   title = st.text_input('Enter title',placeholder='Enter here')
   status = st.text_input('Enter phone number')
   is_c=st.button('Create Task',type='primary',use_container_width=True)
   if is_c:
      d = {'title':title, 'status':status}
      requests.post(base_url + '/add/contact',json=d)
      st.rerun()

cols = st.columns([1,2,1])

with cols[0]:
    st.subheader('TASKIFY')

with cols[2]:
    is_clicked = st.button("+ Add Task", type='primary',use_container_width=True)
    if is_clicked:
       add_task_popup()

st.divider()


for i,t in enumerate(data):
  with st.container(border=True):
    st.write(f"{t['title']} | {t['status']}")
    st.button('update', key=f"update_{i}")
    st.button('Delete',key=f"delete_{i}")