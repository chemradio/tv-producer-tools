from flask import Flask, render_template

from forms import YtdlLinkForm, ReadTimeForm, FileConverterForm
from ytdl import YtdlEngine
from readtime import calc_readtime

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
        print(ytdl_list)
        twoformats, form.host.data, form.uploader.data, form.muxed_resolution.data, form.muxed_url.data, form.best_video_resolution.data, form.best_video_url.data = ytdl_list
    return render_template('ytdl.html', form=form, twoformats=twoformats, ytdl_list=ytdl_list)


@app.route('/readtime', methods=['GET', 'POST'])
def readtime():
    form = ReadTimeForm()
    if form.validate_on_submit():
        form.read_time.data = calc_readtime(text=form.text.data)
    return render_template('readtime.html', form=form)


# @app.route('/audio_converter', methods=['GET', 'POST'])
# def audio_converter():
#     form = FileConverterForm()
#     return render_template('audio_converter.html', form=form)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
