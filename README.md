# **Chromium Browser Automation - Python Script**

## **Description**
This Python script leverages the `DrissionPage` library to automate interactions with a Chromium-based browser. It demonstrates logging into a website, navigating through elements, and interacting with UI components such as checkboxes and buttons, making it ideal for browser automation tasks.

---

## **Key Features**
- **Chromium Browser Options Configuration:** Flexible setup for Chromium browser arguments.
- **Web Element Interaction:** Automates clicking and interacting with elements such as checkboxes, buttons, and navigation menus.
- **Customizable Automation:** Easily extendable for different websites and automation workflows.

---

## **System Requirements**
Ensure the following prerequisites are met:
1. **Python 3.x:** Installed on your system.
2. **DrissionPage Library:** Installable via pip (`pip install DrissionPage`).
3. **Chromium Browser:** Installed on your machine (e.g., Google Chrome).
4. **Environment Variable:** Set `CHROME_PATH` to the path of your Chromium executable.

---

## **Installation & Usage**

### **Installation:**
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-repository/chromium-automation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd chromium-automation
   ```
3. Install required dependencies:
   ```bash
   pip install DrissionPage
   ```

### **Usage:**
1. Update the `CHROME_PATH` environment variable to the path of your Chromium browser executable.
   - Example for Linux:
     ```bash
     export CHROME_PATH=/usr/bin/google-chrome
     ```
   - Example for Windows:
     ```bash
     set CHROME_PATH=C:\Program Files\Google\Chrome\Application\chrome.exe
     ```
2. Run the script:
   ```bash
   python automation_script.py
   ```
3. The script will:
   - Launch the Chromium browser with specified options.
   - Open the target website (`https://app.apollo.io/#/login`).
   - Perform automated interactions (e.g., clicking, navigation).

---

## **Script Overview**

### **Key Functions:**
1. **`get_chromium_options(browser_path: str, arguments: list) -> ChromiumOptions`:**
   - Configures Chromium browser options based on provided arguments.
   - Example arguments include:
     - `-disable-gpu`
     - `-accept-lang=en-US`

2. **Automation Steps:**
   - **Navigation:** Opens the target website.
   - **Element Interaction:**
     - Clicks navigation links, buttons, and checkboxes.
     - Performs conditional actions based on element availability.


## **Customizing the Script**
1. **Target Website:**
   - Update `driver.get('<URL>')` with your desired URL.
2. **Element Selectors:**
   - Modify CSS selectors (e.g., `#side-nav`) to match your target website's structure.
3. **Additional Features:**
   - Add new automation steps for tasks like form filling, file uploads, etc.

---

## **Technologies Used**
- **Python:** Core programming language for scripting.
- **DrissionPage:** Simplifies browser automation tasks.
- **Chromium Browser:** Ensures compatibility and high performance for web automation.

---

## **Author**
[M Ismail Daniyal](https://github.com/ismaildaniyal)

Feel free to reach out for any queries or suggestions at [ismailsarfraz9345@gmail.com]!
