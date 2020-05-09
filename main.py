from flask import render_template
from YtdlFlask.forms import YtdlLinkForm, ReadTimeForm
from YtdlFlask.ytdl import YtdlEngine
from YtdlFlask.readtime import calc_readtime
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c6eafc9425925847cb4218e97d28a6cb'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/ytdl', methods=['GET', 'POST'])
def ytdl():
    form = YtdlLinkForm()
    twoformats=None
    ytdl_list=None
    if form.validate_on_submit():
        ytdl_list = YtdlEngine().go_ahead(form.ytdl_link.data)
        twoformats, form.host.data, form.uploader.data, form.muxed_resolution.data, form.muxed_url.data, form.best_video_resolution.data, form.best_video_url.data = ytdl_list
        print(ytdl_list)
    return render_template('ytdl.html', form=form, twoformats=twoformats, ytdl_list=ytdl_list)


@app.route('/readtime', methods=['GET', 'POST'])
def readtime():
    form = ReadTimeForm()
    if form.validate_on_submit():
        form.read_time.data = calc_readtime(text=form.text.data)
    return render_template('readtime.html', form=form)
