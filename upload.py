import streamlit as st
import os
from zipfile import ZipFile
upload_dir = "上传的文件"
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

choise = st.sidebar.radio("选择操作", ["上传", "提取"])
def save(uploaded_file):
    with open(os.path.join(upload_dir, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"文件 {uploaded_file.name} 上传成功")

if choise == "上传":
    uploaded_file = st.file_uploader("选择一个文件", type=["png", "jpg", "jpeg", "gif", "bmp", "tiff", "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt", "rtf", "csv", "html", "htm", "xml", "json", "zip", "rar", "7z", "mp3", "wav", "flac", "mp4", "mkv", "avi", "mov", "wmv", "php", "js", "css", "py", "java", "c", "cpp", "h", "hpp", "svg", "ico"])
    if uploaded_file is not None:
        save(uploaded_file)
elif choise == "提取":
    password = st.text_input("请输入提取密码:", type="password")
    if password == '1128':
        zip_filename = "上传的文件.zip"

        with ZipFile(zip_filename, 'w') as zip_file:
            for folder, subfolders, filenames in os.walk(upload_dir):
                for filename in filenames:
                    file_path = os.path.join(folder, filename)
                    zip_file.write(file_path, os.path.relpath(file_path, upload_dir))

        with open(zip_filename, "rb") as f:
            btn = st.download_button(
                label="下载上传的文件",
                data=f,
                file_name=zip_filename,
                mime="application/zip"
            )
        st.success("文件成功打包，可下载")
    elif password:
        
        st.error("密码错误")

        
