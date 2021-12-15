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

# Features

# Testing (Link to Testing.md, view yoga app table of tests)

# Bugs

# Deployment

# Credits