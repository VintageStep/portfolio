from flask import Flask, render_template, abort


def create_app():
    app = Flask(__name__)

    projects = [
        {
            "name": "Another Port of Northwind DB for Oracle", #more exactly like title
            "thumb": "images/northwind.png", #img for card ver
            "hero": "images/northwind-hero.svg", # img for detailed ver
            "categories": ["SQL","PL-SQL"],
            "slug": "northwind", # url end-point -> project page
            "demo": "https://github.com/VintageStep/NorthwindOracle_DDL", # demo link
            "code": "https://github.com/VintageStep/NorthwindOracle_DDL", #repo
            "class": "text-first", #CSS class that help with the main layout
            "description":"When I was studying Oracle Database I realized that " + 
            "the examples provided weren't enough for my liking. And since I'm familiar " +
            "with Northwind-DB, I decided to make a port of it myself. This script preserves " +
            "regional characters and automates the creation of the schema. There's no Live Demo " +
            "available for this project, but the source code should suffice.",
        },
        {
            "name": "Portfolio", #more exactly like title
            "thumb": "images/portfolio.svg", #img for card ver
            "hero": "images/portfolio-hero.svg", # img for detailed ver
            "categories": ["Python","HTML","CSS"],
            "slug": "portfolio", # url end-point -> project page
            "demo": "/about/", # demo link
            "code": "https://github.com/VintageStep/portfolio", #repo
            "class": "image-first", #CSS class that help with the main layout
            "description":"While a project like this could be done just with HTML and CSS, " + 
            "I decided to use FLASK to manage url end-points and give it a " +
            "bit of flavor by adding CSS classes in specific situations. " +
            "Finally, I did all the images using Figma.",

        },
        {
            "name": "Habit Tracker", #more exactly like title
            "thumb": "images/habit-tracker.svg", #img for card ver
            "hero": "images/habit_tracker-hero.svg", # img for detailed ver
            "categories": ["Python","HTML"],
            "slug": "habit-tracker", # url end-point
            "demo": "https://little-tracker.herokuapp.com", # demo link
            "code": "https://github.com/VintageStep/habit-tracker", #github repo
            "class": "text-first", #CSS class that help with the main layout
            "description":"With this FLASK project, I learned more about how to " + 
            "manage GET and POST requests, and how to render objects " +
            "with dynamic behavior. I also had the chance to use MongoDB again.",
        },
        {
            "name": "Microblog", #more exactly like title
            "thumb": "images/microblog.svg", #img for card ver
            "hero": "images/microblog-hero.svg", # img for detailed ver
            "categories": ["Python","HTML","CSS"],
            "slug": "microblog", # url end-point
            "demo": "https://vintagestep-microblog-demo.herokuapp.com", # demo link
            "code": "https://github.com/VintageStep/python-web-microblog", #github repo
            "class": "image-first",
            "description":"This was the first Flask project I did from scratch " + 
            "and also my first approach to MongoDB and application deployment, with Heroku in this case. " +
            "It was also the moment I started studying CSS more appropiately",
        },
            {
            "name": "Front-End Snippets", #more exactly like title
            "thumb": "images/snippets.svg", #img for card ver
            "hero": "images/snippets-hero.svg", # img for detailed ver
            "categories": ["HTML", "CSS"],
            "slug": "snippets", # url end-point
            "demo": "https://codepen.io/vintagestep/details/MWVQPOp", # demo link
            "code": "https://codepen.io/vintagestep/pen/MWVQPOp", #github repo
            "class": "text-first",
            "description":"After finishing the Microblog project I sidetracked a bit " + 
            "in order to learn CSS without relying on external tools " +
            "so I can work with page layouts and styles more independently later on. " + 
            "I will display here more snippets in the future. ",
        },
    ]

    slug_to_project = {project["slug"] : project for project in projects}

    @app.route("/")
    def index():
        return render_template("index.html", projects = projects)

    @app.route("/about/")
    def about():
        return render_template("about.html")

    @app.route("/contact/")
    def contact():
        return render_template("contact.html")

    @app.route("/project/<string:slug>/")
    def project(slug):
        if slug not in slug_to_project:
            abort(404)
        return render_template(
            f"project_{slug}.html", 
            project=slug_to_project[slug]
        )

    @app.errorhandler(404)
    def page_not_found(error):
        # 404 status code for the browser at the end.
        return render_template("404.html"), 404
    
    return app