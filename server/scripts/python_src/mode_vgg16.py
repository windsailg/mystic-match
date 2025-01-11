import numpy as np
import cv2
import json
import os
#from tensorflow.keras.models import load_model
#from tensorflow.keras.applications.vgg16 import preprocess_input
from clothes import clothes

# 加載模型
# model = load_model("./vgg16_feature_extractor.keras")

# 加載圖片特徵數據
# with open("./image_features.json", "r") as f:
#     image_features = json.load(f)

# 提取圖片特徵向量的函數
# def get_image_feature_vector(image_path):
#     image = cv2.imread(image_path)
#     image = cv2.resize(image, (224, 224))
#     image = preprocess_input(np.expand_dims(image, axis=0))
#     features = model.predict(image)
#     features = features.flatten()
#     return features

# 計算餘弦相似度的函數
def calculate_cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)

# 主程式
def main(user_input):
    required_fields = ["fit", "style", "type", "color"]
    if not all(field in user_input for field in required_fields):
        raise ValueError(f"輸入缺少必要字段: {required_fields}")

    # print("用戶輸入數據:", user_input)
    user_feature_vector = np.array([user_input["fit"], user_input["style"], user_input["type"], user_input["color"]])

    # 計算用戶輸入特徵與圖片標籤特徵的相似度
    label_similarities = []
    for item in clothes:
        label_similarity = calculate_cosine_similarity(user_feature_vector, np.array(item["vector"]))
        label_similarities.append({"ID": item["id"], "similarity": label_similarity})

    # 根據相似度進行排序
    recommendations = sorted(label_similarities, key=lambda x: x["similarity"], reverse=True)[:10]

    # 構建推薦詳細信息
    if recommendations:
        recommendation_details = {
            "comments": "這套穿搭展現了恬靜與自然的氛圍，整體色調柔和，給人一種輕鬆愜意的感覺。同時，配件的選擇也十分用心，為整體增添了一點亮點。這樣的風格不僅適合日常，也能讓人感覺到穿者的自信與從容。",
            "mainRecommand": f"public/images/clothes/{recommendations[0]['ID']}.jpg",
            "recommandList": [
                f"public/images/clothes/{rec['ID']}.jpg" for rec in recommendations[1:6]
            ]
        }
    else:
        recommendation_details = {
            "comments": "目前無法提供推薦，請檢查數據輸入或圖片特徵。",
            "mainRecommand": None,
            "recommandList": []
        }

    return recommendation_details

# 執行主程式
if __name__ == "__main__":
    import sys

    # 處理命令列輸入
    # print(sys.argv[1])
    input_raw = sys.argv[1]
    # .replace("'", '"')  # 將單引號替換為雙引號
    input_args = json.loads(input_raw)
    result = main(input_args)

    # 輸出結果
    print(json.dumps(result, ensure_ascii=False, indent=4))
