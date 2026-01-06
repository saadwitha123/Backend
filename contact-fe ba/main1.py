import requests
import streamlit as st

base_url = "http://127.0.0.1:8000"

res = requests.get(base_url + "/contacts")
data = res.json()

# st.write(data)

@st.dialog('Add contact')
def add_contact_popup():
  name = st.text_input('Enter name', placeholder = 'Enter Here')
  phone = st.text_input('phone',placeholder = 'Enter Here')
  is_c = st.button('Create contacts', type= 'primary', use_container_width=True)
  if is_c:
    d ={'name':name, 'phone': phone}
    res = requests.post(base_url + '/add/contact', json=d)
    st.rerun()
    

cols=st.columns([1,1,1])
# st.header('Contact')
# st.button(' + add contact')


with cols[0]:
  st.subheader('Contacts')


with cols [2]:
  is_clicked = st.button('+ Add contact', type = 'primary', use_container_width=True)
  if is_clicked:
    add_contact_popup()

st.divider()
# [
#   {
#     "id": 1,
#     "created_at": "2026-01-03T05:27:07.936965+00:00",
#     "name": "Munna",
#     "phone": 9876543210
#   },
#   {
#     "id": 3,
#     "created_at": "2026-01-03T14:43:45.0492+00:00",
#     "name": "kiran",
#     "phone": 7788996655
#   },
#   {
#     "id": 2,
#     "created_at": "2026-01-03T14:10:44.009209+00:00",
#     "name": "swathi",
#     "phone": 6543210987
#   },
#   {
#     "id": 4,
#     "created_at": "2026-01-05T13:20:14.949148+00:00",
#     "name": "teju",
#     "phone": 8888666634
#   },
#   {
#     "id": 5,
#     "created_at": "2026-01-05T13:20:39.82943+00:00",
#     "name": "ruchi",
#     "phone": 9999777666
#   }
# ]

for c in data:
 with st.container(border=True):
  st.write(f"{c['name']} | {c['phone']}")
  st.button('update', key=c['name'])
  st.button('delete', key=c['id'])

