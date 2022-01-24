# Graphic Content

## Code Institute Milestone Project 4
[View the Live Project Here](https://clacken-ms4.herokuapp.com/)

![Graphic Content Site](https://github.com/clacken-dev/ms4/blob/main/documentation/site-mockup.jpg?raw=true)

---

### Table of Contents

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
- Admins can update and delete products, users, graphics, reviews

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

### Examples of Design Implementation
### Products
- The products page has a clean design, easily understood product information and clear buttons for deciding to read further
  - Edit and Delete buttons are only shown to a Site Admin
![Products Page](https://github.com/clacken-dev/ms4/blob/main/documentation/v2-product.png?raw=true)
### Profile Page
- The profile page displays the username of the profile as well as the orders which are fulfilled or unfulfilled. Fulfilled orders will display the finished graphic
![Profile Page](https://github.com/clacken-dev/ms4/blob/main/documentation/v2-profile.png?raw=true)
### Gallery Page
- The gallery page has a clean design and shows work completed by the company as an advertising medium
![Gallery Page](https://github.com/clacken-dev/ms4/blob/main/documentation/v2-gallery.png?raw=true)
### Orders Page
- The orders page is only available to an Admin and shows the orders which are fulfilled or unfulfilled. All new orders will be unfulfilled until an image is uploaded to the order. They can view the full details of a fulfilled order and update the details of an unfulfilled order.
![Orders Page](https://github.com/clacken-dev/ms4/blob/main/documentation/v2-orders.png?raw=true)
### Product Detail Page
- The product detail page gives a longer description of each product as well as the option to continue with the site flow and enter the purchasing options for that product. Review for each product are displayed under the product if they exist. 
![Product Details Page](https://github.com/clacken-dev/ms4/blob/main/documentation/v2-product-details.png?raw=true)
### Review Section on Product Detail Page
- On each product page the users can view reviews which have been left for that specific product and also have the option to a contribute to the site by adding their own review for that product also.
![Review Section](https://github.com/clacken-dev/ms4/blob/main/documentation/v2-reviews.png?raw=true)

### DB Schemas
- The database is a relational model which features several Foreign Keys between tables. These allow for Products to be attached to Orders, Users to be the owners of Orders, Users to write Reviews about Products and more.
- The database for the live site is a Postgresql database added to the Heroku hosting 
- The database tables are as follows: 
![Image of Schema](https://github.com/clacken-dev/ms4/blob/main/documentation/db_schema_v2.png?raw=true)

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
  - short_description
  - lead_time
  - image_url
  - image
- Order
  - user (ForeignKey)
  - service (ForeignKey)
  - order_number
  - date
  - total
  - description
  - image
  - is_fulfilled
  - changes_requested
- Image
  - image
  - image_url
- Review
  - user (ForeignKey)
  - product (ForeignKey)
  - review_title
  - review
  - date

## Wireframes 
![Wireframe1](https://github.com/clacken-dev/ms4/blob/main/documentation/wireframe1.png?raw=true)
![Wireframe2](https://github.com/clacken-dev/ms4/blob/main/documentation/wireframe2.png?raw=true)
![Wireframe3](https://github.com/clacken-dev/ms4/blob/main/documentation/wireframe3.png?raw=true)
![Wireframe4](https://github.com/clacken-dev/ms4/blob/main/documentation/wireframe4.png?raw=true)
![Wireframe5](https://github.com/clacken-dev/ms4/blob/main/documentation/wireframe5.png?raw=true)


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
 - The site features a responsive design with intuitive feedback. Layout is straightforward and simple and allows customers to easily navigate, purchase products, review orders and view their purchased items.
 - Secured pages with registration and login necessary for key functions
 - Admin dashboard for control of products, users, orders and other elements created on the site via user or admin interaction
 - Integrated billing functionality provided by Stripe component
 - Email sending with user registration and order completion
# Testing

## Validation
- The site was tested for compliance with HTML best practice, CSS best practice and to ensure all Python was PEP8 compliant insofar as possible. All python code was gone through and updated and all possible errors were removed. Errors to note which remain are in four lines of DJango settings.py file which were left as originally generated in order to maintain Django settings integrity as well as errors stating that certain models do not contain a .objects property. This error was researched and is not inherintly an error but moreover a miscommunication between the pylint and the codebase. A workaround is possible but not stricly necessary considering it technically conforms to standards.
- Site was validated with W3C Markup Validator and with W3C CSS Validator to ensure site complied with best practice and layout of both languages
## Error Free HTML
![Link to Markup Results](https://github.com/clacken-dev/ms4/blob/main/documentation/html-v2.png?raw=true)
## Error Free CSS 
![Link to CSS Results](https://github.com/clacken-dev/ms4/blob/main/documentation/css-v2.png?raw=true)
- Python Linter was used to identify and rectify pep8 compliance issues in environment wherever possible
## Chrome Devtools Lighthouse
- Lighthouse was used to assess the design and efficacy of the site and its performance. The results were good overall
![Lighthouse Results](https://github.com/clacken-dev/ms4/blob/main/documentation/v2-lighthouse.png?raw=true)

# Testing User Stories

## Further Testing
- Extensive further testing was carried out on all features and functions of the site and can be viewed in the TESTING.md file linked below
- [TESTING.md](https://github.com/clacken-dev/ms4/blob/main/TESTING.md)

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
 - There are small styling issues to be ironed out, mostly around spacing and footer position.
 - Messages not displaying until navigating to admin panel
 - The functions for requesting changes to the order do not correctly update the is_fulfilled value and this negatively affects the Orders display page. Updating an order with an image should move it from UnFulfilled to Fulfilled and simultaneously update the is_fulfilled Boolean value in the Order model. Requesting a change should update the is_fulfilled to False again thereby placing it again in the Unfulfilled section of the Orders page.

# Deployment

## Repository set up
- This app was developed in Gitpod and pushed to a GitHub repository which was connected to Heroku with automatic deployments. The steps for cloning and hosting are below.

Ensure your requirements.txt is up to date.

    pip3 freeze --local > requirements.txt - Ensure there is a Procfile in your repository with the following: 
    web: gunicorn bookaband.wsgi:application

In your Heroku account create a new app and select a region. Link this app to the relevant GitHub Repository by searching the repo and pressing 'connect'.

### Postgres Database Setup

Navigate to resources at the top of page, search for 'Heroku Postgres' and confirm which package you would like to use select.

In the App Settings reveal the config vars and add the following:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- DATABASE_URL
- EMAIL_HOST_PASS
- EMAIL_HOST_USER
- SECRET_KEY
- USE_AWS

Under the 'Deploy' tab, enable automatic deploys.
The Postgres URL can be entered in Django Settings.py and migrations can now be made to the hosted database on Heroku. Fixtures can be exported into a Json file using the command 

    python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json

This can then be uploaded to the connected Postrgres database using:

    python3 manage.py loaddata db.json

## Amazon AWS S3 Bucket
- The S3 bucket is used to host static files and media

After signing into the AWS dashboard it will be necessary to create an S3 Bucket in the S3 menu. Navigate to "Block Public Access" and allow access to the bucket. 

On the properties tab enable static hosting and save changes.

On the permissions tab ed the CORS section and enter the following permissions:

    
    [{
      "AllowedHeaders": ["
      Authorization"
      ],
      "AllowedMethods": [
        "Get"
     ],
      "AllowedOrigins": [
      "*"
     ],
      "ExposeHeaders": [],
     }]

Navigate to the bucket policy section and after clicking 'Edit' then select the Policy Generator from S3 Bucket Policy. Enter the ARN as found on the bucket and generate the policy.

Save all changes to the Bucket and then enter the IAM section of the AWS dashboard.

Create a new User Group and attach the policy created to the user group. Create a User and add this user to the User Group with Access Type of Programmatic. Download the .csv file and ensure to store the the details in a safe location.

## Connect Heroku to AWS S3

Install boto3 using pip3 and add this to the requirements.txt file.

Add the access credentials from the .csv file to Heroku Config Vars under the app settings. Create the Media and Static files in the Bucket in the S3 dashboard and enable COLLECTSTATIC so that Heroku will collect static files and store new ones in the S3 Bucket.

Now pushes to GitHub will automatically deploy to Heroku which in turn will update using the S3 Bucket to store static files.

## Forking Repository

Log into GitHub and at the top right of the page while looking at the repository the Fork button is visible. Clicking this gives the option to fork it for personal use.

## Making a Clone of the Repository to run locally

Click the Code dropdown button located above the repository and copy CLI code to enter in the local development environment:
    
    gh repo clone clacken-dev/ms4

Install the necessary requirements from the requirements.txt file using the following command:

    pip3 install -r requirements.txt

The app can now be run from the local environment


# Credits
### Code
- Site design is based off Code Institute's Boutique Ado and borrows features and functionality from it. Most elements are adapted as needed and all are attributed in the code. 
- Some design, layout and logic was inspired from other MS4 projects and those looked at are mentioned below:
  - [Joyce English School by AideenM12](https://github.com/AideenM12/Joyce-English-School-MS4)
  - [Book A Band by OlieHickie](https://github.com/OliHickie/book_a_band)
  - [Milestone Project 4 by Puksrevolution](https://github.com/Puksrevolution/milestone-project-4)
  - [Coached by Caoimhe by Bozy15](https://github.com/Puksrevolution/milestone-project-4)

### Images
- Images used were downloaded from Unsplash and Pexels and are royalty free under Creative Commons

## Acknowledgments
- This project was inspired by Code Institute's Boutique Ado project.

 - Many thanks go to my mentor for his continued support throughout the project.

- Thanks  to the Code Institute tutor team for their guidance and help.
- The Slack Community