![The Note magazine](https://res.cloudinary.com/kdcloud-8710/image/upload/v1653936713/webpage_ss_j3s0lp.jpg)



# User Experience (UX)

## Strategy

### Project Goals

The main business goal for The Note magazine is to provide users with a blog-style website with various posts about music, concerts, reviews accessible for the user to view. The user can create an account to be able to further interact with these blog posts via likes and leaving comments.

The main target audience for this website are music-lovers, music fans who enjoy informing themsleves about any music topics coming from different levels of music intrest. This is also a website for users to be able to share their comments and reviews among the cummunity.



### User Stories

* __Site User Goals:__

    * As a user I can register an account so that I can comment and like
    * As a user I can navigate easily through the site so that find the relevant information with ease
    * As a user I can view a list of posts so that I can select one to read
    * As a admin/user I can select the category of the post so that I can read what I am interested in
    * As a user I can view a paginated list of posts so that I can select which post I want to view
    * As a user / admin I can view the number of likes on each post so that I can see which is the most popular or viral
    * As a user I can click on a post so that I can read the full text
    * As a user I can like or unlike a post so that I can interact with the content
    * As a user / admin I can view comments on an individual post so that I can read the conversation/reviews
    * As a user I can comments on a post so that I can be involved in the conversation/leave reviews


* __Site Admin Goals:__

    * As a admin I can prevent unauthorized users from having access so that they cannot access admin content or other user's profiles
    * As a admin I can create draft posts so that I can finish writing the content later
    * As a admin I can create, read, update and delete posts so that I can manage my blog content
    * As a admin I can approve or disapprove comments so that I can filter out objectionable comments
    * As a admin I can add a post on the webpage so that I can create a post easily
    * As a admin I can edit a post so that I can modify the content from the webpage
    * As a admin I can delete a post so that I can control of which post is published


## Scope

To achive the strategy goals, I want to implement the following features:

* A category navigation bar fixed at the top of the screen which will allow the user to easily navigate and find the rekevant sections.
* A home section which allow the user to find out about the latest posts.
* A login page for existing users to access their account to allow to like and add comments.
* A register/signup page to allow new users to create an account.
* A search bar to allow users to enter specific post in more detail for the recipes and add comments/like the post.
* A fully responviedesign that will work on different devices including desktop, tablets, and mobile devices, allowing users to access the site anytime and anywhere.
* An Error 404 page to allow users to redirect back to H/ome page in case of any errors.
* A full CRUD functionality for Admin to allow to create, read, update and delete posts.

## Design 

### Colours

I have used white for the overall background colour fo the website, accompanied by black and #140C40 for the header to noteably distinguish this from the main content.

For the text, black has been used against the white background. this opposite contrast has been chosen for ease of visibility, so users are able to read the text without any additional difficulty.

### Typography

The fonts were obtained from [Google Fonts](https://fonts.google.com/).

....

### Imagery 

Images are obtained from the Google search thourgh different sources.

I have used imagery appropriate to the website's content to provide a more visual experience to the user.


## Skeleton

### Wireframes

Wireframes were created using my book and pencil.

The wireframes have examples of desktop, tablet, and mobile phone displays.

* Home link
* Post detail link
* Register link
* Login link
* Add, Edit link

Overall, the finished projects design is similar to what I had originally intended to create as per my wireframes.

### Database

A relational database was used for this project.

During production SQLite/Postgres was used as the main database, and for deployement all data was migrated to Heroku Postgres.

Please note that for testing purposes SQLite database was used. In the setting.py code was added to allow for the databases to be switched between SQLite for the testing and Postgres for regular producion.

Photo here

The database diagram was created using 

The database contains the following models

* __Post__:
* __Comment__:
* __Category__:

## Features

### Current Features

For this project I opted for a website with different pages accessed by clicking the navlinks, this is fully responsive and consiss of a header, footer and the following main section; Home, Sign Up, Login, Search, Add post if Admin is logged in.

__Navigation__:

    * This feature is presnet on all the pages/sections and is fixed to the top.
    * The hearder section has fully responsive navigation bar which consists of the logo, located on the middle.
    * The navigation buttons for Home, Sign Up, Login (located right-hand side after the logo) and a Search bar (located on the left-hand side).
    * The navigation buttons for categories are located underneath the logo at the bottom part of the header navigation bar.
    * The search bar has a placeholder text to indicate to the user that they can enter text in the box provided.


__Home__:

    * This is the default page displayed when the user accesses the website.
    * This page can also be viewed by clicking The Note magazine logo or the home button from the navigation bar.
    * The latest posts from all categories are displayed (max of 6) per page.
    * The is a 'Next' button that allows user to click and navigate to the next page to view more articles.
    * Alternatively 'Prev' button can be clicked to return a page back.
    * Acticle psots are displayed from most recent to oldest.
    * Each post is displayed in a card style with an image, title, date, like count (And if Admin logged in, can see Edit and Delete buttons).
    * Selecting the clickable text or image will take the user to the 'Post detail' page to display the full content of the article.

__Post Detail__:

    * Accessed once the user selects an article from the 'Home' or 'Search' or 'Category' page.
    * Article image will be displayed at the top.
    * Content is then followed by the title, author, date, (if Admin, Edit and Delete button).
    * Like button and comment count, sharing socials icon.
    * Further below is the comment section which users can view even if not logged in.
    * Comemnt section is available and displayed for logged in users who can submit a comment.
    * This is then sent for approval which is feature only the Admin can access.
    * Alert is displayed to indicate the comment has been sent for approval.
    * Approved comments can be viewed on the post.

__Sign Up__:

    * Accessed from the navigation bar by selecting the 'Sign Up' button.
    * Once selected, the user is taken to the 'Sign Up' page.
    * New users are prompted to enter a username, email (optional), are requiered for the user to be able to create an account, otherwise an error is displayed.
    * All fields apart from the email (optional) are required for the user to be able to create an account, otherwise an error is displayed.
    * Upon successful creation the user is then able to login to the account.
    * Alert is displayed to indicate that the user has signed in.
    * Exisiting users are provided with the sign in to take them to the 'Login' page.

__Login__:

    * Accessed from the navigation bar by selecting the 'Login' button.
    * Once selected, the user is taken to the 'Login' page.
    * Existing users can enter their username and password and click the login button.
    * Upon successful login, user is taken to the 'Home' page.
    * Alert is displayed to indicate that the user has signed in.
    * Incorrect username and password will faily to log the user into their account and a message will be displayed on the 'Login' page to indicate this.
    * New users are provided with the register link to take them to the 'Sign Up' page to create an account.

__Logout__:

    * Option only available to users who are currently logged in.
    * Accessed from the navigation bar by selecting the 'Logout' button.
    * Once selected, user will be taken to the 'Sign Out' page to confirm that they wish to sign out from their account.
    * User can select the sign out button option which will successfully sign out the user from their account and return them to the home page.
    * Alert added to indicate that the user has signed out.


__Search__:

* Accessed from the navigation bar in the top left-hand corner. 
* Placeholder text added to indicate to the user that text can be entered in the input box.
* User cannot submit an empty search and user has to enter a max of 1 character otherwise an error is displayed.
* User is able to click the search button once the requirements are met (as stated above), this will take the user to the 'Search' page.
* User is able to scroll down and view the displayed results of the articles which match the keywords entered.
* Prior to the search results, the user is displayed with the keyword searched and below the results are displayed.
* For any successful matches display the recipe card (same as the ones on the 'Home' page), the user can click this and be taken to the recipe page.
* For any unsuccessful matches, the user is displayed with a message to state that no results have been found for this keyword.

__Footer__:

* This feature is present on all the pages/sections and is fixed to the top.

__Features Exclusive to Admin__:

    * Only the Admin can approvem and delete user comments.
    * Only the Admin can createm update and delete posts.

### Future Features

Due to time constraints, I was unable to apply additional features, in the future I would like to implement the following:

* Allow users to edit/delete their own posted comments.
* Improving the User experience on the website, with the ability to like a post with a reaload of the page.


## Technologies Used

For this project the main languages used are __HTML5__, __CSS3__, __JavaScript__, __Python__, __Django__ and __Heroku Postgres__.

I have also utilised the following frameworks, libraries, and tools:

* [Bootstrap v5.1.3](https://getbootstrap.com/): 
    * Bootstrap has been used for overall responsiveness of the website and for the layout with the addition of select classes.
* [GitPod](https://www.gitpod.io/): 
    * I used GitPod as the IDE for this project and Git has been used for Version Control.
* [GitHub](https://www.github.com/): 
    * GitHub has been used to create a repository to host the project and receive updated commits from GitPod.
* [Balsamiq](https://balsamiq.com/): 
    * I used Balsamiq to create the wireframe for the website for the basic structure and layout.
* [dbdiagram](https://dbdiagram.io/home): 
    * I used dbdiagram to create the database diagram model for the website.
* [Google Fonts](https://getbootstrap.com/): 
    * I have used Google Fonts to import fonts for styling purposes for this project.
* [Font Awesome](https://fontawesome.com/): 
    * Font Awesome was used to apply icons in the Home, Exercises and Footer sections.
* [Affinity Photo](https://affinity.serif.com/en-gb/photo/): 
    * Affinity Photo is a program used to edit the favicon and picture for this project.
* [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools): 
    * Chrome Dev Tools was used to test the site, assist with debugging issues and run reports from Lighthouse.
* [W3C Markup Validation Service](https://validator.w3.org/): 
    * The W3C Markup Validation Service was used to validate the HTML document for this project and to identify any issues with the code.
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/): 
    * The W3C CSS Validation Service was used to validate the CSS document for this project and to identify any issues with the code.
* [JSHint Validation Service](https://jshint.com/): 
    * The JSHint Validation Service was used to validate the JavaScript document for this project and to identify any issues with the code.
* [PEP8 Online Validation Service](http://pep8online.com/): 
    * The PEP8 Online Validation Service was used to validate the Python document for this project and to identify any issues with the code.
* [Heroku](https://www.heroku.com/): 
    * Heroku has been used to create a repository to host the project and receive updated commits from GitPod.
* [Django](https://docs.djangoproject.com/en/3.1/): 
    * Django was used as the main framework to build this project.
* [Cloudinary](https://cloudinary.com/): 
    * Cloudinary was used to store all media and static files for this project.
* [Am I Responsive](http://ami.responsivedesign.is/):
    * Am I Responsive was used to create the header image for the README file.
* [Python](https://www.python.org/): 
    * Various Python modules were used to build this project as detailed below and as seen in the requirements.txt file.


## Testing

Testing for this project was completed manually and some auto unit testing was also implemented.