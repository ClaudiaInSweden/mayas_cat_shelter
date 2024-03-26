# Mayas Cat Shelter

## Introduction

### Project Description

[Mayas Cat Shelter](https://mayas-cat-shelter-9ef5d0b15271.herokuapp.com/) is a fictional cat shelter in the city of Gävle, Sweden. The structure, set-up as well as the background stories of the cats are losely based on a real local cat shelter, Gefle Katthem. 

![Mayas Cat Shelter](IMAGE)

Each page includes a responsive navigation bar as well as a footer with copyright information, social media links and a fictional telephone number. 
The start page includes an image carousel with two images which link to a page with available cats respective a page with information about the adoption process. 
From both pages a link to an adoption form is available for the user. 

Full CRUD functionality is reserved for the administrator role who can log-in/log-out in the navigation bar. When a user is logged in, an additional dropdown menu link is available to administrate cats (Create, Read, Update, Delete) as well as the incoming adoptions requests. However, the data in these requests is not editable but the user/administrator can change the status log and add comments. 
More details can be found in the respective Features section.  


## UX

Mayas Cat Shelter is for all people who love cats and consider to adopt one. 
Stumbling into the cat adoption world myself by accident, cat lovers come in all sizes, shapes, education levels, cultural backgrounds and ages. However, loving cats it not enough because when adopting a cat you take over the responsibility for a living being. And cats can be up to 20 years (or older) so it's really a long lasting relationship and should be well thought through. That's why I put much effort into the adoption rules & process page and tried to explain why a cat shelter is thorough in checking each application to find the perfect match. 


## Design

### Colors

The websites's color scheme uses soft tones that harmonize very well with each other. I wanted to have a color scheme that includes red and blue tones to represent female and male cats and found a palette that blends some calming greenish color with the mentioned red and blue and makes it look very appealing.

### Typography

I wanted to add a logotype representing a cat and found a nice image that I used for both the logotype, the favicon and as placeholder image. The font "Playpen" works very well with this logotype. For the body text I used "Prompt" with has a nice rounded form and is very well readable even on small screens. 


## Wireframes

Wireframes were created for desktop, iPad and smartphones using Balsamiq.
IMAGES

## Agile 

Agile Methodology was used during the project.
User stories were created at project start, and prioritized according to MOSCOW way of working. 
Github was used to document the user stories by using the build in Issues resp. project functionality.
For each user story a list of tasks and acceptance criterias was created.
Working progress was illustrated in a canban board.
All user stories labelled "Must have" have been closed. 
Open user stories have been collected in the backlog section. 

The project is open for public access and can be visited here.
![Agile Project](https://github.com/ClaudiaInSweden/mayas_cat_shelter/projects)
![Project User Stories](IMAGE)


<hr>

## Features

### Navigation

The responsive navigation bar on top of the page includes links to the Home Page, Our Cats, Adoption, Staff Login. When a user is logged in, a Logout link is visible instead as well as a dropdown link with two sections, one to the cats administration page and the other one to a list of all adoption requests.
On smaller screens the links are replaced with a clickable toggle icon.

Image Navbar


### Footer

The responsive footer sticks to the bottom of each page and includes copyright information, links to the social media platforms, Facebook, Instagram and Youtube and a fictional telephone number.


### Home Page

The Home page is the starting point for users. A carousel shows two alternating cat images with links to either the cats page or the adoption page. Some descriptive text about the cat shelter can be found below the carousel. 


![Home Page](https://hanneles-art-gallery.s3.eu-north-1.amazonaws.com/readme-docs/Homepage.jpg) IMAGE



### Our cats

On this page all available cats are listed with:
- Name (colored in red (female) or blue (male))
- Approx. birth date (originally I used a date field but realized in a later stage that cat shelters resp. vets often only can guess when a homeless cat is born so I updated this field to a textfield)
- Gender (depending on gender, displayed in red (female) or blue (male))
- Background and Temperament
-  



### Painting details

Again, the focus is on the painting and the user might need to scroll down to see the price.

To keep the interest alive and display a full collection of the artwork it's decided to leave the sold paintings in the shop but with a "SOLD" label and no price and no "Add to cart" button available. 
At the time of project submission there is not yet an automatically function implemented to change the status of a painting. This is possible through the product management page which is available for superusers. However, an automated function should be implemented in phase 2.

![Painting details](https://hanneles-art-gallery.s3.eu-north-1.amazonaws.com/readme-docs/painting_detail.jpg)
![Confirmation window](https://hanneles-art-gallery.s3.eu-north-1.amazonaws.com/readme-docs/add_to_cart.jpg)


### Shopping cart

On the shopping cart page the user can see an overview of the paintings in the shopping cart as well as total costs including a delivery flat rate. As the paintings don't differ a lot in sizes and can easily be packaged I decided to use a flat rate for delivery. 
Here the user also has the possibility to remove a painting from the cart or go back to the paintings overview page. 

![Shopping cart](https://hanneles-art-gallery.s3.eu-north-1.amazonaws.com/readme-docs/shopping_cart.jpg)

If the user deletes all items in the shopping cart some info text will be displayed, telling the user that the shopping cart is empty; and a button to the paintings overview page. 

If the user clicks the Complete checkout button the user will be directed to the checkout form. Also here the user can see what paintings are in the shopping cart and the total sum. 

### Checkout

On the checkout page the user can see a short summary of the order on the right side and a form on the left side. 
The form asks for name, email and the delivery address. When the user is already registered and logged in, the address will be pre-populated. As the location for the webshop is in Sweden, it was decided to use only the address fields that are common in Sweden, so state/county has not been used. 
On the bottom of the page you can find the Stripe credit card section for the user to fill in credit card number, valid date, CVV and zip code.
As only a Stripe test account is used, an error will be displayed when a credit card number other than the test card number 4242 ... is entered.
Also here the user can still choose to interrupt the checkout process and go back to the paintings page. 

![Checkout Page](https://hanneles-art-gallery.s3.eu-north-1.amazonaws.com/readme-docs/checkout.jpg)

When the user completes the form and clicks on Complete Order the Checkout Success/Order confirmation page is opened. 


### Order confirmation

While the payment transfer is ongoing a spinning overlay is displayed to inform the user that the transaction is ongoing.

![Checkout overlay](https://hanneles-art-gallery.s3.eu-north-1.amazonaws.com/readme-docs/checkout_overlay.jpg)

Once the transaction is completed successfully an order confirmation page is displayed informing the user that a confirmation email has been sent to the provided email address. Also an order summary with the delivery address is visible as well as a button back to the paintings page. 

![Order confirmation](https://hanneles-art-gallery.s3.eu-north-1.amazonaws.com/readme-docs/order_confirmation.jpg)


### My Account

Under the My Account menu tab in the navigation the user will see different options depending on the log-in status:
- When the user is not logged in a Registration and a Log-in Option are available. They open Allauth templates which are Bootstrap-styled to match the rest of the website. The log-in page offers also the possibility to restore the password in case it's been forgotten.
- When the user is already loggeg in, a Log-out option will be visible instead. 
- When a user is logged in as a superuser, the Product Management link is available that leads to a page that enables to add another painting. Contrary to the Walkthrough project the image upload is mandatory as we cannot sell paintings without being able to show them to the user. 

![Not logged in](https://hanneles-art-gallery.s3.eu-north-1.amazonaws.com/readme-docs/account_logged_out.jpg)
![Logged in as administrator(https://hanneles-art-gallery.s3.eu-north-1.amazonaws.com/readme-docs/account_logged_in.jpg)]







## Technologies used

### Languages
- HTML5
- CSS
- JavaScript
- jQuery
- Python
- Django

### Technologies and programs
- IDE: Gitpod/VS Code
- Repository: GitHub
- Database: ElephantSQL
- Payment solution: Stripe
- Storage: AWS S3 for storing media and static files
- Deployment: Heroku

### Software and frameworks
![Colorlib template "Pillowmate"](https://themewagon.com/themes/free-bootstrap-4-html5-responsive-online-store-template-pillow-mart/)
![Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
![Fontawsome Icons](https://fontawesome.com/icons)
![Favicon](https://favicon.io/)
![Birme](https://www.birme.net/)
![Snagit Editor](https://www.techsmith.com/screen-capture.html)




## Testing

### Validator Testing

#### HTML

A lot of errors were returned when passing through the [W3C Markup validator](https://validator.w3.org/).
However, this must be due to the fact that the templates are rendered differently. When I compare the errors with the actual code they do not correspond at all. This is the products page so the error repeats for the whole loop of 24 products. 
See example below.
![HTML Validator](https://hanneles-art-gallery.s3.eu-north-1.amazonaws.com/readme-docs/HTML+Validator-errors.jpg)
![HTML Validator](https://hanneles-art-gallery.s3.eu-north-1.amazonaws.com/readme-docs/HTML+Validator.jpg)


#### CSS

No errors were found when passing through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) validator
![CSS Validator](https://hanneles-art-gallery.s3.eu-north-1.amazonaws.com/readme-docs/CSS_Validator.jpg)

#### Google Chrome Lighthouse Reports

These reports presents the results of Lighthouse testing to assess the performance, accessibility, best practices and SEO of Hanneles Art Gallery.

The tests were executed using the Google Chrome browser's DevTools.
ADetails for each page can be found by clicking the expand button.
![Home](https://hanneles-art-gallery.s3.eu-north-1.amazonaws.com/readme-docs/lighthouse_home.jpg)
![Paintings](https://hanneles-art-gallery.s3.eu-north-1.amazonaws.com/readme-docs/lighthouse_products.jpg)
![Paintings Details](https://hanneles-art-gallery.s3.eu-north-1.amazonaws.com/readme-docs/lighthouse_product_detail.jpg)
![Shopping Cart](https://hanneles-art-gallery.s3.eu-north-1.amazonaws.com/readme-docs/lighthouse_cart.jpg)
![Checkout](https://hanneles-art-gallery.s3.eu-north-1.amazonaws.com/readme-docs/lighthouse_checkout.jpg)
![My Profile](https://hanneles-art-gallery.s3.eu-north-1.amazonaws.com/readme-docs/lighthouse_myprofile.jpg)
![Product Management](https://hanneles-art-gallery.s3.eu-north-1.amazonaws.com/readme-docs/lighthouse_product_management.jpg)

#### JavaScript validation
Due to lack of time this step could not be performed.


#### Python validation
Due to lack of time this step could not be performed.



## Browser Testing

Functionality, links, layout, and responsiveness were tested with the following browsers without any major issues:

- Microsoft Edge Version 117.0.2045.47
- Firefox Version 118.0.1
- Brave Version 1.58.135
- Google Chrome Version 116.0.5845.188
  

## Bugs
Due to a bug regarding Stripe webhooks hours of research were spent and finally solved with help from Rebecca from Tutor Service.
However, due to this major issue, the project could not be finalized on time.



## Credits

All painting images belong to Hannele Hannele Kaarlejärvi
![404 Error Image](https://www.vecteezy.com/free-vector/painting-stand)
![Bootstrap-4-multi-dropdown-navbar:]
![Bootstrap Template "Pillow Mart"](https://themewagon.com/themes/free-bootstrap-4-html5-responsive-online-store-template-pillow-mart/)