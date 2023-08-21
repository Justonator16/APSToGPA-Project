
# Video demo: <URL HERE>
# APSToGPA

### Description: APSToGPA is a user-friendly web application designed to help students and applicants in South Africa calculate their Admission Point Score (APS) and Grade Point Average (GPA). This tool assists users in determining their eligibility for university admissions and provides insights into their academic performance by converting grades into APS levels and letter grades.

## Table Of Contents
- [Introduction](#Introduction)
- [Features](#Features)
- [HTML files in Templates folder](#templates)
- [Static](#static)
- [Other files](#otherfiles)
- [Problems l encountered ](#solution)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction
Welcome to APStoGPA, South Africa's greatest tool for calculating and converting academic results! Whether you want to know your Admission Point Score (APS) or your Grade Point Average (GPA), our easy-to-use online app has you covered. To better comprehend your academic achievements and university eligibility, seamlessly move between APS levels, letter grades, and numerical scores.

## Features
Main features of APSToGPA include:
> [!MPORTANT]
> The application is exclusively utilized by high school students who are either applying to colleges or universities or simply interested in understanding their APS and GPA.
- **APS Score Calculation**: Easily calculate your Admission Point Score (APS) based on your final exam results.

- **GPA Conversion**: Convert your grades to GPA values on a 4.0 scale for a clearer understanding of your academic performance.

- **Letter Grade Conversion**: Instantly transform your numerical grades into letter grades (e.g., A, B, C+) for quick interpretation.

- **Custom Reports**: Create personalized reports with unique names to track and compare your academic progress over time.

- **Clear User Interface**: Intuitive design and easy navigation make it simple for users to input data and obtain results.

- **Subject Analysis**: View detailed summaries of subjects, including APS level, letter grade, and GPA weighting.

- **Error Handling**: Get informative messages for successful actions or potential issues, ensuring a smooth user experience.

- **Data Persistence**: Store and manage user records securely, allowing you to revisit and compare results at any time.

- **Quick Links**: Use interactive buttons to swiftly access specific sections of the app, enhancing user convenience.

- **User Authentication**: Securely register and log in with unique credentials to ensure data privacy and personalization.

## HTML files in Templates folder
The following is a list of all html files in my project and their purpose inorder from index page to report page:
- **index.html** - This website provides a brief introduction to my project while also providing a user-friendly experience.

- **form.html** - is the foundation template for the general layout of the <sup>signup.html</sup> and <sup>login.html</sup> pages. It contains the header as well as the navigation menu, maintaining uniformity across all pages. This is the basic layout, which extends to the pages signup.html and login.html with some flask code to display (flash) error warnings when the login username/password is wrong, the account already exists, and to prohibit two or more separate users from using the same username in their accounts. Overall, on the signup.html page, create an account to save reports and then compare them.

     - **signup.html** - is responsible for user registration. It provides a user-friendly interface for users to create new accounts.
     - **login.html** - handles user authentication, allowing users with existing accounts to log in.

- **layout.html** - From this point on, the page applies to all html pages. This shortens my code and allows me to concentrate on the purpose of the pages based on their titles, eliminating the need to copy and paste simple body tags.

- **home.html** - The main landing page of the web app serves as an introduction to the APStoGPA project, presenting its features and benefits to users. It also offers quick access to various sections of the app. Furthermore, it provides a basic explanation of APS and GPA, accompanied by links to YouTube videos that offer in-depth assistance to logged-in users seeking a comprehensive understanding of APS and GPA concepts.

- **aps.html** -
This HTML file offers a user-friendly interface for computing the APS score using entered subject grades. Users can input both their grades and subjects to receive their APS scores. Using JavaScript, I've integrated functions that, upon clicking specific buttons, promptly display results in a pop-up window for convenience. The page also features a button that seamlessly transforms numerical grades into corresponding letter grades (such as A, B, C+), facilitating a rapid and comprehensible assessment of the grades. In the "Calculate APS Score" button l included conditions that alert a user if they got a distinction ( grade 80 and above in south africa ) for a particular subject.

- **aps_score.html** - presents a user-friendly interface for computing the APS score and GPA on a 4.0 scale, using the entered subject grades. Users can input their grades for each subject and receive their corresponding APS score. Additionally, it enables users to save their reports with personalized names. To enhance user experience, I've incorporated code that detects and prevents the use of the same report name for different sets of results, effectively returning an error in such cases.

- **transcript-default** - This page features a simple dropdown menu for selecting a report name and a "View Report" button that leads users to the "transcript.html" page. To address a previous issue, I've introduced the "transcript_default.html" page. This page acts as an intermediary step when users click the "Transcript" button on the navigation bar. It redirects users to the "transcript.html" page without tables or information, serving as a placeholder before they input data. This enhancement prevents the appearance of empty tables with headings on the main transcript page.

- **transcript.html** - empowers users to track and analyze their academic journey using personalized reports. It offers an in-depth overview of subjects, showcasing APS levels, letter grades, and GPA weights. This insightful presentation allows users to assess their performance across different subjects.

## Static folder contents
- **styles.css** - It defines the visual design and arrangement of the web app's user interface through Cascading Style Sheets (CSS). Additionally, it includes various images that I incorporated as backgrounds, extending from the index.html page to the headings within other HTML files.

- **aps.js** - This JavaScript file contains the functions I used for most of the buttons in the project. For some functions like calculating APS score, GPA on a 4.0 scale, and converting grades to letter grades, I've included an alert method. This allows users to receive their results instantly upon clicking the button, without needing to wait for the page to reload.

### Other files in my project folder
- **app.py** - The majority of the file contains Python scripts that handle the backend logic of my web application.. It's the heart of my Flask-based web application, handling routing, user authentication, data processing, and rendering templates for the frontend. In essence, app.py defines the behavior of my web application when users interact with it through their web browsers.

- **aps_and_gpa_calculators.py** - The file encompasses functions I utilized to showcase APS levels corresponding to specific subject grades, calculate APS scores for groups of subjects' grades, determine letter grades for each subject's grade, compute grade points for individual subject grades, and establish GPA weighting for seven subjects.

- **apstogpa.db** - The database serves as a repository for all user information, encompassing usernames, passwords, and the subjects and grades they have saved under personalized names. This information is then utilized within the <sup>app.py</sup>> file to perform a range of functions, including verifying user logins by cross-referencing data in the users table, as well as retrieving subjects and grades that users have saved for display within the transcript section of the web application.

#### Problems l encountered in my project and how l fixed them
- From Flask sessions, I aimed to have the browser remember the currently logged-in user. I attempted to create a dictionary using a key-value pair, where the key was "user_id" and the value was the user ID from the database of users. However, the dictionary returned a "None" value for the value section. Despite my efforts to find a solution, I couldn't resolve this issue.

As an alternative, I devised an approach to store the logged-in user's information in the "current_user" table within my "apstogpa" database. Within this table, there is a column named "user_logged_in" that stores a text value. Each time a different user logs in, their username is updated in the "user_logged_in" column. This method replicates the functionality of Flask sessions by storing the username for later use in other functions and HTML files.

Now, I can easily refer to the username within the "current_user" table to determine which reports should be displayed based on the logged-in user. This solution addresses potential issues I might have encountered in my application, such as users accessing other users' reports without using their own accounts.

- To address the issue of buttons overlapping tables, headings, and paragraphs, I have included page breaks between the buttons and the tables, headings, or paragraphs. This ensures that the content is properly separated and displayed without overlapping.

- During the initial development of the project, my intention was to allow high school users to convert their APS scores to a GPA 4.0 scale and vice versa. However, I encountered an issue with this approach. APS calculations are constrained to a maximum of 7 subjects, while GPA calculations can involve more than 7 subjects. This meant that users who had studied more than 7 subjects in their report would need to select only 7 subjects for APS calculation.

Consequently, on the web page's APS AVERAGE section, I incorporated a provision for up to 14 inputs from the user, including both subjects and corresponding grades. This flexibility was introduced to accommodate situations where users might have more than 7 subjects to consider for GPA conversion, thus providing a more accurate representation of their academic performance.

## Installation
1. Requirements on how to install this application locally packages:
     - Flask modules
     - Cs50 module
     - Python
     - SQLIte
     - JavaScript
2. Clone the repository: `git clone https://github.com/Justonator16/APSToGPA.git`


## Usage
1. Run the web application: `flask run`
2. Open a web browser and go to `http://localhost:5000`
3. Sign up or log in to your account.
4. Use the various features to calculate APS levels, view reports, and more.

## License
MIT License

Copyright (c) 2023 Justonator16

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

