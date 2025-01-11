import json
from transformers import pipeline

# 初始化 Hugging Face 的文本生成管道
generator = pipeline("text-generation", model="gpt2")  # 使用合適的模型

# 選擇的衣服資訊
selected_clothing = {
    "ID": 1,
    "fit": "合身",
    "style": "日系",
    "type": "休閒",
    "color": "紅",
}

# 評語生成的提示語（Prompt）
prompt = (
    f"這套穿搭由以下特徵組成："
    f"合身的剪裁、日系風格、休閒類型，並採用紅色作為主色調。"
    f"請生成一段評語，描述其特點和適用場合："
)

# 生成評語
response = generator(prompt, max_new_tokens=100, num_return_sequences=1)  # 使用 max_new_tokens 控制生成長度
generated_comment = response[0]["generated_text"]

# 處理生成的文本
generated_comment = generated_comment.replace(prompt, "").strip()  # 去除提示語部分

# 打印結果
print("生成的評語:")
print(generated_comment)

# 保存到 JSON 文件（可選）
output_file = "clothing_comment.json"
output_data = {
    "selected_clothing": selected_clothing,
    "comments": generated_comment,
}

with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(output_data, file, ensure_ascii=False, indent=4)

print(f"評語已保存到 {output_file}！")
