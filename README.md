![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 
<<<<<<< HEAD

=======
>>>>>>> fe131e27499d2ff2e1400ed4d56dc0da03d83e69
# Proyecto de Cinemática Directa de Robots

## Introducción
Este proyecto tiene como objetivo implementar la cinemática directa simbólica de tres robots manipuladores utilizando Python.  
Los robots analizados son: un robot planar de dos grados de libertad (RR), un robot antropomórfico de tres grados de libertad (RRR) y un robot con configuración SCARA (RRP).  
La cinemática directa permite obtener la posición y orientación del efector final del robot en función de los ángulos de sus articulaciones.

## Metodología
Para el desarrollo del proyecto se siguieron los siguientes pasos:

1. **Repositorio base:**  
   Se clonó el repositorio [DH-Forward-Kinematics-Function](https://github.com/SolKacil/DH-Forward-Kinematics-Function---Python) que contiene funciones para calcular la cinemática directa de robots a partir de sus parámetros Denavit-Hartenberg (DH).

2. **Implementación en Python:**  
   - Se crearon archivos separados para cada robot: `RR.py`, `RRR.py` y `SCARA.py`.  
   - Cada archivo contiene los parámetros DH específicos del robot según las tablas del libro *Control de robots manipuladores* de Fernando Reyes Cortes (páginas 226-237).  
   - Se utilizó **SymPy** para manejar variables simbólicas y calcular las matrices de transformación homogénea.  
   - Se imprimieron en la terminal las matrices de transformación homogénea que representan la posición y orientación del efector final de cada robot.

3. **Documentación en el código:**  
   - Se añadieron comentarios en cada línea o bloque relevante del código para explicar su función.  
   - Se indicó claramente dónde se ingresan los parámetros DH, cómo se calculan las matrices y cómo se muestran los resultados.

4. **Verificación de resultados:**  
   - Se compararon los resultados obtenidos con los ejemplos y resultados del libro para asegurar que la implementación fuera correcta.  
   - Se verificó que las matrices fueran consistentes y reflejaran correctamente la cinemática de cada robot.

## Resultados
- Se logró implementar con éxito la cinemática directa simbólica de los tres robots.  
- Cada robot tiene un archivo Python independiente que permite calcular y visualizar la matriz de transformación homogénea de manera simbólica.  
- El código es modular, fácil de modificar y reutilizable para otros robots si se requieren cambios en los parámetros DH.

## Conclusión
El proyecto permitió comprender y aplicar los conceptos de cinemática directa de robots manipuladores, así como el uso de Python y SymPy para cálculos simbólicos.  
Se logró un entendimiento práctico de cómo los parámetros DH determinan la posición y orientación del efector final, y cómo validar resultados con la bibliografía.

## Referencias
- Fernando Reyes Cortes, *Control de robots manipuladores*.  
- Código base: [Repositorio DH-Forward-Kinematics](https://github.com/SolKacil/DH-Forward-Kinematics-Function---Python)


# DH Forward Kinematics Python

This project provides tools to compute the forward kinematics of serial robotic manipulators using Denavit-Hartenberg (DH) parameters. It supports both numerical and symbolic calculations, making it useful for both simulation and analytical studies.

## Features
- Compute forward kinematics numerically using NumPy
- Compute forward kinematics symbolically using SymPy
- Unified class interface for both calculation types
- Example scripts for quick testing

## File Structure
- `forward_kinematics_dh.py`: Numeric DH forward kinematics functions (NumPy)
- `forward_kinematics_dh_symbolic.py`: Symbolic DH forward kinematics functions (SymPy)
- `forward_kinematics_dh_class.py`: Unified class with both numeric and symbolic methods
- `example.py`: Example usage of numeric and symbolic functions (separate functions)
- `example2.py`: Example usage of the unified class for both numeric and symbolic calculations

## How to Use
1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd dh_forward_kinematics_python
   ```
2. **Install dependencies**
   This project requires `numpy` and `sympy`. Install them with:
   ```sh
   pip install numpy sympy
   ```
3. **Run examples**
   - For basic function usage:
     ```sh
     python example.py
     ```
   - For class-based usage:
     ```sh
     python example2.py
     ```

## How It Works
- **Numeric calculation:**
  - Provide a list of DH parameters (theta, d, a, alpha) for each joint as numbers.
  - The code computes the transformation matrix using NumPy.
- **Symbolic calculation:**
  - Provide DH parameters as SymPy symbols or expressions.
  - The code computes the transformation matrix symbolically, allowing for analytical manipulation.
- **Unified class:**
  - The `ForwardKinematicsDH` class provides both `numeric()` and `symbolic()` static methods for easy switching between calculation types.

## Example
```
from forward_kinematics_dh_class import ForwardKinematicsDH
import numpy as np
import sympy as sp

# Numeric
dh_params = [[np.pi/4, 0, 1, 0], [np.pi/4, 0, 1, 0]]
H = ForwardKinematicsDH.numeric(dh_params)
print(H)

# Symbolic
th1, th2 = sp.symbols('th1 th2')
a1, a2 = sp.symbols('a1 a2')
dh_params_sym = [[th1, 0, a1, 0], [th2, 0, a2, 0]]
H_sym = ForwardKinematicsDH.symbolic(dh_params_sym)
sp.pprint(H_sym)
```

## License
MIT
