# import pandas as pd
#
# # 读取 train.csv 文件
# df_train = pd.read_csv('./MSciNLI/train.csv')
#
# # 重命名列
# df_train.rename(columns={'sentence1': 'premise', 'sentence2': 'hypothesis'}, inplace=True)
#
# # 合并 premise 和 hypothesis 列并新建一个列 sentence1
# df_train['sentence1'] = df_train.apply(lambda row: f"PREMISE: {row['premise']} HYPOTHESIS: {row['hypothesis']}", axis=1)
# df_train = df_train.drop(columns=['Unnamed: 0'])
# # 映射字典，将原始标签映射到对应的数字
# # label_mapping = {
# #     'entailment': 0,
# #     'neutral': 1,
# #     'contrasting': 2,
# #     'reasoning': 3
# # }
# #
# # # 使用map方法进行替换
# # df_train['label'] = df_train['label'].map(label_mapping)
# #
# # # 删除包含NaN（无效标签）的行
# df_train = df_train.dropna(subset=['label'])
#
# # 保存修改后的 DataFrame 到新的 CSV 文件
# df_train.to_csv('./MSciNLI/train_modified.csv', index=False)
#
# print("文件已成功处理并保存为 train_modified.csv")
#
# df_train_null = df_train.copy()
# df_train_null['sentence1'] = ""
# df_train_null.to_csv('./MSciNLI/train_modified_null.csv', index=False)
#
# # # 读取 test.csv 文件
# # df_test = pd.read_csv('./MSciNLI/test.csv')
# #
# # # 重命名列
# # df_test.rename(columns={'sentence1': 'premise', 'sentence2': 'hypothesis'}, inplace=True)
# #
# # # 合并 premise 和 hypothesis 列并新建一个列 sentence1
# # df_test['sentence1'] = df_test.apply(lambda row: f"PREMISE: {row['premise']} HYPOTHESIS: {row['hypothesis']}", axis=1)
# # df_test = df_test.drop(columns=['Unnamed: 0'])
# # # 使用map方法进行替换
# # # df_test['label'] = df_test['label'].map(label_mapping)
# # #
# # # # 删除包含NaN（无效标签）的行
# # df_test = df_test.dropna(subset=['label'])
# # # 保存修改后的 DataFrame 到新的 CSV 文件
# # df_test.to_csv('./MSciNLI/test_modified.csv', index=False)
# #
# # print("文件已成功处理并保存为 test_modified.csv")
# #
# # # 读取 dev.csv 文件
# # df_dev = pd.read_csv('./MSciNLI/dev.csv')
# #
# # # 重命名列
# # df_dev.rename(columns={'sentence1': 'premise', 'sentence2': 'hypothesis'}, inplace=True)
# #
# # # 合并 premise 和 hypothesis 列并新建一个列 sentence1
# # df_dev['sentence1'] = df_dev.apply(lambda row: f"PREMISE: {row['premise']} HYPOTHESIS: {row['hypothesis']}", axis=1)
# # # # df_dev = df_dev.drop(columns=['Unnamed: 0'])
# # # # 使用map方法进行替换
# # # df_dev['label'] = df_dev['label'].map(label_mapping)
# #
# # # 删除包含NaN（无效标签）的行
# # df_dev = df_dev.dropna(subset=['label'])
# # # 保存修改后的 DataFrame 到新的 CSV 文件
# # df_dev.to_csv('./MSciNLI/dev_modified.csv', index=False)
# #
# # print("文件已成功处理并保存为 dev_modified.csv")


import pandas as pd

# 定义文件处理函数
# def process_csv(file_path, output_path):
#     # 读取CSV文件
#     df = pd.read_csv(file_path)
#     print(df.columns)
#
#     # 检查是否已经有 'Unnamed: 0' 列，若无则添加
#     if "Unnamed: 0" not in df.columns:
#         df.insert(0, "Unnamed: 0", range(len(df)))
#
#     # 重命名列
#     df = df.rename(columns={"sentence1": "premise", "sentence2": "hypothesis"})
#
#     # 创建新的 sentence1 列
#     df["sentence1"] = df.apply(lambda row: f"PREMISE: {row['premise']} HYPOTHESIS: {row['hypothesis']}", axis=1)
#
#     # 替换 label 列中的值
#     # 替换 label 列的内容
#     label_map = {
#         "entailment": 0,
#         "neutral": 1,
#         "contrasting": 2,
#         "reasoning": 3
#     }
#
#     # 检查未匹配的标签所在行
#     unmatched_rows = df[~df["label"].isin(label_map.keys())]
#     if not unmatched_rows.empty:
#         print(f"Unmatched labels in {file_path}:")
#         print(unmatched_rows)
#
#     # 删除未匹配的行
#     df = df[df["label"].isin(label_map.keys())]
#
#     # 进行 label 转换
#     df["label"] = df["label"].map(label_map)
#
#     # 保留指定的列
#
#     # 保留指定的列
#     df = df[["Unnamed: 0", "premise", "hypothesis", "label", "sentence1"]]
#
#     # 保存处理后的文件
#     df.to_csv(output_path, index=False)
#
# # def process_csv_null(file_path, output_path):
# #     # 读取CSV文件
# #     df = pd.read_csv(file_path)
# #     print(df.columns)
# #
# #     # 检查是否已经有 'Unnamed: 0' 列，若无则添加
# #     if "Unnamed: 0" not in df.columns:
# #         df.insert(0, "Unnamed: 0", range(len(df)))
# #
# #     # 重命名列
# #     df = df.rename(columns={"sentence1": "premise", "sentence2": "hypothesis"})
# #
# #     # 创建新的 sentence1 列
# #     df["sentence1"] = df.apply(lambda row: f"PREMISE: {row['premise']} HYPOTHESIS: {row['hypothesis']}", axis=1)
# #
# #     # 替换 label 列中的值
# #     label_mapping = {"entailment": 0, "neutral": 1, "contrasting": 2, "reasoning": 3}
# #     df["label"] = df["label"].map(label_mapping)
# #
# #     df['sentence1'] = ""
# #
# #     # 保留指定的列
# #     df = df[["Unnamed: 0", "premise", "hypothesis", "label", "sentence1"]]
# #
# #     # 保存处理后的文件
# #     df.to_csv(output_path, index=False)
# # 处理 train.csv、test.csv 和 dev.csv 文件
# process_csv("./MSciNLI/train.csv", "./MSciNLI/train_modified.csv")
# # process_csv_null("./MSciNLI/train.csv", "./MSciNLI/train_modified_null.csv")
# process_csv("./MSciNLI/test.csv", "./MSciNLI/test_modified.csv")
# process_csv("./MSciNLI/dev.csv", "./MSciNLI/dev_modified.csv")
#
# print("文件处理完成！")
#
# df = pd.read_csv('./MSciNLI/train_modified.csv')
# df_null = df.copy()
# df_null['sentence1'] = " "
# df_null.to_csv('./MSciNLI/train_modified_null.csv', index=False)


df = pd.read_csv('./MSciNLI/test_modified.csv')
df_null = df.copy()
df_null['sentence1'] = " "
df_null.to_csv('./MSciNLI/test_modified_null.csv', index=False)