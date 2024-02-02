# Overview

This Python application provides a user-friendly graphical interface for calculating wages based on hours worked, hourly rates, and other parameters.

## Features

* <b>Wage Calculation</b>:
Input hours worked, hourly rate, week number, start date, end date, and invoice number.
Calculates wages based on provided inputs.

* <b>Breakdown of wage into expenditure, savings, investment, and tax.</b>

* <b>Data Storage</b>:
Store calculated wages in a CSV file for future reference.
Read existing wage data from the file upon program startup.

## Dependencies

* tkinter
* pandas
* tkcalendar

## Usage

Enter relevant details in the provided fields.
Click the "Calculate Wage" button to calculate wages and store the data.

## Getting Started

* Clone the repository:<br>
` git clone https://github.com/your-username/wage-calculator.git`
* Navigate to the project directory:<br>
` cd WageCal`
* Install dependencies:<br>
` pip install -r requirements.txt`
* Run the application:<br>
`python main.py`

## License

This project is licensed under the MIT License.

## Acknowledgments

Thanks to tkinter for the GUI components.
pandas for data manipulation.
tkcalendar for the date entry widget.
