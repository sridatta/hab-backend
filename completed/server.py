# #Post pages
from flask import *
from flask_simpledb import SimpleDb

app = Flask(__name__)
db = SimpleDb()

@app.route("/")
def homepage():
    posts = db.getPosts()
    return render_template('home.html', posts=posts)

@app.route('/create', methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template('create.html')
    else:
        title = request.form["title"]
        content = request.form["content"]

        db.addPost(title, content)

        return redirect('/')

# We've been neglecting this little function down here but it's time has
# come! When the client requests a particular post ID, get it out of the
# database and render it onto our new template.
@app.route('/posts/<post_id>')
def show_post(post_id):
    post = db.getPost(int(post_id))
    return render_template("post.html", post=post)

#
if __name__ == "__main__":
    app.debug = True
    app.run()
