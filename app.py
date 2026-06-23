import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('learning_data.csv')
df.columns

X = df.drop(columns=['Target_Shape'])

y = df[['Target_Shape']]

en_y = pd.get_dummies(y)

assert X.isnull().sum().sum() == 0, "NULL"

X_train, X_test, y_train, y_test = train_test_split(X, en_y, test_size=0.1, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
print("SUKSES")

prediksi = model.predict(X_test)
akurasi = accuracy_score(y_test, prediksi)
print(f"Akurasi: {akurasi * 100:.2f}%")

print("Format: (Number of Sides, Total Angle, Equilateral, Curved Line, Perimeter, Area)")
try:
    number_of_sides = int(input("Number of Sides: "))
    total_angle = int(input("Total Angle: "))
    equilateral = int(input("Equilateral (Y/N): ").lower() == "y")
    curved_line = int(input("Curved Line (Y/N): ").lower() == "y")
    perimeter = float(input("Perimeter: "))
    area = float(input("Area: "))
except(ValueError, NameError, TypeError) as e:
    print(f"Invalid input. Error: {e}")

shapes = pd.DataFrame(
    [[number_of_sides, total_angle, equilateral, curved_line, perimeter, area]],
    columns=[
        "Number_of_Sides",
        "Total_Angle",
        "Equilateral",
        "Curved_Line",
        "Perimeter",
        "Area",
    ],
)

prediksi = model.predict(shapes)

undummy = pd.DataFrame(
    prediksi,
    columns=[
        "Circle",
        "Equilateral Triangle",
        "Oval",
        "Pentagon",
        "Rectangle",
        "Scalene Triangle",
        "Square",
    ],
)
df_predict = undummy.idxmax(axis=1)
print(f"The shape is: {df_predict.iloc[0]}")
