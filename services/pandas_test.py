import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Miesiąc":["Styczeń","Luty","Marzec","Kwiecien"],
    "Sprzedaż":[120,400,200,900]
}

dataframe = pd.DataFrame(data)
#dataframe.to_excel("testowy1.xlsx", index=True, index_label="Indeks")
dataframe.to_json("test.json",force_ascii=False)
dataframe.to_html("test.html")


# print(dataframe.values)
# print(dataframe.head(1))
#
# dataframe.plot(
#     x="Miesiąc",
#     y="Sprzedaż",
#     kind="line",
#     color="red",
#     marker="s"
# )
#
# plt.ylim(0, max(data["Sprzedaż"]) + 100)
#
# plt.title("Sprzedaż w mojej firmie")
# plt.xlabel("Miesiące")
# plt.ylabel("Ilość")
# plt.show()
#
#
# data2 = {
#     "x":[6,4,8,2,3,1],
#     "y":[20,30,15,70,12,18]
# }
#
# df2 = pd.DataFrame(data2)
# df2.plot(
#     x="x",
#     y="y",
#     kind="scatter",
#     color="green"
# )
# plt.title("Zależność między X a Y")
# plt.xlabel("Wartości X")
# plt.ylabel("Wartości Y")
# plt.show()
