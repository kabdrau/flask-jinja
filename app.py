from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def select_story():
    """Select story template."""
    
    all_stories = stories.values()

    return render_template("home.html", stories = all_stories)

@app.route("/questions")
def ask_questions():
    """Generate and show form to ask words."""

    story_id = request.args["story_id"]
    story = stories[story_id]
    prompts = story.prompts

    return render_template("questions.html", story_id = story_id, title = story.title, prompts = prompts)

@app.route("/story")
def show_story():
    """Show story result."""

    story_id = request.args["story_id"]
    story = stories[story_id]
    new_story = story.generate(request.args)

    return render_template("story.html", title = story.title, story = new_story)