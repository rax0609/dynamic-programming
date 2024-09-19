# 5b1g0905 陳昱安
def calculate_bmi(weight, height_cm):
    """計算並返回BMI值"""
    height_m = height_cm / 100  # 將身高從公分轉換為公尺
    bmi = weight / (height_m ** 2)  # 計算BMI值
    return bmi  # 返回計算出的BMI值

def main():
    try:
        weight = float(input("請輸入您的體重(公斤): "))  # 提示使用者輸入體重，並將其轉換為浮點數
        height_cm = float(input("請輸入您的身高(公分): "))  # 提示使用者輸入身高，並將其轉換為浮點數
        bmi = calculate_bmi(weight, height_cm)  # 調用calculate_bmi函數計算BMI
        print(f"您的BMI是: {bmi:.2f}")  # 輸出計算出的BMI值，保留兩位小數
    except ValueError:
        print("請輸入有效的數字。")  # 如果輸入的不是有效的數字，則提示錯誤訊息

if __name__ == "__main__":
    main()  # 如果這個模組是主程式，則調用main函數