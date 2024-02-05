<h1>Recipe Website (Django CRUD) with Login and Registration</h1>

<p>This Django project is a Recipe Website that allows users to perform CRUD (Create, Read, Update, Delete) operations on recipes. Additionally, the website includes a user authentication system with login and registration pages. Users must be logged in to add new recipes.</p>

<h2>Features</h2>

<ul>
    <li><strong>Recipe CRUD Operations:</strong>
        <ul>
            <li>Create, read, update, and delete recipes.</li>
            <li>View a list of all recipes on the home page.</li>
        </ul>
    </li>
    <li><strong>User Authentication:</strong>
        <ul>
            <li>Secure user registration with validation.</li>
            <li>Login system to authenticate users.</li>
        </ul>
    </li>
    <li><strong>Bootstrap Styling:</strong>
        <ul>
            <li>Utilizes Bootstrap for a responsive and visually appealing design.</li>
        </ul>
    </li>
</ul>

<h2>Requirements</h2>

<p>Make sure to install the required dependencies before running the project:</p>

<pre>
pip install django
</pre>

<h2>How to Run</h2>

<ol>
    <li>Clone the repository:</li>
    <pre>
    git clone https://github.com/mahim008/Recipe_Website_Django.git
    cd Recipe_Website_Django
    </pre>
    <li>
    Run the development server: </li>
    <pre>
    python manage.py runserver 8000
    </pre>
    <li>Access the website at
    <pre>
    http://127.0.0.1:8000/
    </pre>
    </li>
</ol>

<h2>Usage</h2>

<ol>
    <li>Register a new account on the registration page.</li>
    <li>Log in with your registered credentials.</li>
    <li>Explore the list of recipes on the home page.</li>
    <li>Add, update, or delete recipes by navigating to the appropriate pages.</li>
</ol>

<h2>Project Structure</h2>

<ul>
    <li><strong>login/</strong>:  for user login</li>
    <li><strong>registration/</strong>:  for user registration</li>
    <li><strong>recipes/</strong>:  for managing recipes.</li>
</ul>

<h2>Dependencies</h2>

<ul>
    <li><a href="https://www.djangoproject.com/">Django</a></li>
    <li><a href="https://getbootstrap.com/">Bootstrap</a></li>
</ul>

<h2>Notes</h2>

<ul>
    <li>Ensure that your database is configured in the <code>settings.py</code> file.</li>
</ul>

<p>Feel free to explore and customize the project according to your needs. If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request.</p>

