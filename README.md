# Coffee Project

### Project 3 with Code Institute 
#### Rebecca Manning

For the final project with Code Institute I chose to create a website for a Coffee shop that provides monthly subscriptions and aims to integrate the local community online ...and so with an attempt at some humour, I named it Starbex.

----------------
### STARBEX
#### What the project does, needs it fulfills & functionality

The project offers customers the chance to purchase a certain number of coffees per month at a discounted price. This makes it quick and easy for them to pop into the store and show the QR code from their phone to buy a coffee.

The project also aims to integrate the community through online blogs, forums and profiles. Through having to subscribe to coffees, you create your own profile that you can log in and out of. Each profile is unique and has information suited to the user. For example it may show you how many coffees you have left for the month and days till renewal if you are Subscribed. If you aren't subscribed it shows you a link to go and purchase some coffees with the price list. The profile also tells if new members have joined and shows them to the new member section to introduce yourself.

When you're logged in you can can get involved by reading regular blogs as well as commenting. You can also do the same for forums and even post your own. It allows the store to post weekly announcements and keep everyone informed as well as hear feedback.

----------------
### TECHNOLOGIES

* Bootstrap
* FlexBox
* CSS
* HTML
* JavaScript
* jQuery
* Python
* Django
* Paypal

----------------
### DEPLOYMENT

**Heroku** - https://starbex.herokuapp.com/

Try it out for youself and log in with someone who has purchased and someone who hasn't to see the difference

Email | Password | Subscribed
------------ | ------------- | -------------
rebm@hotmail.co.uk | beccam01 | Yes
mrfairtrade@hotmail.co.uk | mrf01 | No

----------------
### TESTING

* [flake8](http://flake8.pycqa.org/en/latest/)
* https://validator.w3.org/
* I frequenty asked friends, family and peers to have a look trhough my website and give feedback on code, functionality or aesthetics that could be improved.
* Testing code in each App, created under tests.py.
* I constantly tested the website on different browsers as well as different size screens.

----------------
### CREDIT

* Scattered Polaroid Gallery - https://tympanus.net/codrops/2014/01/28/scattered-polaroids-gallery/
* A lot of my Code I got from Code Institute as it is the course I am taking - I have showed in my annotation that I understand it all and also personalised it a lot to my needs.
* Font-Awesome - http://fontawesome.io/
* Images were sourced from Pixabay (a free royalty-free images site) or created myself.

----------------
### CHALLENGES
#### What was kept/changed to fit my need

* One of my main aims was to focus on the little details of the website that people using it will see. I really wanted the user to enjoy the unique experience of going through the website. Although this took a lot of time and late nights, it was worth it! I created an animated favicon (although it does not work on chrome), I focussed on making the site interactive as well as a few more small things that I'll let you all discover when visiting the site.
* As you can see, the site is interactive is places. However, at one point in creating the website I realised a lot of the animation was slowing down the website. So from this, I decided to take out certain things that weren't needed like hovering over the back button in a forum thread and being able to see the page it sends you to.
* Although the website does not have a mobile first design, I focussed a lot on making sure it works. I kept checking on different size screens and resolutions as I went through the project.
* The About page was editted a lot as I had a particular way I wanted it to look and feel. It needed to be straight to the point and not boring which is why I made it so interactive.
* I wanted the home page to be simplistic but also attention grabbing for new, potential customers. With this in mind I found a Polaroid Gallery which I used and added some coffee shop music.

----------------
### TO-DO

Unfortunately I ran out of time to finish certain parts, but if I had a bit longer I would have worked on:
* Cancel Subscription button working on profile.html and coffees.html
* Search Bars on Forum page and Blog page working
* Can not currently post a new thread without a Poll
* Add some tests to the Apps: coffees, polls and paypal_store

----------------
### PROJECT BRIEF
#### Code Institute

**Build An Issue Tracker**

* Now that you’re a full fledged web developer you’ve decided it’s probably time for you to start your very own cool, modern startup, offering the extremely awesome UnicornAttractor webapp to your users. It’s really really amazing, but we don’t care about it at all in this project. The interesting thing is the business model that you’ve decided upon – you chose to offer the service and bug fixes for free, but ask for money from your users to develop additional features.

* To manage the tracking of bugs and feature requests, you decided to create an Issue Tracker that will allow your users to submit and track any issues (bugs or feature requests) related to using the UnicornAttractor.

* The basic entity in the Issue Tracker is a ticket describing a user’s issue, and similar to Github’s issue tracker, you should allow users to create tickets, comment on tickets, and show the status of the ticket (e.g. ‘to do’, ‘doing’, or ‘done’). As mentioned, issues come in two varieties – ‘bugs’ (which you’ll fix for free, eventually), and ‘features’ which you’d only develop if you’re offered enough money. To help you prioritise your work, your users will be able to upvote bugs (signifying ‘I have this too’), and upvote feature requests (signifying ‘I want to have this too’). While upvoting bugs is free, to upvote a feature request, users would need to pay some money (with a minimum amount of your choice) to pay for your time in working on it. In turn, you promise to always spend at least 50% of your time working on developing the highest-paid feature.

* To offer transparency to your users, you decide to create a page that contains some graphs showing how many bugs and features are tended to on a daily, weekly and monthly basis, as well as the highest-voted bugs and features.

* Add any additional pages that would help you attract users to the Issue Tracker (and have them pay you well). To make the users participate as much as possible in your online community, make sure that your UI/UX is sublime. Feel free to add additional features, such as a blog, additional perks for active participants, etc…

* If you want to have some more fun with this, feel free to also add pages describing your fictional UnicornAttractor application 🙂

* And of course, as this project is going to be lifeblood of your company, it’s important that new developers that join the company will be able to get up and running as quickly as possible. Documentation is the best way to achieve this.

**Choose Your Own Project**

* If you choose to create your own project, the scope should be similar to that of the example brief above, or the we_are_social project from earlier in this stream. If you want some ideas, please ask your mentor for advice and direction.

-----------------
### PROJECT GUIDELINES
#### Code Institute

* Build a web app that fulfills some actual (or imagined) real-world need. This can be of your own choosing and may be domain specific.

* Write a README.md file for your project that explains what the project does and the need that it fulfills. It should also describe the functionality of the project, as well as the technologies used. Detail how the project was deployed and tested and if some of the work was based off other code, explain what was kept and/or how it was changed to fit your need. A project submitted without a README.md file will FAIL.

* The project must be a brand new Django project, composed of multiple apps (an app for each reusable component in your project).

* The project should include an authentication mechanism, allowing a user to register and log in, and there should be a good reason as to why the users would need to do so. E.g. a user would have to register in order to persist their shopping cart between sessions (otherwise it would be lost).

* At least one of your Django apps should contain some kind of e-commerce functionality using Stripe and/or Paypal. This may be a shopping, or subscriptions, or single payments, etc.

* Include at least one form with validation, that will allow users to create and edit models in the backend (in addition to the authentication mechanism).

* The project will need to connect to an SQL database using Django’s ORM, or to a Document-Oriented database (e.g. MongoDB) using pymongo.

* The UI should be responsive, use either media queries or a responsive framework such as Bootstrap to make sure that the site looks well on all commonly-used devices.

* As well as having a responsive UI, the app should have a great user experience.

* The frontend should contain some JavaScript logic to enhance the user experience.

* Whenever relevant, the backend should integrate with third-party Python/Django packages, such as Disqus, Django Rest Framework, etc. Strive to choose the best tool for each purpose and avoid reinventing the wheel, unless your version of the wheel is shinier (and if so, consider also releasing your wheel as a standalone open source project).

* Make sure to test your project extensively. In particular, make sure that no unhandled exceptions are visible to the users, in any circumstances. Use automated Django tests wherever possible. For your JavaScript code, consider using Jasmine tests.

* Use Git & GitHub for version control. Each new piece of functionality should be in a separate commit.

* Deploy the final version of your code to a hosting platform such as Heroku.

-----------------
### FINAL NOTES

I would just like to mention that the reason the github uploads are not spread out more evenly is because I've also been in my final year at Universtiy so have been working on this course when I haven't had exams or coursework.
