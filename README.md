# Graphic Content

## Code Institute Milestone Project 4
[View the Live Project Here](https://clacken-ms4.herokuapp.com/)

Add mockup image here

---

### Table of Contens

- ## Project
  - Website Description
  - Website Owner's Goals
- ## UX Design
  - User Stories
    - List of User Stories Here
    - Another User Story
    - Another User Story
  - Story Fulfillment
- ## Design
  - Colours
  - Wireframes
  - Responsiveness
  - Site Design
  - Database Schema
- ## Technologies Used
  - Languages
  - Database
  - Libraries
  - Tools
  - Programs
- ## Features
  - User Stories Implemented
  - CRUD Functionality
  - Messages
  - Additional Site Features
  - Future Feautures
- ## Testing (Link to Testing.md, view yoga app table of tests)
- ## Bugs
- ## Deployment
   - Cloning for Github
   - Deploying for Heroku
- ## Credits
  - Code
  - Images
  - Acknowledgements


# Project Goals
- The purpuse of this website is to attract individuals looking for graphic design services. They can view the available design options on the website, submit a request and then receive their artwork in their user profile when it's ready.

## Dev & Business Goals
- Graphic Content has the intention of selling graphics to users based on their selected purchase option
- User will submit a design request with a description, pay for the design, and view their submitted order in their profile
- Users can check back to their profile where their finished graphics will be displayed
- Admins are able to view and update orders, adding finished graphics to orders which are currently unfulfilled
- Admins can update and delete products, users, graphics, testimonials

# UX Design
## User Stories
- As a new user I want to understand the purpose of the site, navigate easily and select the suitable product I'm looking for
- As a user I want to select a product and view the price, as well as submit my design and checkout
- As a user I want to view my profile with orders attached
- As a user I want to view a selection of work by the company
- As a user I want to be able to sign up/login and logout

- As an admin I want to update products or orders
- As an admin I want to update users
- As an admin I want to fulfill the orders easily by uploading graphics

# Design

### Overall Design Idea
- Simple, minimalist design
- Clear to see what functions do and how to navigate
- A nice logo which gives the graphic design theme
- Simple colours, lots of use of white space
- Abstract or artistic images to give design impressions
- Straightforward checkout, one click pay

### DB Schemas
![Image of Schema](https://github.com/clacken-dev/ms4/blob/main/documentation/db_schema.png?raw=true)

## Architecture

### Main project Directory
- graphic_design
  - core templates and static folders are located here
### Apps
- home - this renders the home view and contains some graphics for around the site
- profiles - This saves users to a profile model and loads a profile page to view information and orders
- checkout - this handles orders and payments and redirects as necessary
- products - this contains the product models and pages for viewing, selecting and proceeding with an order
- orders - this is for the admin side of order editing and fulfilment
### Models
- UserProfile
  - username
  - password
  - email
- Product
  - service_type
  - description
  - price
- Order
  - user (ForeignKey)
  - service (ForeignKey)
  - total
  - description
  - date
  - order_number
  - image
- Image
  - image
  - image_url
- Testimony
  - user (ForeignKey)
  - testimony

## Wireframes 

# Technologies Used

## Languages Used
 - HTML5
 - CSS3
 - Javascript
 - Python

## Frameworks, Libraries and Programs
- Bootstrap
- Django
- Google Fonts
- Photoshop
- Balsamiq Wireframes
- Font Awesome
- JQuery
- Git
- GitHub
- AWS S3

# Features
 - The site features a responsive minimalist design with intuitive feedback
# Testing

## Validation
- Site was validated with W3C Markup Validator and with W3C CSS Validator to ensure site complied with best practice and layout of both languages
[Link to Markup Results]()
[Link to CSS Results]()
- Python Linter was used to identify and rectify pep8 compliance issues in environment wherever possible

## Testing User Stories
| Scenario  	| Expectation  	|  Results 	|
|---	|---	|---	|
|   Home Page links verification	| Check all links work, are clearly labelled and bring to correct page  	|   PASS	|
|   Logo	|  Logo is displayed everywhere clearly and works as Home nav 	|   PASS	|
|   Products	|   Clear to see what products are availble, easy to see what the options and prices are if following the details link. Get a good idea of the products offered and what they entail	|   PASS	|
|  Gallery 	|   Easy to view gallery and view previous work to get an idea of the work offered by this company.	|  PASS 	|
|  Account creation 	| Possible to create an account, login and logout work and new navbar items are displayed after user authenticated  	|   PASS	|
|   Create Order	|  Verify that filling in the details on the checkout page will take payment and give confirmation of an order being confirmed with order number generated. Confirmation success page loading and displaying all relevant info 	| PASS  	|
|  View Profile 	|   Verify that navigating to profile after creating an order displays that order in the page with all order information. Also lets me know that the order is unfulfilled as there is no graphic uploaded yet	|   PASS	|
|   View fulfilled order	|  Navigating to the profile page if an order is fulfilled displays the graphic in the order information and separates the fulfilled and unfulfilled orders if a customer has multiple orders 	|   PASS	|
|   Admin Orders	|   As the site admin I clearly get the Orders link on the navbar and can navigate to the page showing all orders submitted on the site. The option to update unfulfilled orders is there. 	|   PASS	|
|   Fulfill Order	|   As the admin I can click the update order button on an unfulfilled order and will be brought the the upload form where I can complete a user's order by adding the graphic they requested	|  PASS 	|
|   Admin Functions	|  Admin functions for products, users, testimonies and images are accessed through the admin page. Logging into the admin page I see that the necessary fields and models have all been registered and can be used as desired 	|   PASS	|
|   Logout	|   As a user wishing to logout I can easily logout using the account link on the navbar which will check to confirm first. I can then logout and am redirected as necessary	|  PASS 	|
|   Checkout - Ease of Use	|   The checkout is layed out clearly with fields for input marked. The price is displayed and the card information is clearly visible and provides feedback if there are errors in input. Clicking the submit lets the user know that the button is disabled and when payment complete the page refreshes.	|   PASS	|
|   Overall Experience	| The navigation experience is smooth overall. Pages are clearly laid out with lots of breathing space, sections are labelled and buttons and links all work. There is always the navbar to navigate back to a different location and pages are linked in an intuitive manner to aid site flow. The products view flows naturally into creating an order and paying. The order confirmation flows nicely to the profile page where users get accustomed to how the site flow will be on their next visit when checking for their finished image. Interaction is nice and responsive and site behaves as expected.  	|  PASS 	|

# Bugs
 - Some whitespace on mobile view of home page
 - Messages not displaying until navigating to admin panel
# Deployment
Repository set up

Ensure your requirements.txt is up to date.

pip3 freeze --local > requirements.txt - Ensure you have a Procfile in the repository.
web: gunicorn bookaband.wsgi:application
Create a new app on Heroku

Navigate to Heroku.
Once logged in/signed up for an account, select 'New' and 'Create New App'.
Create an app name and select a region.
Link up GitHub Repository

Select the 'Connect to GitHub' tab.
Type in repository name and select 'search'.
Once the repository is found, press 'connect'.
Heroku Set up

Navigate to the resources tab at the top of the page.
Search for 'Heroku Postgres' and select. Confirm which package you would like to use and 'submit order form'.
Environment Variables can be set in the app settings.
The following variables will need to be set:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
DATABASE_URL
EMAIL_HOST_PASS
EMAIL_HOST_USER
SECRET_KEY
USE_AWS
Under the 'Deploy' tab, enable automatic deploys.

Deploying locally
To run the project on your local IDE Download Repository

Download the repository and navigate to the 'code' dropdown.
Add the HTTPS url to your clipboard.
Open your environemt and use git clone followed by the repository url.
Install the requirements file with pip3 install -r requirements.txt
Set variables in an env file or in your environment variables settings.
Add 'developement' to the list of environement variables to ensure debug is set to True.
Ensure USE_AWS is set to False
EMAIL_* variables are not required as emails will be posted to the terminal while in development mode.


# Credits
### Code
- Site design is based off Code Institute's Boutique Ado and borrows features and functionality from it. Most elements are adapted as needed and all are attributed in the code. 

### Images
- Images used from Unsplash and Pexels

## Acknowledgments
- This project was inspired by Code Institute's Boutique Ado project.

 - Many thanks go to my mentor for his continued support throughout the project.

- Thanks  to the Code Institute tutor team for their guidance and help.