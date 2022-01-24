## Contents

### Testing Features
- Home

Testing the home section involved ensuring that the Brand was clearly visible and conveyed with the logo and header image and that the site purpopse was clear for a new user. Information hierarchy was tested to ensure there was logical flow of information down the home page and right onto the footer. The buttons to view the products and gallery are also clear, spaced out and let the user know their purpose.

### Navigation

- The navigation links were all tested to ensure they worked correctly by clicking through them and noting that the results were congruent with the labels. 

The Navigation also features different links for a guest user of the site with no account, for a registered user of the site and for the site admin. A guest will see the options to Log in or to Register which ensures that only features which are accessible to a guest user a visible. This test demonstrated that the navbar authentication works as expected and desired. 

Logged into a test user account without superuser priveleges also shows the necessary level of links for their status on the Navigation side. They can create orders, view the products and their own profile via the navigation but won't have any access by navigation links to any other portion of the site.

### Products Page

- Navigating to the products page displays a nicely laid out view of the products available. Information hierarchy is present with the product details following each other logically. 

Authentication on the products page was tested to ensure that only an admin has access to the product features such as editing and deleting. A guest user can view the products and also the product details but won't have any further access to editing or deleting a product or to ordering a product. A registered user can view the products and also order them but won't be shown the product links to edit or delete a product either. 

### Product Details page

- The product details page clearly lists the details associated with each product. The information is laid out in a way that makes the service clear to the user. 

Authentication on this page also works as desired. A guest will be directed to the signup page if they attempt to order a product. They will also not be shown the review form but instead links to signup or register in order to write a review. 

### Order Page

- The order page is available to registered users and is populated with the specific product the user has chosen from the product details page. The amount and service is shown and the directions are clear for the user. The user enters the details of the graphic they would like and are informed in red of the charge which will be made to their card if they continue with the purchase. 

### Stripe

- Stripe is incorporated into the order page to handle card payments. This comes with all of the Stripe authentication and checks and will also inform the user of any errors as they occur while entering their card details or when completing the purchase. This was tested with invalid details, empty details and the stripe test card. It is relevant to note that the functionality on this version of the site is functional due to using the stripe test card only. A fully developed live site would also need to submit billing details for the card owner. The security and credentials tests however all passed when auditing the Stripe features of the orders page. 

### Completed Order

- Upon completing an order the user is given their order number and told that their receipt will be emailed. They are then given a link to the profile where their completed graphic will be displayed. This was tested with creating orders and ensuring that the profile link worked and displayed the non-fulfilled order in the user profile. All worked as expected here.

### Profile Page

- The profile page was tested with non-fulfilled and fulfilled orders. It is clear to the user which orders are fulfilled as the finished graphic is displayed with the order. The finished order will also have the option to request changes to the graphic they have received. The request form loads and displays as expected and allows the user to submit the request. This then moves the order to non-fufilled as expected and the functionality works. On the programming side the form submission needs added capability to change the Boolean 'is_fulfilled' in the Order form, however the order is placed in the non-fulfilled orders regardless and so the interface side works as desired. 

 - The user-friendly message at the top of the page also clearly shows the relevant profile that the current orders are associated with. 

### Orders Page

- The orders page is accessible only to a site admin or superuser. The authentication of the site works to redirect a user without the necessary privileges. The site admin can view the orders on the orders page and the necessary order information including if the order is fulfilled or not. New orders will automatically be under the non-fulfilled heading as they do not contain any image. The admin has the option under these orders to update which will allow an image to be uploaded to the order. This will move the order to the fulfilled section of the site as desired. An order which a user has requested changes on will be under the Changes Requested heading. The admin can update these orders again with a new image as desired. This testing of the orders page ensured that it operates as expected and that orders behave logically based on whether they have been fulfilled or not. The order status is therefore clear for each order to the site admin. 

### Products Page - Superuser

- Viewing the products page as an admin or superuser was tested to ensure that the links display as they should under each product. This gives the admin the option to edit or delete products. Editing a product leads to an edit product page where the information is displayed about the current product. The message displays to the user what product they are currently editing. Submitting the edit form leads the user back to the products page where the updated product is visible. Deleting a product deletes the product as expected. 

### Review Product 

- Viewing the product details page as a registered user gives the user the option to write a new review for the current product. The form displays with the current product they are reviewing and submitting redirects properly to the page with the review now visible. 

### Viewing Gallery

- Viewing the gallery is the same for all users whether registered or not. The images load and the display is nicely laid out and gives the user an idea of the past work completed by the company. 

### Login/Sign-In/Register

- The account features all work as desired and expected for registering and logging in and out. Registration displays the form with the details required and gives a notification that the signup was successful. Upon validating an email the signup works to let the user log in and use the site features. Logging out displays a confirmation message to the user and redirects to the home page when logged out. All features which require registration are adequatly blocked from users who are not registered. 

### Route Handlers, URLs, Views

- All code was tested to ensure that it behaved as expected and that views worked as desired. Route handlers were tested to ensure they led to the correct functions. Views were tested to ensure the output was as desired and that the templates and context were passed through correctly. 

- PEP8 Compliance
    - All code was also gone through to ensure the highest possible level of PEP8 compliance and any issues flagged were noted in the README.md as being left as non-serious. 

## Future Features

- Future features to implement would be giving users the option to add their work to the graphics featured in the Gallery and display a review to the specific graphics.
- Adding a download link or displaying a finished graphic in a new tab.
- Add a feature for an admin to add new products on the products page for simplicity. 
- Send an email alert to a user when their order status changes so they know when to check their profile. 

