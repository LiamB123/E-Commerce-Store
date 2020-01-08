[![Build Status](https://travis-ci.org/LiamB123/E-Commerce-Store.svg?branch=master)](https://travis-ci.org/LiamB123/E-Commerce-Store)

# Retro Jerseys  https://liams-the-store.herokuapp.com/
##An ecommerce site for selling retro NBA jerseys

Retro Jerseys is an ecommerce site for buying retro nba jerseys, mainly from the 90's and 2000's era. 
The purpose of the site for enthusiasts in the niche to buy hard to find jerseys, or sell their own collection through the site. 
Its a simple ecommerce webiste, which requires membership to buy from the site.
Since the success of the "Sneakerhead" market, I feel it is an angle not yet taken within the sports entusiast/memorabilia/fashion industry.


### UX


The UX i wanted to achieve was ease of use at all times, i wanted a full purchase to take  minimal clicks and clear display of product and price. 
My Ux focus was on ease of access and making all products available quickly findable, the desirable black and white styling fo the backround allows the real focus, the coloured jerseys, to stand out in the store section of the page.
There are few but valuable calls to action on the home page both to sign up for the site, to allow acces, and to traverse the simple html pages. 



### User Stories:
There are 2 key users I would like to use this page with scale to grow out from this starting niche.

User 1: The Buyer
I am a nostalgic Jersey Enthusiast, looking to buy a 90's Nba jersey for a friend. I havent been able to find a particular jersey (Such as say a Black Pippen Jersey from the 90's). 
I want to buy a Jersey online to send to my friend as a gift. I want the process to be quick as i often get lost on other retail website, Too many clicks!

User 2:The Seller
I am a collector of Retro Jerseys, and I'm Looking to sell off some of my collection but cant deal with the hassle of meeting potential buyers. 
I want a quick way of contacting a retailer to sell the jersey on my behalf, All i want is to send it off for a good price and have the money sent back to me.

User 3: The Window Shopper
I want to browse some old jerseys because i was a big fan of the styles of jerseys over the years, I want to buy one but im not yet sure if im ready to buy and i dont want to give over any of my details to any sites.


### Features
Feature 1 - Accounts
 The Accounts app allows users to login or log out of the website, creating a username and saving their info for ease of use in return visits to the site. Having an account also allows users to contact the website for queries,questions and possible sales of jerseys. Having an account is also a requirement for anyone looking to buy a jersey from the website as the functions demand a user be logged in first. This is added security for both user and site owner.
This also grants the site owner an email list for possible future marketing such as site related promotions i.e. sales,deals
changes or updates. This will be elaborated on in the Features left to implement.


Feature 2 - Products
  The Products app allows products to be written, displayed and saved on the site. This app has strict models to ensure every product has a similar look for uniformality throughout the site. Each product requires a title, brief description, price and an image of the item. Their is also a field for the Team it came from which will be elaborated on in the Features left to implement. Products can be easily added by an admin quickly, with the media files being stored in an S3 AWS bucket to allow the site load quicker. 


Feature 3 - Cart
  The Cart app allows users who are signed in to add products to a cart so they can browse and save items for purchase later. The app allows the users to add to, edit the amount and removee all items if they so choose. It also displays in an easily read fashion all items currently in the users cart, allowing them to proceed to the checkout.
  
  
Feature 4 - Checkout
    The Checkout allows users to purchase the items in their cart. The app uses the stripe API to handle the transaction. 
The views are constructed in a way that all fields necessary for the transaction are requirements on the site, with easy to fill out forms to process the payment, with a final reminder of what you are buying before you hit purchase!
The sensitive details such as card information is hidden with cookies, so no access is available to the site owner with diirect contact to stripe the only means of handling any potential dispute. This is an added safety measure.

Feature 5 - Contact Us
  The Contact app alows users to contact the site owner with any issues/queries regards the purchase, delivery and any other topics of interest. The simple to fill out form provides the site owner with the inquirer's contact details and content of their message, so the conversation can be moved onto email after first contact. It is a quick and clear method of contact between site owner and cutomer.
  
  
### Features Left to Implement

  Feature 1 - Library for the products
    At the moment as the stores product offering is very limited there is no demand for a better search for the products.
However if the site is to scale succesfully it will need a multidude of jerseys from different teams and way down the line, different sports. At the moment products are inputed with a team parameter which means they are being tagged and a quick search app that calls upon that tag can provide a new layout for the store when the demand requires it.


Feature 2 - Expand from Just NBA Jerseys!
  The choice of NBA jerseys to start with is because it is a passion of mine, however it there is no reason bar demand at this point in time on why the site couldnt be scaled up to include Football, American Football, Hockey or any sport where the demand is there for nostalgic jerseys. In a time where sustainability is becoming a hot topic in fashion it is an excellent medium for the conscientious buyer.
  
Feature 3 - Personal Profile
  At present the sign up feature just allows a user to use the store, they dont have a hub or profile of their own which can be implemented. This hub would have info such as previous purchases, receipt details and a watch list for specific products if they come into the store.
  
  
Feature 4 - Product Ratings
  This would allow users to rate the quality of the product and leave a review of their experience with the Retro Jerseys Store. These testimonials are integral for business growth as it puts prospect buyers at ease that the site can be trusted and has a proved track record. 
A simple rating out of 5 star with a comment would be ideal as it is a crucial aspect the site is currently missing.
  

Feature 5 - Menu Button on mobile
  The current bug annoying me and the user most is on the mobile version of the site the menu button clicks, however it doesnt stay open. This is do to a conflict with the stripe js and needs to be resolved before official launch of the site. 
It is only a small bug but its impact on the overall user experience is massive.


### Technologies Used

Django - https://www.djangoproject.com/
  Django was the basis of the entire project, it helped with the creation of several python based apps, providing authentication and authorisation libraries and a lot of built in conveniences for me while programming. From handling url roots, backend authentication security, easily constructed forms and storage.
  
Python - https://www.python.org/download/releases/3.0/
  Python was used as the basis for the site, allowing for easily repeated functions.
  
JQuery - https://jquery.com/
  JQuery was used to help manipulate the DOM model throughout the webpage and handle stripes javascript!

Bootstrap - https://getbootstrap.com/
  Bootstrap was utilised for front-end development, its styling and dom manipulation allowed for ease of creating reactive styling allowing the 

AWS S3 Bucket - https://aws.amazon.com/s3/
  S3 was utilised to collect all static information for the site, hosting the css, js and media files for the site.
  
AWS IAM -https://aws.amazon.com/iam/
  IAM was used as an added assurance that the site was being interacted with solely authorised and authenticated 
  
Stripe - https://stripe.com/ie
  Stripe's API was used to securely handle the transactions of purchases on the site.
  
GitHub - https://github.com/
  GitHub was used for version control and integrated with heroku for deployment.
  
Travis-ci - https://travis-ci.org/
    Travis was used as a continous integration testing environment on each commit to make sure my code was passing.

### Testing
  
 Travis-CI was used to make sure that continous testing was undertaken at every commit. After many attempts with multiple depency and library version changes it passed! 
   
To maximise my testing i ran all tests on varying devices available (desktop, laptop, tablet and iphones 8 onward) 
  
#### Home Page
 
1. The first test was to push all buttons, make sure they led to the correct pages and that the animation on the buttons triggered when hovered over.
The Nav Bar was to have "Store, Register, Sign In" as options for a non signed in user and then "Store, Log Out, Cart". After trying it out on all devices I noted one key issue.
The key problem found during this testing was that on phones, the dropdown menu doesnt remain open once clicked. This is to due with a conflict in the JQuery for Stripe and the Bootstrap used for the dropdown menu.

2. The Contact Forms off of the home page were tested, with repeatedly submitting forms that were missing variables. They were successfully refused by the page requiring an email in the contact section and limiting the size of the input in the message section. 

#### Store

1. The Store section was tested by attempting to add excessive amounts of the products, which was successfully found to be limited to 19 items per user at a time. 
2. The products themselves were tested as the django admin would not accept a product without all necessary requirements. The images succesfully saving to the S3 Bucket.
3. The amount of a product was easily edited and saved correspondingly in the cart. 

#### Cart
1. The cart's contents were easily manipulated in value, however it was noted that the addition of a trash can icon for an instant removal of the product would of been an added UX idea.
2. The cart could be accessed directly from the url, however it could not be added to without being signed in so I felt that was okay.

#### Checkout
1. The Checkout requried all fields to be filled out with multiple forms partly filled out succesfully refused by the site requiring the fields to be filled out correctly. Email fields,number fields all behaved as was hoped.
2.The Stripe payments were succesful while using the test card number (4242 4242 4242 4242), They were succesfully accepted by stripe as test payments with actual card payments not succesfully going through as the stripe account is not activated.



### Deployment

This project is deployed on Heroku. 
To get the project to deploy on heroku within the settings.py app I created several enviornnmental factors that could be kept hidden for security purposes. Thanks to these Config Vars Heroku can have them plugged in for deployment.
Before Deployment, Travis-ci  testing had to pass and once completed deployment was very simple.
Linking the GitHub repo to the Heroku app allowed all code to be ran through once a clear Procfile was added to the project.
The Key difference between the deployed and development versions of the project was the database used. In development a SQLite database was used but with Heroku, a Postgres database was utilised. 
Again this was easly linked into the ConfigVars thanks to Django's Settings.py file at the heart of the project.


If you wish to run the code locally you will need to sub in your own secret key and all enviornmental variables,
I find GitPod the quickest way to clone and run a project such as this locally!



### Credits

Certain aspects of the creation of the accounts, checkout and cart apps are taken from the Code Institutes tutorials on how to create these apps, written in the video by Niel McEwan and Matt Rudge.


### Content
The text for all is written by myself, 

### Media
The photos used in this site were obtained from a google image search, with most originating from https://www.fanatics.com/.

### Acknowledgements
I received inspiration from this project as it was always an interest of mine to see how successful a niche topic such as this would do in the highly diluted sports merchandise industry within Ireland.
