import pandas as pd
import random
df_true_semantic = pd.read_csv("true_positive_java.csv", index_col=None)
df_false_semantic = pd.read_csv("false_positive_java.csv", index_col=None)
non_clone_functions = []

non_clone_functions.extend(df_false_semantic['function 1'].tolist())
non_clone_functions.extend(df_false_semantic['function 2'].tolist())

df_cs_contrastive = pd.DataFrame(columns=["function 1", "function 2", "clone"])


for i in range(len(df_true_semantic)):
    _,clone1_function, clone2_function = df_true_semantic.iloc[i]

    print()
    df_cs_contrastive.loc[len(df_cs_contrastive.index)] = [clone1_function, clone2_function, 1]
    df_cs_contrastive.loc[len(df_cs_contrastive.index)] = [random.choice([clone1_function,clone2_function]), random.choice(non_clone_functions), 0]


df_cs_contrastive
df_cs_contrastive.to_csv("df_java_contrastive.csv", index=None)