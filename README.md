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

### User Stories Testing

From the Home page,  the user is presented with the navugation which consists of the Note Magazine logo, Home button, Sign Up button and Login button on the right-hand side. Then on the left-hand side is the search bar with the Search box. Each of these buttons are functionable that the user can click or utilise. The following actions will occure once the user clicks the following buttons:

* The Note magazine Logo -> Defaults to the Home page, user can click this to take them back to the Home page
* Home button -> Links to the Home page, user can click this to take them back to the Home page
* Sign Up button -> Links to the Sign Up page, user can click this to take them to the Sign Up page
* Login button -> Links to the Login page, user can click this to take them to the Login page
* Search button -> Links to the Search page, user can only click this once the search criteria has been met (cannot be blank and a minimum of 1 characters), this will then allow for the form to be submitted.

the user can easily access the navigation categories as this is fixed at the top of the page and is accesable from all the pages of the website. On desktop view the navigation can be viewed in full but in mobile view this then collapses and is accessed from the burger menu.

Photo here...

Further down from the navigation, the user is presented with a greeting introductory message for The Note magazine website. This gives the user an idea that this is a articles magazine/blog.


Photo here....

The main section of the Home page displays the posted articles, there is a max of 6 articles displayed per page. The user can navigate between the acrticles pages by clicking Next button to go to the next page to view more articles or clicking Prev button to go to the previous page. The recipes are displayed in date order, the most recent posts are displayed first and the older articles will be displayed at the very end (or on a different page if exceeding 6 posts per page). Each recipe is presented with a card style with an image, the article title, category, posted date and time, and a like count. the user can select any article cards from the available articles by clicking the title or image. This action will take the user to the article page of that particular post.

Photo here ...

At the bottom of the page is the footer. The footer is present and can be seen from any page of the website. The footer provides the copyright text for the website.

Photo here....

the following user sotries have been achived from the section:

* As a Site User I can click on a post so that I can read the full text
* As a Site User I can view a list of posts so that I can select one to read
* As a Site User I can locate their social media accounts so I can receive updates and see their following and how well they are known and reliable
* As a Site User I can navigate easily through the site and find the relevant information with ease

Selecting the Sign Up button from the navigation will take the user to the Sign up page. This page can also be accessed by clicking the links available on the Login page. The page is provided with Sign Up section, any existing users with an account are prompted to go to the login page provided fomr the link. Any new users are prompted to enter the required details to be able to sign up. The fields username, password and password (again) are required fileds, therefore the user cannot submit a blank form for these. However the E-mail is an optinal field as stated on the form, therefore the user does not need to enter this to sign up to become a member.


Photo here ...

If the password section does not match for both fields, then the user will be presented with a message to state that they must type the same password each time to be able to create the account.

Photo here ...

If the password is too similar to the username the user will also be displayed with an error message. This is a security feature on the form to ensure the user's account cannot be acessed easily by creating a different and strong password.

Photo here ...

Once the sign up form fields have been successfully filled out and the user clicks the sign up button, then the user will be taken back to the Hope page and an alert message will be displayed at the top (below the navigation) to indicate that the user is signed is as their 'username' name. The navigation will now be updated to remove Sign Up and Login buttons with the Logout button.

photo here ...

Alternatively for any existing users with an account already created, by selecting the Login button from the button, this will take the user to the Login page. The link is also accessed from the sign up page for existing users. The page is displayed with the Login section, any new users are prompted to go to the sign up page provided from the link. Any existing users are prompted to enter the required details to be able to login. The user is required to enter their username and password which they previously used to create the account. The user also has an option to tick the 'Remeber Me' checkbox. 

Photo here ...

Once the user has entered the relevant details and clicked the login button to submit the form, they will be taken back to the Home page and an alert will be displayed at the top of the page (below the navigation) to notify the user that they have logged in successfully. The navigation bar will be changed once logged in as described above in a previous point.

Logged in users have the option to Logout from their account by selecting the Logout button from the navigation. By selecting the Logout button this will take the user to the Logout page. The page is displayed with the Sign Out section, the message prompts the user to confirm if they wish to sign out. Selecting the sign out button will confirm this choice and the user will be taken back to the Home page, and an alter will be displayed to confirm that the user has signed out. Users who do not wish to logout can click back to the Home page from the navigation (or any other page) to undo this action.

Photo here ...

Users with an account that are logged in have the option to add comments and like posts on the post detail page once an article is selected.

the main section of the article post is exactly the same for logged in users as if for users who are not logged in. The acticle title, author, time and date  and image are displayed at the top. Them further down is the main post body with the review/embbed playlist. At the end of the article body, there is like counter and comment counter displayed which will show how many users have liked the post and how many commetns does a post have.

phtoo here ...

With likes and comments:

photo here...

With no likes and comments:

phtoo here...

After the main article post, logged in users will be displayed with the comments section where any posted comments which have been approved by the asmin can be viewed, and the comment box where the can submit a comment. The comment box is only available for logged in users, wherears the comments section is visibke to both logged in users and users not logged in.

Logged in user view: 

Photo here ...

Generic view for non-members:

photo here ...

The comment box provides details to the user as to who they are posting as which corresponds to the username they have logged in with. Further down is the main comment body secion where the user is able to enter a comment. Once clicking the submit button, the user will be presented with an alert message to state that the comment has been sent for approval. Only the admin can approve comments. Once the admin has approved the comment, this can now be viewed on the article page.

Photo here ...

The following user stories have been achived from this section:

* As a Site User I can register an account so that I can comment and like
* As a Site User I can like or unlike a post so that I can interact with the content
* As a Site User I can leave comments on a post so that I can be involved in the conversation
* As a Site User/Admin I can view comments on an individual post so that I can read the conversation
* As a Site User/Admin I can view the number of likes on each post so that I can see which is the most popular or viral

Users are also able to utilise the search functionality on the website. This feature is accsessed from the navigation bar located on the left-hand side.

Photo here ...

the user is able to enter keyword corresponding to the desired article they would like to locate in the input box. Once this has been filled out, the user can click enter which will take them to the Search page. Users cannot submit a blank form as this field is required, in addition athere is a requirement of minimum of 1 character to be added before the form can be submitted.

Photo here ...

On the Search page, there is the search result section.

photo here ...


For the search results sections, the user is presented with the keyword searched and below that any successful returns of the keyword will display the articles which math this. The article results are displayed in the same manner as the article post on the home page. The user is able to click on the articlr which will take them to the post detail page for that article.

Photo here ...

Any unsuccessful matches to the user's search will be displayed with a message to say so.

Photo here ...

The following user stories have been achieved from this section:

* As a Site User I can search keywords for specific articles

__Admin Only User Story Testing__

This section tests the user stories for the Admin only functions of the website.

The admin section is accessed by entering 'admin/' at the end of the url for the website. This displayed the login page for the admin from which they can login.

Photo here...

The site admin has various actions available to be able to manage the website such as:

* Delete users
* Create/edit/delete posts and drafts
* Approve and delete comments

From the home section of the admin page, by selecting the Users link under 'Authentication and Authorization' the admin can view the lists of users currently signed up to the website. The admin also has the permission to delete the users by selecting the username and from the drop down selecting the delete user option.

From the home section, the admin can also view comments added by users some of which are pending approval. This is accessed from the Comments link under the 'Post' section. Approved comments are indicated witha green tick under the approved column. Comments pending approval ave the red cross icon. To approve the comment the admin has to tick the unapproved comment from the list, then from the action drop down select the 'approved comments' option. By clicking Go button this will proced to carry out the action to approve the selected commen and also viewed on the website now.

phtos here....

Alternatively selecting the 'Delete selected comments' action will proceed to delete the comment selected. Users will also no longer be able to view the comment on the website.

From the home section, the admin can also view the posts on the website, create new posts and edit/delete any existing ones. This can be accessed from the Posts link under the 'Blog' section. By selecting this link, this will display all the current posts submitted on the website.

phto here ...

The admin can delete any of these posts by selecting the 'Delete selected posts' action from the Action drop down.

The admin can also click on an existing posts by selecting the post tile to view the editor. From this section the admin can edit the posts content, and also has the option to delete the post or to save the changes.

photo here ...

The admin can also create new posts by selecting the Add Post + button. This will open up the editor page which will allow the fields to be populated. The status of the post can also be toggled between Draft or Published. The Published posts can then be viewed on the website, whereas Draft posts cannot.

The admin also has the capability to create, edit and delete posts via the front end of the website.

When logged in as admin, from the navigation the admin has an additional link available 'Add Post'.

hoto here...

Selecting the 'Add Post' link will direct the admin to the add a article page. From here the admin can enter the relevant details on the form to submit the form to add a new article to the website. The admin can select whether to create this post as a draft or publish this straight away. Any published posts can be viewed on the home page, and any draft posts can be accessed in the admin section and approved later once editing is completed.

phtoo here ...

Submitting the form will direct the admin to the home page with a success message.

phtoo here ..

The admin also has the capability to edit or delete posts. There are displayed on each article cards. If delete is selcted then the post is deleted from the database and this is confirmed via an alert message. By selecting the edit option, the admin is directed to the edit article pagge which allows for any changes to be mafe and saved.

Phtoo here ...

These particular admin only permissions cannot be accessed by any other users, and users cannot edit or delete comments or posts or access another users account.

The following user stories have been achieved from this section:

* As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments
* As a Site Admin I can create draft posts so that I can finish writing the content later
* As a Site Admin I can create, read, update and delete posts so that I can manage my blog content
* As a Site Admin I can prevent unauthorised users from having access so that they cannot access admin content or other users' profiles


