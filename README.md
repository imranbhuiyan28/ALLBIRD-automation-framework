# ALLBIRD Website Test Automation Framework

## Project Overview

This project is a **UI Test Automation Framework** developed using **Python**, **Selenium WebDriver**, and **Behave (BDD)**.

The framework automates real user workflows for the Allbirds e-commerce website and demonstrates automation practices commonly used in modern QA engineering teams.

The framework is built using the **Page Object Model (POM)** design pattern to improve maintainability, scalability, and test readability.

It includes structured logging, reusable page objects, organized feature files, and modular step definitions.

This repository serves as part of my **QA Automation Engineering portfolio** and demonstrates real-world automation framework design.

---

## Technologies Used

* Python
* Selenium WebDriver
* Behave (BDD)
* Page Object Model (POM)
* Custom Logging
* Git Version Control

---

## Framework Architecture

The project follows a layered automation architecture:

```
Feature Files (BDD Scenarios)
        ↓
Step Definitions
        ↓
Page Object Classes
        ↓
Base Page Utilities
        ↓
Selenium WebDriver
```

This structure ensures clear separation between **test logic**, **UI interactions**, and **framework utilities**.

---

## Test Coverage

### Homepage Testing

* Verify homepage loads successfully
* Validate page title
* Verify navigation functionality
* Validate footer links
* Validate social media links

### Product Page Testing

* Verify product images load correctly
* Select product options such as size
* Add product to cart

### Shopping Cart Testing

* Add product to cart
* Update product quantity
* Remove product from cart
* Verify cart updates correctly

### Responsive Design Testing

Layout validation across:

* Desktop
* Tablet
* Mobile

### Performance Validation

* Measure homepage load time
* Validate acceptable page load performance

---

## Project Structure

```
selenium-behave-test-automation
│
├── features
│   ├── cart.feature
│   ├── homepage.feature
│   ├── product.feature
│   └── responsive.feature
│
├── steps
│   ├── cart_steps.py
│   ├── homepage_steps.py
│   ├── product_steps.py
│   └── responsive_steps.py
│
├── pages
│   ├── base_page.py
│   ├── main_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── footer_page.py
│
├── support
│   └── logger.py
│
├── environment.py
├── requirements.txt
└── README.md
```

---

## Key Framework Components

### Feature Files

Feature files contain user-focused scenarios written in **Gherkin syntax** to describe application behavior.

### Step Definitions

Step definition files connect Gherkin steps to Python automation logic.

### Page Objects

Page classes store UI locators and reusable actions that represent the behavior of each page.

### Base Page

The `base_page.py` file provides shared Selenium utilities used by all page classes.

### Logging

Centralized logging captures scenario execution details and improves debugging and traceability.

---

## Getting Started

### 1. Clone the repository

```
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the automation suite

```
behave
```

---

## Author

**Imran Bhuiyan**
QA / Test Automation Engineer

Skills demonstrated in this project:

* Selenium Web Automation
* Python Test Framework Development
* Behavior Driven Development (BDD)
* Page Object Model Architecture
* Automation Framework Design
* Test Automation Best Practices
