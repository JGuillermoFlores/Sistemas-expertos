# Importar las librerías necesarias
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generar datos de ejemplo
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=123)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=123)

# Definir el modelo de bosques aleatorios
modelo = RandomForestClassifier(n_estimators=100, random_state=123)

# Entrenar el modelo con los datos de entrenamiento
modelo.fit(X_entrenamiento, y_entrenamiento)

# Predecir las etiquetas de los datos de prueba
y_pred = modelo.predict(X_prueba)

# Evaluar el rendimiento del modelo
precision = modelo.score(X_prueba, y_prueba)
print("La precisión del modelo es: {:.2f}%".format(precision*100))