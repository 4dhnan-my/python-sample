from django.shortcuts import render


def home(request):
    context = {
        "name": "Adhnan",
        "role": "Python Django Developer",
        "email": "adhnan.official.id@icloud.com",
        "location": "India",
        "skills": [
            {
                "name": "Python",
                "description": "I use Python to write clean backend logic, handle data, and build reliable web application features.",
            },
            {
                "name": "Django",
                "description": "I build Django apps with routes, views, templates, static files, and simple database-driven workflows.",
            },
            {
                "name": "HTML5",
                "description": "I create structured pages with semantic HTML so the website content is clear and easy to maintain.",
            },
            {
                "name": "CSS3",
                "description": "I style responsive layouts, animations, hover effects, and modern dark interfaces using custom CSS.",
            },
            {
                "name": "JavaScript",
                "description": "I add interactive behavior such as mobile menus, scroll effects, reveal animations, and card interactions.",
            },
            {
                "name": "SQLite",
                "description": "I use SQLite for local Django projects to store app data in a simple and lightweight database.",
            },
        ],
        "projects": [
            {
                "title": "Portfolio Website",
                "description": "A responsive personal website built with Django templates and static frontend files.",
                "tech": "Django, HTML, CSS, JavaScript",
            },
            {
                "title": "Task Tracker",
                "description": "A simple app idea for creating, updating, and organizing daily tasks.",
                "tech": "Python, Django, SQLite",
            },
            {
                "title": "Weather Dashboard",
                "description": "A frontend dashboard concept that displays weather cards and clean visual summaries.",
                "tech": "JavaScript, API, CSS",
            },
            {
                "title": "Student Management System",
                "description": "A Django web app concept for managing student profiles, courses, and basic records.",
                "tech": "Django, SQLite, Bootstrap",
            },
            {
                "title": "Blog Platform",
                "description": "A content publishing project with post listings, detail pages, categories, and clean templates.",
                "tech": "Python, Django, HTML, CSS",
            },
            {
                "title": "Expense Tracker",
                "description": "A simple finance tracker idea for recording expenses and viewing spending summaries.",
                "tech": "Django, JavaScript, SQLite",
            },
            {
                "title": "Landing Page Design",
                "description": "A modern responsive landing page focused on layout, animations, and visual presentation.",
                "tech": "HTML, CSS, JavaScript",
            },
        ],
    }
    return render(request, "portfolio/home.html", context)
