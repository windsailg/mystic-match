import json
import os

# 定義輸入 JSON 文件名稱
input_file = "./user_input.json"

# 假設 user_input.json 的內容如下：
# 根據服裝圖片標籤:
# {
#     "fit": 1,
#     "style": 1,
#     "type": 1,
#     "color": 3,
#     "height": 170,
#     "weight": 60
# }

# 檢查文件是否存在
if not os.path.exists(input_file):
    print(f"文件 {input_file} 不存在，請檢查路徑或創建文件！")
    # 選擇退出程式或創建默認文件
    exit()

# 讀取用戶輸入數據
with open(input_file, 'r', encoding='utf-8') as file:
    user_input = json.load(file)

# 計算用戶的 BMI
user_input["bmi"] = round(user_input["weight"] / ((user_input["height"] / 100) ** 2), 2)

# 打印用戶輸入
print("用戶輸入數據:", user_input)

# 模擬推薦算法的推薦結果
recommendations = [
    {"ID": 1, "similarity": 1.00},
    {"ID": 3, "similarity": 0.87},
    {"ID": 2, "similarity": 0.50},
]

# 打印推薦結果
print("推薦結果:")
for rec in recommendations:
    print(f"ID: {rec['ID']}, 相似度: {rec['similarity']:.2f}")

# 構建輸出結果
output_data = {
    "user_input": user_input,
    "recommendations": recommendations,
}

# 保存推薦結果到 JSON 文件
output_file = "./recommendations.json"
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(output_data, file, ensure_ascii=False, indent=4)

print(f"推薦結果已保存到 {output_file}！")
