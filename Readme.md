# Calorie Counter

A simple Django web application that helps users track their daily calorie intake by logging the foods they eat. The app automatically calculates the total calories consumed and provides an easy way to manage daily food entries.



##  Overview

The Calorie Counter is designed to make calorie tracking simple and efficient. Users can add food items along with their calorie values, view all logged foods, monitor their total calorie intake, and reset the list whenever they want to start a new day.

This project was built to practice Django fundamentals, including models, views, templates, forms, and static files.


## Features

-  Add food items with their calorie values
-  Display all logged food items
- Automatically calculate the total calories consumed
-  Reset all logged food items
- Clean and responsive user interface using CSS


##  Tech Stack

- Python 3
- Django
- HTML5
- CSS3
- SQLite3
- Git & GitHub



## Project Structure

```
CALORIE_COUNTER/
│
├── calorieApp/
│   ├── migrations/
│   ├── static/
│   │   └── calorieApp/
│   │       └── styles.css
│   ├── templates/
│   │   └── index.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── calorieProject/
│
├── db.sqlite3
├── manage.py
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/tugiii45/calorie_counter_django.git
```

### 2. Navigate into the project

```bash
cd calorie-counter
```

### 3. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```



## 💻 Usage

1. Enter the name of a food item.
2. Enter its calorie value.
3. Click **Add Item**.
4. View all logged foods and the total calories consumed.
5. Click **Reset All** to clear the list.



## Future Improvements

- User authentication
- Food categories
- Daily calorie goals
- Nutritional breakdown (Protein, Carbs, Fat)
- Search functionality
- Food editing and deletion
- Charts and analytics
- Mobile-friendly responsive design


## Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.



##  Author

**Conrad Karanja**


## License

This project is licensed under the MIT License.
