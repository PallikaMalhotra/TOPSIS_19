
# **Title: TOPSIS Decision Support Web Application**

---

## **1. Methodology**

The project implements the **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** method, a widely used **Multi-Criteria Decision Making (MCDM)** technique.

The workflow includes:

* Data normalization
* Weight application
* Identification of ideal best and ideal worst solutions
* Distance calculation from ideal points
* TOPSIS score computation
* Ranking of alternatives based on scores

This method helps in selecting the best alternative when multiple conflicting criteria are involved.

---

## **2. Description**

This web-based TOPSIS application allows users to:

* Upload a CSV file containing alternatives and criteria
* Provide weights and impacts for each criterion
* Execute TOPSIS analysis through a backend algorithm
* Automatically generate a ranked result file

The system is built using:

* **Flask (Python)** for backend logic
* **HTML & CSS** for frontend interface
* **Pandas & NumPy** for data processing

The application ensures input validation and produces accurate ranking results based on user-defined preferences.

---

## **3. Input / Output**

### **Input**

* CSV file with:

  * First column as alternatives
  * Remaining columns as numerical criteria
* Weights (comma-separated, numeric)
* Impacts (comma-separated, `+` or `-`)
* Valid email ID (for future extension)

### **Output**

* A CSV file containing:

  * TOPSIS Score
  * Rank of each alternative
* Result file generated and stored on the server

---

## **4. Live Link**

🔗 **Live Application:**
https://topsis-19.onrender.com/

---

## **5. Technologies Used**

* Python
* Flask
* Pandas
* NumPy
* HTML
* CSS
* Render (Deployment)

---

## **6. Author**

**Developed by:**
**Pallika Malhotra**
TOPSIS Decision Support System

---

## **7. Notes**

* Email functionality can be extended using SMTP services.
* The application can be scaled for large datasets.
* Suitable for academic, research, and decision-support use cases.

---

### ✅ How to use

```bash
1. Upload CSV file
2. Enter weights and impacts
3. Submit the form
4. Download the result CSV
```

---
