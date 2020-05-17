import os, secrets
from flask import Flask, render_template, request, send_from_directory
from static.forms import YtdlLinkForm, ReadTimeForm
from static.engines.ytdl_engine import YtdlEngine
from static.engines.readtime_engine import calc_readtime
from static.engines.audio_conv_engine import convert_audio_mp3


app = Flask(__name__)
app.config.from_object('config.Config')


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


@app.route('/audio_converter', methods=['GET', 'POST'])
def audio_converter():
    if request.method == 'POST':
        if request.files:
            file = request.files['file']
            hash_filename = secrets.token_hex(15)
            ext = os.path.splitext(file.filename)[-1]
            file.save(os.path.join(app.config["AC_UPLOADS"], hash_filename + ext))
            converted_filename = convert_audio_mp3(app.config['AC_UPLOADS'] + '/' + hash_filename + ext)
            return send_from_directory(app.config['AC_CONVERTED'], converted_filename, as_attachment=True), os.remove(app.config['AC_CONVERTED'] + "/" + converted_filename)
        else:
            return 'no file'
    elif request.method == 'GET':
        print('get')
    return render_template('audio_converter.html', as_attachment = True)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
