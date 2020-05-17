from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, URL


class YtdlLinkForm(FlaskForm):
    ytdl_link = StringField('Paste a link to the video', validators=[DataRequired(), URL()])
    submit = SubmitField('Get video download URL')

    host = StringField('Host')
    uploader = StringField('Uploader Name')
    download_name = StringField('Download Filename')
    muxed_resolution = StringField('Resolution')
    muxed_url = StringField('Download URL')
    best_video_resolution = StringField('Best Available Video Resolution')
    best_video_url = StringField('Download URL        Warning! NO Audio.')


class ReadTimeForm(FlaskForm):
    text = TextAreaField('Add text here', validators=[DataRequired()])
    submit = SubmitField('Calculate read time')
    read_time = StringField('Text read time')


class FileConverterForm(FlaskForm):
    file = FileField('Add your file here', validators=[DataRequired()])
    submit = SubmitField('Convert to MP3')
