# Geometry Shape Classifier using Machine Learning

A simple yet interactive Machine Learning project that predicts geometric shapes based on their physical characteristics (such as sides, angles, loops, perimeter, and area). This project demonstrates data preprocessing, handling categorical targets via One-Hot Encoding, reversing dummy variables using Pandas, and building an interactive CLI-based prediction tool.

## 🚀 Features
* **Custom Synthetic Dataset**: Built with geometric rules to avoid underfitting.
* **Decision Tree Classifier**: Utilizing Scikit-Learn for accurate shape classification.
* **Robust Preprocessing**: Properly handles DataFrame feature names during inference to prevent Scikit-Learn UserWarnings.
* **Interactive CLI**: Allows users to input properties manually and get instant geometric shape predictions.

---

## 📊 Dataset Features

The model learns from the following input features (case-sensitive):

* `Number_of_Sides` *(Integer)*: The total number of sides/edges of the geometric shape (e.g., `4` for a Square, `0` for a Circle).
* `Total_Angle` *(Integer)*: The sum of all internal angles in degrees (e.g., `180` for triangles, `360` for quadrilaterals).
* `Equilateral` *(Binary: 1 or 0)*: Indicates whether all sides of the shape are equal in length (`1` for Yes, `0` for No).
* `Curved_Line` *(Binary: 1 or 0)*: Indicates whether the shape consists of curved paths (`1` for Yes, `0` for No).
* `Perimeter` *(Float)*: The total distance around the outside of the shape.
* `Area` *(Float)*: The total space enclosed inside the boundary of the shape.

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
```bash
   git clone [https://github.com/RaffaSatya/geo-shape-classifier.git](https://github.com/RaffaSatya/geo-shape-classifier.git)

   cd geo-shape-classifier
```
2. **Create and active Virtual Environment:**
- **Windows**
```bash
   python -m venv .venv
   .venv\Scripts\activate
```
- **macOs/Linux**
```bash
   python3 -m venv .venv
   source .venv/bin/activate
```
2. **Install required library:**
```bash
    pip install pandas scikit-learn
```
3. **Run the script:**
```bash
   python app.py
```