# NEIGHBOURHOOD WATCH

Welcome to the **Neighbourhood Watch** Python web application.

<hr>

## About the Project

Below is a screenshot of the project's landing page.
![ScreenShot](static\images\screenshot.jpg)

**Neighbourhood Watch** project is a web application that is created using a Python backend and its purpose is to keep a user on the know regarding with activities going on in their neighbourhood. This project is created to demonstrate the proficiency in Python Language and Django Framework.

<hr>

## User Stories

The following are the user stories in this project:

- A user can register before being able to use the application.
- A user can be able to set up their profile to their liking, with fields such as profile picture, their bio and contact details.
- A user can be able to create a neighbourhood which they are in or also join an already existing neighbourhood
- A user can be able to move out of their current neighbourhood and into another neighbourhood
- A user can be able to view, search and also create businesses within a specific neighbourhood
- A user can be able to not only view posts within a neighbourhood but also create posts for others to see

<hr>

## BEHAVIOUR DRIVEN DEVELOPMENT

|Behaviour|Input|Output|
|:--------|:-----|:----|
|Signing up for the application|Choosing between signing up for new users or login for usual users|Depending on the choice, respective pages will be displayed for the authentication process
|Join a neighbourhood|A button within the landing page, marked 'Join Neighbourhood'|Redirected to the specific neighbourhood page with specific details regarding the neighbourhood
|Create a neighbourhood|A button within the landing page, marked 'Create Neighbourhood'|Redirected to a page with a create neighbourhood form where details regarding the neighbourhood to be created should be input
|Move neighbourhoods|A button within the current neighbourhood card, marked 'Move Neighbourhood'|A user and their respective details gets moved from that particluar neighbourhood, a user is then able to create a neighbourhood or join another neighbourhood|
|Creating a neighbourhood post|Click on the 'Create Post' button within the specific neighbourhood page|The user is redirected to a page with a form where they can create their posts|
|Creating a neighbourhood business|Click on the 'Create Business' button within the specific neighbourhood page|The user is redirected to a page with a form where they can create their own business|
|Search for a business within a neighbourhood|Input the details within the search bar found in the specific neighbourhood page|Results for the desired output are displayed in a dedicated results page|

## Setup Instructions

**Neighbourhood Watch** is a web application which can be accessed by a device of choice with internet capabilities. No setup is required since it is in the form of a website. The application is built to be responsive across all devices with different media queries such as desktops, tablets and mobile phones.

To add Police Authority and Health Services information, log in to the admin dashboard using 'chacha' as the username and '6775' as the password.

<hr>

## Author

The sole author of the project is Jonathan Mwita Chacha.

<hr>

## Dependencies and Technologies Used

This project is built using:

- [Python](https://www.python.org)
- [Django Framework](https://www.djangoproject.com/)
- HTML
- CSS
- [Bootstrap](https://getbootstrap.com/)
- [Visual Studio Code Editor](https://code.visualstudio.com/)
- [Postgres Database](https://www.postgresql.org/)

This project is also dependant on various Django extensions that make up the functionality of the application.

<hr>

## Acknowledgements

The following parties greatly contributed to the development of **Instagram Clone** project:

- Moringa School LMS
- [Google Fonts](https://fonts.google.com/specimen/Ephesis#pairings)
- [ColorHunt](https://colorhunt.co/)
- [StackOverflow](https://stackoverflow.com/)
- [Font Awesome](tawesome.com/?utm_source=font_awesome_homepage&utm_medium=display&utm_campaign=fa5_released&utm_content=download_modal)
- [MIT License](https://opensource.org/licenses/MIT)

<hr>

## Contact Information

For any suggestions, reporting of bugs or improvements, reach me through my email address - jonahhchacha@gmail.com

## Copyright and License Information

Copyright (c) 2021 Jonathan Mwita Chacha

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
