import pandas as pd
import matplotlib.pyplot as plt

# 1. Tao DataFrame gom 10 sinh vien
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

df = pd.DataFrame(data)

# 2. Tinh diem tong ket
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
)

# 3. Xep loai sinh vien
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7.0:
        return "Kha"
    elif diem >= 5.0:
        return "Trung binh"
    else:
        return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# Hien thi bang du lieu
print("=== BANG DIEM SINH VIEN ===")
print(df.round({"Tong_ket": 2}).to_string(index=False))

# 4. Thong ke
diem_tb = df["Tong_ket"].mean()
sv_cao_nhat = df.loc[df["Tong_ket"].idxmax()]
sv_thap_nhat = df.loc[df["Tong_ket"].idxmin()]
so_sv_dat = (df["Tong_ket"] >= 5).sum()

print("\n=== THONG KE ===")
print(f"Diem trung binh lop: {diem_tb:.2f}")
print(
    f"Sinh vien cao nhat: {sv_cao_nhat['Ho_ten']} "
    f"- {sv_cao_nhat['Tong_ket']:.2f}"
)
print(
    f"Sinh vien thap nhat: {sv_thap_nhat['Ho_ten']} "
    f"- {sv_thap_nhat['Tong_ket']:.2f}"
)
print(f"So sinh vien dat: {so_sv_dat}/10")

# 5. Ve bieu do cot
plt.figure(figsize=(12, 6))
plt.bar(df["Ho_ten"], df["Tong_ket"])
plt.title("DIEM TONG KET CUA 10 SINH VIEN")
plt.xlabel("Ho va ten sinh vien")
plt.ylabel("Diem tong ket")
plt.ylim(0, 10)
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()
