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
- Adoption status (when a cat is already adopted, the "Adopt" button is replaced with just some info text accordingly)
- Adopt Button that links to the adoption form  


### Adoption

The adoption page includes information about what to consider when adopting a cat, the costs and the process steps.
On the bottom of the page a button links to the adoption form. 


### Adoption Form

The adoption form consists of two parts:
1. The user fills in Name, E-Mail, Phone, Date of birth and some information about themselves. 
2. The user selects up to three cats to adopt. It's also possible to search for cat names.

When clicking the submit button, the user will be redirected to the start page and a confirmation message will be displayed for 5 seconds. It is also possible to remove the message by closing it manually. 


### Administration for staff

When a staff member is logged in, the administration dropdown menu will be visible in the navbar.
Two options are available:


#### Administration Cats 

The staff member will see a table of all cats, both with status published or draft. 
The table contains the cat name, gender, adoption status and publication status. On the right side there's an edit and delete button for each row/cat. 
On top of the page, a "Add a cat" button links to the add cat form. To populate a new cat, name, gender need to be entered. Publication status as well as adoption status are mandatory, but have default values ("Draft" resp. "Ready for adoption"). If no image is uploaded, a default image with a cat silhoutte (same as logo and favicon) will be added. 
When the staff member clicks on the edit button in the cat table, the same form will be opened, but with the cat data pre-populated. 
When the staff member clicks on the delete button in the cat table, a confirmation page will be opened, asking for a confirmation to delete the cat. When the user confirms deleting, the cat will be deleted and the user redirected to the cat administration page. If the user clicks on Cancel, the user will be redirected back to the cat administration page. 


#### Administration Adoption requests

The staff member will see all adoption requests in card form, sorted by date. The idea with this page is that the staff can see at one glance all information about an adopter. A staff member can also edit the status of the adoption request, following the steps outlined on the adoption page, and add comments. 
Personal data of the adopter is not editable in this view! 
However, as there is the possibility that either the interested adopter or the cat shelter staff conclude that the choosen cat might not be the right one for this person, the cat selection list is editable for staff members. 


### Login/Logout

The navigation bar includes a "Staff Login" link for staff members to log in. This might not be best practise for real cases but it's the easiest way to log in for the project assessors at Code Institute.
However, I have removed the link to the "Sign in" page to avoid sign in attempts of page visitors. 
When a staff member is logged in, the "Staff Login" link will change to "Logout".

Non-staff users who try to access one of the administrator pages (add-cat, update-cat, delete-cat, update-status), will be redirected to the Login page.




## Technologies used

### Languages
- HTML5
- CSS
- Python

### Technologies and programs
- IDE: Gitpod/VS Code
- Repository: GitHub
- Database: ElephantSQL
- Deployment: Heroku

### Software and frameworks
![Django 4.2](https://docs.djangoproject.com/en/4.2/)
![Bootstrap 5.1.3](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
![Fontawsome Icons](https://fontawesome.com/icons)
![Favicon](https://favicon.io/)
![Google Fonts](https://fonts.google.com/)
![Color palette](https://coolors.co/palettes/trending)
![Birme](https://www.birme.net/)
![Snagit Editor](https://www.techsmith.com/screen-capture.html)
![Balsamiq](https://balsamiq.com/)
![Draw.io](https://github.com/jgraph/drawio/wiki)




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