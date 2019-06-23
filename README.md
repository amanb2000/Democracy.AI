# Democratiam_Intelligentia

### The Premise
Ever since I started my journey into machine learning in grade 11, I have been mystified by how unavailable people's findings are for applied papers. I would read papers about people training amazing algorithms that could do things like predicting life expectancy from pictures of people's faces, and all I wanted was to try it for myself and have access to the algorithm. However, recreating the papers' results is a challenge in itself, making the concrete results inaccessible and impossible to play with. In essence, much of the power that cutting-edge AI research has is held by a select few. When our team formed, we found that we all shared this common frustration. We saw our opportunity to make a difference.

We created a platform that enables people to put their trained algorithms online in an accessible way so that lay people can use them easily. We made a platform that a random student with no coding experience can find and play around with cutting-edge algorithms in an easy and productive way. Our platform connects machine learning enthusiasts and researchers directly to people who can use their discoveries and algorithms with minimum overhead. In essence, we have democratized AI.

### Our System: Technologies Used
* Flask: General Upload architecture
* Rust with Rocket for Servers: Compiled Executables for Maximum Efficiency
* Python and TensorFlow: For Deep Learning Models
* SQL for voting and keeping track of ML Models
* User validation (custom in Flask/SQL)
* JavaScript/HTML5/CSS3/Angular/jQuery for UI and requests
* Custom compiled web pages with Python scripts and JSON for client-side web pages

### Our System: Data Flow
1. Clients upload machine learning algorithms to a forum-style system.
2. The code is asynchronously compiled with a custom Rust library in the back-end for quick service to the end user.
3. The end user is served a single packaged entity, dynamically written with custom Python libraries to be hosted and run on our remote server OR on their remote client.
4. The end user is free to play with the algorithm as they wish, and they can vote, bookmark, and report the algorithm on the forum as necessary.

### What We have Done
In essence, we have democratized AI such that any lay person can make an account, download, play with, and vote on algorithms from anyone from first year comp sci students to cutting-edge AI researchers who choose to make thir algorithms public.
