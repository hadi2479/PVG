import os

# 기본 폴더 이름
base_directory = "O:\\SOGPRO\\11.SMO1\\4.주간보고\\2024\\Wk"

# 10번 반복하면서 폴더 생성
for i in range(39, 53):
    directory = f"{base_directory}{i}"
    # print(base_directory)
    print(directory)

    # 폴더가 이미 존재하는지 확인하고, 존재하지 않으면 새로 만듦
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"{directory}가 성공적으로 생성되었습니다.")
    else:
        print(f"{directory}가 이미 존재합니다.")
