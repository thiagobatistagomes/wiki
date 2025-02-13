Wiki Encyclopedia Project Documentation
Overview
This project is a Django-based implementation of a basic online encyclopedia, similar to Wikipedia. The encyclopedia entries are stored in Markdown format and rendered as HTML when viewed by users. The project aims to provide a lightweight, user-friendly platform for creating, viewing, searching, editing, and managing encyclopedia entries.
Project Structure
encyclopedia/: Contains the main application files.
urls.py: URL routing for the application.
views.py: View functions for handling requests and rendering pages.
templates/encyclopedia/: Contains HTML templates.
index.html: Template for the homepage displaying all encyclopedia entries.
entry.html: Template for displaying a single encyclopedia entry.
create.html: Template for creating a new encyclopedia entry.
edit.html: Template for editing an existing encyclopedia entry.
util.py: Utility functions for interacting with encyclopedia entries.
entries/: Directory where each encyclopedia entry is stored as a Markdown file.

Getting Started

HOW TO RUN THE PROJETCT
Prerequisites
1 - Install Python
Ensure that Python 3 is installed on your system. You can check the Python version with the following command: python --version
2 - Install Django
Install Django and other dependencies using pip: pip install django markdown2
3 - Download the Project
Clone or download the project code to your local machine.
4 - Set Up the Django Project
Run migrations to set up the database (if necessary) with: python manage.py migrate.
5 - Run the Development Server:
Start the Django development server: python manage.py runserver

Project Files:

util.py provides three utility functions:
list_entries(): Returns a list of all encyclopedia entries.
save_entry(title, content): Saves a new encyclopedia entry.
get_entry(title): Retrieves the content of an encyclopedia entry by title.
Markdown files for each encyclopedia entry are stored in the entries/ directory.

Functionality Requirements
1. Entry Page
URL format: /wiki/TITLE
Render a page displaying the content of the specified encyclopedia entry.
2. Index Page
List all available encyclopedia entries on the homepage.
3. Search Functionality
Allow users to search for entries by title or partial match.
If the search query matches an exact title, users will be redirected to the corresponding entry page.
If no exact match is found, it will show a search results page with entries containing the query as a substring.
Clicking a result should redirect to the full entry page.
4. Create New Page
Goal: Allow users to create a new encyclopedia entry.
Users can enter the title and Markdown content for a new page.
5. Edit Page
Allow users to edit an existing entry.
Provide a form with the current Markdown content pre-populated in a textarea.
Users can modify the content and submit the form to save changes.
Once saved, the user is redirected back to the entry page.
6. Random Page
Display a random encyclopedia entry.
Clicking "Random Page" in the sidebar will take the user to a randomly selected entry.
7. Markdown to HTML Conversion
Convert Markdown content into HTML before rendering.

Pages:
Home Page (index.html): Displays a list of all entries with links to their pages.
Entry Page (entry.html): Displays the content of a specific entry, converted from Markdown to HTML.
Create Page (create.html): Form for users to create a new entry.
Edit Page (edit.html): Form for users to edit an existing entry.
Search Results Page: Displays search results when no exact match is found.

Conclusion
This project provides a solid foundation for a basic online encyclopedia using Django. By handling Markdown files for content and dynamically rendering them as HTML, users can easily view, search, create, edit, and manage encyclopedia entries. The project can be further enhanced by adding features like user authentication, content moderation, and advanced search functionality.