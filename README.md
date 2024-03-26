# Mayas Cat Shelter

## Introduction

### Project Description

[Mayas Cat Shelter](https://mayas-cat-shelter-9ef5d0b15271.herokuapp.com/) is a fictional cat shelter in the city of Gävle, Sweden. The structure, set-up as well as the background stories of the cats are losely based on a real local cat shelter, Gefle Katthem. 

![Mayas Cat Shelter](static/readme-images/screenshots-pages/amiresponsive1.png)
![Mayas Cat Shelter](static/readme-images/screenshots-pages/amiresponsive2.png)

Each page includes a responsive navigation bar as well as a footer with copyright information, social media links and a fictional telephone number. 
The start page includes an image carousel with two images which link to a page with available cats respective a page with information about the adoption process. 
From both pages a link to an adoption form is available for the user. 

Full CRUD functionality is reserved for the administrator role who can log-in/log-out in the navigation bar. When a user is logged in, an additional dropdown menu link is available to administrate cats (Create, Read, Update, Delete) as well as the incoming adoptions requests. However, the data in these requests is not editable but the user/administrator can change the status log and add comments. 
More details can be found in the respective Features section.  


## UX

Mayas Cat Shelter is for all people who love cats and consider to adopt one. 
Stumbling into the cat adoption world myself by accident, cat lovers come in all sizes, shapes, education levels, cultural backgrounds and ages. 
So, target group for this website are all people who love cats, but of course merely those who live close to the cat shelter. 



## Design

### Colors

The websites's color scheme uses soft tones that harmonize very well with each other. I wanted to have a color scheme that includes red and blue tones to represent female and male cats and found a palette that blends some calming greenish color with the mentioned red and blue and makes it look very appealing.

![Color palette](static/readme-images/others/color_palette.png)

### Typography

I wanted to add a logotype representing a cat and found a nice image that I used for both the logotype, the favicon and as placeholder image. The font "Playpen" works very well with this logotype. For the body text I used "Prompt" with has a nice rounded form and is very well readable even on small screens. 


## Wireframes

Wireframes were created for desktop, iPad and smartphones using Balsamiq.

#### Home Page
![Home Page Desktop](/static/readme-images/wireframes/Home.png)

![Home Page iPad](/static/readme-images/wireframes/Home iPad.png)

![Home Page Smartphone](static/readme-images/wireframes/Home Smartphone.png)

#### Our Cats
![Our Cats Desktop](/static/readme-images/wireframes/Our Cats.png)
![Our Cats iPad](static/readme-images/wireframes/Our Cats iPad.png)
![Our Cats Smartphone](static/readme-images/wireframes/Our Cats Smartphone.png)

#### Adoption
![Adoption Rules Desktop](static/readme-images/wireframes/Adoption Rules.png)
![Adooption Rules iPad](static/readme-images/wireframes/Adoption Rules iPad.png)
![Adoption Rules Smartphone](static/readme-images/wireframes/Adoption Rules Smartphone.png)

#### Adoption Form
![Adoption Form Desktop](static/readme-images/wireframes/Adoption Form.png)
![Adoption Form iPad](static/readme-images/wireframes/Adoption Form iPad.png)
![Adoption Form Smartphone](static/readme-images/wireframes/Adoption Form Smartphone.png)

#### Administration Cats
![Admin Cats Desktop](static/readme-images/wireframes/Administration Cats.png)
![Admin Cats iPad](static/readme-images/wireframes/Administration Cats iPad.png)
![Admin Cats Smartphone](static/readme-images/wireframes/Administration Cats Smartphone.png)

#### Administration Adoption Requests
![Admin Adoption Desktop](static/readme-images/wireframes/Administration Adoptions.png)
![Admin Adoption iPad](static/readme-images/wireframes/Administration Adoptions iPad.png)
![Admin Adoption Smartphone](static/readme-images/wireframes/Administration Adoptions Smartphone.png)

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
![Project User Stories](static/readme-images/others/user-stories.png)


<hr>

## Features

### Navigation

The responsive navigation bar on top of the page includes links to the Home Page, Our Cats, Adoption, Staff Login. When a user is logged in, a Logout link is visible instead as well as a dropdown link with two sections, one to the cats administration page and the other one to a list of all adoption requests.
On smaller screens the links are replaced with a clickable toggle icon.

![Navbar](static/readme-images/screenshots-pages/navbar.png)


### Footer

The responsive footer sticks to the bottom of each page and includes copyright information, links to the social media platforms, Facebook, Instagram and Youtube and a fictional telephone number.

![Footer](static/readme-images/screenshots-pages/footer.png)


### Home Page

The Home page is the starting point for users. A carousel shows two alternating cat images with links to either the cats page or the adoption page. Some descriptive text about the cat shelter can be found below the carousel. 


![Home Page](static/readme-images/screenshots-pages/amiresponsive2.png)



### Our cats

On this page all available cats are listed with:
- Name (colored in red (female) or blue (male))
- Approx. birth date (originally I used a date field but realized in a later stage that cat shelters resp. vets often only can guess when a homeless cat is born so I updated this field to a textfield)
- Gender (depending on gender, displayed in red (female) or blue (male))
- Background and Temperament
- Adoption status (when a cat is already adopted, the "Adopt" button is replaced with just some info text accordingly)
- Adopt Button that links to the adoption form

![Our Cats](static/readme-images/screenshots-pages/cats.png)


### Adoption

The adoption page includes information about what to consider when adopting a cat, the costs and the process steps.
On the bottom of the page a button links to the adoption form. 

![Adoption](static/readme-images/screenshots-pages/adoption.png)


### Adoption Form

The adoption form consists of two parts:
1. The user fills in Name, E-Mail, Phone, Date of birth and some information about themselves. 
2. The user selects up to three cats to adopt. It's also possible to search for cat names.

When clicking the submit button, the user will be redirected to the start page and a confirmation message will be displayed for 5 seconds. It is also possible to remove the message by closing it manually. 

![Adoption Form](static/readme-images/screenshots-pages/adoption-form.png)


### Administration for staff

When a staff member is logged in, the administration dropdown menu will be visible in the navbar.
Two options are available:


#### Administration Cats 

The staff member will see a table of all cats, both with status published or draft. 
The table contains the cat name, gender, adoption status and publication status. On the right side there's an edit and delete button for each row/cat. 
On top of the page, a "Add a cat" button links to the add cat form. To populate a new cat, name, gender need to be entered. Publication status as well as adoption status are mandatory, but have default values ("Draft" resp. "Ready for adoption"). If no image is uploaded, a default image with a cat silhoutte (same as logo and favicon) will be added. 
When the staff member clicks on the edit button in the cat table, the same form will be opened, but with the cat data pre-populated. 
When the staff member clicks on the delete button in the cat table, a confirmation page will be opened, asking for a confirmation to delete the cat. When the user confirms deleting, the cat will be deleted and the user redirected to the cat administration page. If the user clicks on Cancel, the user will be redirected back to the cat administration page. 

![Admin Cats](static/readme-images/screenshots-pages/admin_cats.png)


#### Administration Adoption requests

The staff member will see all adoption requests in card form, sorted by date. The idea with this page is that the staff can see at one glance all information about an adopter. A staff member can also edit the status of the adoption request, following the steps outlined on the adoption page, and add comments. 
Personal data of the adopter is not editable in this view! 
However, as there is the possibility that either the interested adopter or the cat shelter staff conclude that the choosen cat might not be the right one for this person, the cat selection list is editable for staff members. 

![Admin Adoptions](static/readme-images/screenshots-pages/update_status.png)


### Login/Logout

The navigation bar includes a "Staff Login" link for staff members to log in. This might not be best practise for real cases but it's the easiest way to log in for the project assessors at Code Institute.
However, I have removed the link to the "Sign in" page to avoid sign in attempts of page visitors. 
When a staff member is logged in, the "Staff Login" link will change to "Logout".

Non-staff users who try to access one of the administrator pages (add-cat, update-cat, delete-cat, update-status), will be redirected to the Login page.


## Information Architecture

### Relationship Diagram

![ERD](static/readme-images/others/PP4_Entity Relationship Diagram.drawio.png)

### Data Models

#### Cats Model

id (PK): unique identifier for each cat
name (string): Name of the cat
date_born (string): month and year when cat is born
gender (choice): female or male
description (textfield): A description of the cats background and temperament
image (image upload to Cloudinary): picture of cat or placeholder image
status (choice): draft or published
adopt_status (choice): Not yet ready for adoption, ready for adoption, booked, adopted
date_created (date): set automatically to todays date

#### Adoption Model

id (PK): unique iedentifier for each adoption request
full_name: (string) Name
email (email field): Email 
phone (phonenumber): phone number
date_of_birth (date input): date, validates if adopter is 19 years or older
about_you (text area): Freetext field
cats (ManyToMany relationship to cats): to select up to three cats 
received (date): set automatically to todays date
status (choice): for admin to set according to where in the adoption process they are
comments (text field): for admin to fill in


#### CRUD Functionality
Administrator can create, read, update and delete cats
Administrator can read and update adoption requests
User can read non-restricted content


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

No errors were returned when passing through the [W3C Markup validator](https://validator.w3.org/).
Details for each page can be found by clicking the expand button.
 

<details>

<summary>HTML Validation </summary>
![Home Page](static/readme-images/validation-html/index.png)
![Our Cats](static/readme-images/validation-html/cats.png)
![Adoption](static/readme-images/validation-html/adoption.png)
![Adoption Form](static/readme-images/validation-html/adoption_form.png)
![Admin Cats](static/readme-images/validation-html/cats_administration.png)
![Admin Adoption](static/readme-images/validation-html/adoption_administration.png)
![Login](static/readme-images/validation-html/login.png)
![Logout](static/readme-images/validation-html/logout.png)

</details>



#### CSS

No errors were found when passing through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) validator
![CSS Validator](static/readme-images/validation-css/validation-css.png)

#### Google Chrome Lighthouse Reports

These reports presents the results of Lighthouse testing to assess the performance, accessibility, best practices and SEO of Mayas Cat Shelter.

The tests were executed using the Google Chrome browser's DevTools.
Details for each page can be found by clicking the expand button.

<details>

<summary>Lighthouse Reports</summary>

![Home](static/readme-images/validation-performance/index.png)
![Our Cats](static/readme-images/validation-performance/cats.png)
![Adoption](static/readme-images/validation-performance/adoption.png)
![Adoption Form](static/readme-images/validation-performance/adoption_form.png)
![Admin Cats](static/readme-images/validation-performance/cats_administration.png)
![Admin Adoptions](static/readme-images/validation-performance/adoption_administration.png)
![Login](static/readme-images/validation-performance/login.png)
![Logout](static/readme-images/validation-performance/logout.png)

</details>


#### Python validation
No errors were returned when passing through the [CI Python Linter](https://pep8ci.herokuapp.com/).
Details for each part can be found by clicking the expand button.
 

<details>

<summary>Python Linter </summary>
![models.py](static/readme-images/validation-python/models_py.png)
![forms.py](static/readme-images/validation-python/forms_py.png)
![admin.py](static/readme-images/validation-python/admin_py.png)
![urls.py](static/readme-images/validation-python/urls_py.png)
![views.py](static/readme-images/validation-python/views_py.png)

</details>



## Browser Testing

Functionality, links, layout, and responsiveness were tested with the following browsers without any major issues:

- Microsoft Edge Version 117.0.2045.47
- Firefox Version 118.0.1
- Brave Version 1.58.135
- Google Chrome Version 116.0.5845.188
  

## Bugs




## Credits

#### Cats images:
![Default image, logo & favicon](https://www.vectorportal.com)
![All Cats](https://unsplash.com)

#### Code Snippets & Tutorials:
![Fieldset and legend revert](https://stackoverflow.com/questions/70536735/override-bootstrap-5-fieldset-style)
![Django Select2](https://www.youtube.com/watch?v=Zzd4sL7drKQ&list=PL-2EBeDYMIbQIu4aMZYqM6_w1ihIKWIql&index=19&pp=iAQB)
![Bootstrap5 Documentation](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
![Django Documentation](https://docs.djangoproject.com/en/4.2/)
![W3Schools](https://www.w3schools.com/)
