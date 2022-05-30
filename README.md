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




