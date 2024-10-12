import tkinter as tk

# 버튼 클릭 시 발생하는 함수
def on_button_click(value):
    current = entry.get()  # 현재 입력 필드의 값 가져오기
    entry.delete(0, tk.END)  # 입력 필드 비우기
    entry.insert(tk.END, current + str(value))  # 클릭한 버튼의 값을 입력 필드에 추가

# '=' 버튼 클릭 시 결과 계산
def calculate():
    try:
        result = eval(entry.get())  # 입력 필드의 수식을 계산
        entry.delete(0, tk.END)  # 입력 필드 비우기
        entry.insert(tk.END, str(result))  # 결과를 입력 필드에 표시
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")  # 잘못된 수식일 경우 에러 표시

# 'C' 버튼 클릭 시 입력 필드 비우기
def clear():
    entry.delete(0, tk.END)

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("GUI 계산기")

# 입력 필드 생성
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# 버튼 텍스트
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# 버튼 생성 및 배치
row_value = 1
col_value = 0
for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, width=5, height=2, font=('Arial', 18),
                        command=calculate)
    elif button == "C":
        btn = tk.Button(root, text=button, width=5, height=2, font=('Arial', 18),
                        command=clear)
    else:
        btn = tk.Button(root, text=button, width=5, height=2, font=('Arial', 18),
                        command=lambda b=button: on_button_click(b))
    
    btn.grid(row=row_value, column=col_value)
    
    col_value += 1
    
    
    if col_value > 3:
        col_value = 0
        row_value += 1
    
# 메인 루프 실행
root.mainloop()
