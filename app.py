import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cau hinh trang web
st.set_page_config(
    page_title="Quan ly diem sinh vien",
    page_icon="🎓",
    layout="wide"
)

# Tieu de
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.write("Ứng dụng quản lý, thống kê và xếp loại điểm sinh viên.")

# Du lieu mau gom 10 sinh vien
data = {
    "Ho_ten": [
        "Nguyen Van An",
        "Tran Thi Binh",
        "Le Van Cuong",
        "Pham Thi Dung",
        "Hoang Van Em",
        "Vo Thi Giang",
        "Dang Van Hung",
        "Bui Thi Lan",
        "Do Van Minh",
        "Nguyen Thi Nga"
    ],
    "Chuyen_can": [9, 8, 7, 10, 6, 9, 5, 8, 7, 10],
    "Giua_ky":    [8, 7, 6, 9, 5, 8, 4, 7, 6, 9],
    "Cuoi_ky":    [9, 8, 7, 9, 6, 9, 4, 8, 7, 10]
}

# Tao DataFrame
df = pd.DataFrame(data)

# Tinh diem tong ket
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
)

# Ham xep loai sinh vien
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 1. Hien thi bang diem
st.subheader("1. Bảng điểm 10 sinh viên")

bang_diem = df.rename(columns={
    "Ho_ten": "Họ tên",
    "Chuyen_can": "Chuyên cần",
    "Giua_ky": "Giữa kỳ",
    "Cuoi_ky": "Cuối kỳ",
    "Tong_ket": "Tổng kết",
    "Xep_loai": "Xếp loại"
})

st.dataframe(
    bang_diem.round({"Tổng kết": 2}),
    use_container_width=True,
    hide_index=True
)

# 2. Thong ke ket qua hoc tap
diem_tb = df["Tong_ket"].mean()
sv_cao_nhat = df.loc[df["Tong_ket"].idxmax()]
sv_thap_nhat = df.loc[df["Tong_ket"].idxmin()]
so_sv_dat = int((df["Tong_ket"] >= 5).sum())

st.subheader("2. Thống kê kết quả học tập")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Điểm trung bình", f"{diem_tb:.2f}")
c2.metric("Điểm cao nhất", f"{sv_cao_nhat['Tong_ket']:.2f}")
c3.metric("Điểm thấp nhất", f"{sv_thap_nhat['Tong_ket']:.2f}")
c4.metric("Số sinh viên đạt", f"{so_sv_dat}/10")

st.write(
    f"**Sinh viên cao nhất:** {sv_cao_nhat['Ho_ten']} "
    f"- {sv_cao_nhat['Tong_ket']:.2f} điểm"
)

st.write(
    f"**Sinh viên thấp nhất:** {sv_thap_nhat['Ho_ten']} "
    f"- {sv_thap_nhat['Tong_ket']:.2f} điểm"
)

# 3. Danh sach chon sinh vien
st.subheader("3. Tra cứu thông tin sinh viên")

ten_sv = st.selectbox(
    "Chọn một sinh viên:",
    df["Ho_ten"].tolist()
)

sv = df[df["Ho_ten"] == ten_sv].iloc[0]

st.write(f"**Họ tên:** {sv['Ho_ten']}")
st.write(f"**Điểm chuyên cần:** {sv['Chuyen_can']}")
st.write(f"**Điểm giữa kỳ:** {sv['Giua_ky']}")
st.write(f"**Điểm cuối kỳ:** {sv['Cuoi_ky']}")
st.write(f"**Điểm tổng kết:** {sv['Tong_ket']:.2f}")
st.write(f"**Xếp loại:** {sv['Xep_loai']}")

# 4. Ve bieu do cot
st.subheader("4. Biểu đồ điểm tổng kết của 10 sinh viên")

fig, ax = plt.subplots(figsize=(12, 5))

bars = ax.bar(
    df["Ho_ten"],
    df["Tong_ket"],
    color="steelblue"
)

ax.set_title("ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN")
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)

ax.tick_params(axis="x", labelrotation=45)
ax.grid(axis="y", linestyle="--", alpha=0.4)

# Hien diem tren dau moi cot
ax.bar_label(bars, fmt="%.1f", padding=3)

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 5. Thong tin nguoi tao ung dung
st.divider()

st.markdown(
    """
    <div style="text-align:center; color:gray; font-size:12px;">
        Người tạo ứng dụng: DOAN MANH KHUONG<br>
        MSSV: 052208006111
    </div>
    """,
    unsafe_allow_html=True
)
