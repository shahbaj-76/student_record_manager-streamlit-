import streamlit as st
st.title("Student Record Manager ")
if "students" not in st.session_state:
    st.session_state.students=[]

name=st.text_input("Enter name of student: ")
marks=st.number_input("Enter total marks of student")

if st.button("Save"):
    student={"name": name,
             "marks": marks}
    st.session_state.students.append(student)
    st.success("Student Saved!")
for student in st.session_state.students:
    st.write(f"{student['name']}- {student['marks']}")

student_search=st.text_input("Enter the student name to search: ")
if st.button("Search"):
    found=False
    for student in st.session_state.students:        
        if student["name"]== student_search:
            st.success("Found!")
            st.write(f"Name: {student['name']}-Marks:{student['marks']}")
            found= True
            break
    if found == False:
        st.error("Not found")
if st.button("Find Topper"):
    if len(st.session_state.students)>0:
        topper= st.session_state.students[0]
        for student in st.session_state.students:
            if student["marks"]>topper["marks"]:
                topper=student
        st.success("Topper Found!")
        st.write(f"Topper: {topper['name']} - Marks: {topper['marks']}")
    else:
        st.error("No students saved")
if st.button("Average marks"):
    total=0
    for student in st.session_state.students:
        total+=student['marks']
    if len(st.session_state.students)>0:
        average= total/len(st.session_state.students)
        st.success("Average found")
        st.write(f"Average marks : {average}")
    else:
        st.error("Can't divide with zero")
if st.button("Total students "):
    st.write(len(st.session_state.students))      
if st.button("Clear all records"):
    st.session_state.students=[]
    st.success("All record cleared successfully")